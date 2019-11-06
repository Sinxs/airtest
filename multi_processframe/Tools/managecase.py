# -*- encoding=utf8 -*-
__author__ = "Lee.li"

import unittest, sys, math
from airtest.core.api import *
from BeautifulReport import BeautifulReport
from multi_processframe.Tools import multiprocessing, analysis, emali
from multi_processframe.TestCase import *

def run_testcase(devices):
    """
    实现用例分配到设备以及多进程管理的方法
    :param devices: main方法传过来的单独设备
    :return: 没有返回值
    """
    config_Path = os.path.join(os.getcwd(), "config.ini")
    case_Path = os.path.join(os.getcwd(), "TestCase")
    devices_List = analysis.analysis_config(config_Path, "deviceslist")  # 设备的数量
    if not os.path.exists(case_Path):
        print("测试用例需要放到‘TestCase’文件目录下")
    report_Path = os.path.join(os.getcwd(), "Report")
    if not os.path.exists(report_Path):
        os.mkdir(report_Path)  # 创建Report文件夹
        os.mkdir(report_Path + "/Screenshot") # 创建Screen文件夹
    config_Test_List = analysis.analysis_config(config_Path, "testcase") # 从配置文件中后去待测文件
    script_List = analysis.get_script_list(case_Path) # 获取TestCase下文件可用的测试文件
    suite = unittest.TestSuite()
    cases = [] # 定义一个空的待测用例列表
    for i in range(len(config_Test_List)):  #循环遍历
        file_Name = "TC_" + config_Test_List[i] # 把配置列表中的用例加上tc标志
        if file_Name in script_List:
            cases.append(file_Name)
            if i == len(config_Test_List) - 1:  # 当TestCase全部用例循环加载之后

                for b in range(devices_List.index(devices)+1): # 根据设备的数量循环把用例分成若干等分
                    split_Cases = cases[math.floor( b / len(devices_List) * len(cases)):math.floor((b + 1) / len(devices_List) * len(cases))]  # 到这里已经把当前用例给分片了

                for c in range(len(split_Cases)):
                    result = globals()[split_Cases[c]].Main(devices)
                    suite.addTests(result)
    unittest_Report = BeautifulReport(suite)
    # 获取设备名称
    devices_name = os.popen(f"adb -s {devices} shell getprop ro.product.name").read()
    nowtime=time.strftime("%H-%M-%S")
    report_Name = devices_name.split()[0] + "_" + str(nowtime)
    unittest_Report.report(filename=report_Name, description="龙之谷-东南亚+8版本", report_dir=report_Path)
    # emali.sendemail(report_Name,report_Path) # 项目实战的时候需要打开邮件发送功能