# -*- encoding=utf8 -*-
__author__ = "Lee.li"

import unittest
import math
import shutil
from airtest.core.api import *
from multi_processframe.ProjectTools.common import sendemail, get_script_list
from BeautifulReport import BeautifulReport
from multi_processframe.TestCase import *

index_print = print


def print(*args, **kwargs):
    index_print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)


def run_testcase(sample, start):
    """
    :param sample: 实例化参数
    :param start: 唯一标识
    :return: 没有返回值
    """
    devices = sample.get_momentdevices()
    # 获取设备列表
    devices_list = sample.get_deviceslist()
    # 获取测试类型 True=兼容，False=分布
    testtype = sample.get_testtype()
    # 生成测试报告
    devices_name = os.popen(f"adb -s {devices} shell getprop ro.product.name").read()
    nowtime = f'{time.strftime("%Y-%m-%d-%H-%M-%S", start)}'
    report_Name = devices_name.split()[0] + "_" + str(nowtime)
    # 获取测试报告路径
    report_path = (os.path.abspath(os.path.join(os.getcwd(), f"../platform/Controller/static/Report/{report_Name}")))
    if not os.path.exists(report_path):
        os.makedirs(report_path + '/Screenshot')
        os.makedirs(report_path + '/data')
        os.makedirs(report_path + '/script')
    # 复制文件到报告
    tempjs = (os.path.abspath(os.path.join(os.getcwd(), f"../platform/Controller/static/Report/script/highcharts.js")))
    scriptjs = report_path + '/script'
    shutil.copy(tempjs, scriptjs)
    # 得到config中的所有待测用例
    config_Test_List = sample.get_testcase()
    # 获取testcase下的所有用例
    case_path = os.path.join(os.getcwd(), "TestCase")
    script_list = get_script_list(case_path)
    # 实例化测试套件
    suite = unittest.TestSuite()
    cases = []  # 定义一个空的待测用例列表
    for i in range(len(config_Test_List)):  # 循环遍历
        file_Name = "TC_" + config_Test_List[i]  # 把配置列表中的用例加上tc标志
        if file_Name in script_list:
            if testtype == "True":  # 测试类型，如果是typeTest=1，就是兼容测试，否则就是单分测试
                result = globals()[file_Name].Main(start, devices)
                suite.addTests(result)
            else:
                cases.append(file_Name)
                if i == len(config_Test_List) - 1:  # 当TestCase全部用例循环加载之后

                    for b in range(devices_list.index(devices) + 1):  # 根据设备的数量循环把用例分成若干等分
                        split_cases = cases[math.floor(b / len(devices_list) * len(cases)):math.floor(
                            (b + 1) / len(devices_list) * len(cases))]  # 到这里已经把当前用例给分片了

                    for c in range(len(split_cases)):
                        result = globals()[split_cases[c]].Main(start, devices)
                        suite.addTests(result)
    unittest_Report = BeautifulReport(suite)
    unittest_Report.report(filename=report_Name, description="龙之谷国内版本", report_dir=report_path)
    receivers = sample.get_email()
    if receivers != '':
        sendemail(report_Name, receivers)
