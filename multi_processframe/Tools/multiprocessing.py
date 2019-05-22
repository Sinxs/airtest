# -*- encoding=utf8 -*-
__author__ = "Lee.li"
import multiprocessing, sys, os
from airtest.core.api import *
from airtest.core.error import *
from poco.exceptions import *
from multi_processframe.Tools import gettimer, analysis, managecase

def  entrance(processNo,devices):
    start_Time = gettimer.get_time()
    print(start_Time,f"进入第《-{processNo}-》进程----{devices}")
    is_Connect = ""
    os.system("adb connect " + devices) # 确保端口号已经打开
    try:
        connect_device("Android:///" + devices)

        time.sleep(1)
        auto_setup(__file__)
        is_Connect = "Pass"
    except Exception as e:
        print(e)
        is_Connect = "Fail"
        print(f"连接设备{devices}失败")
    if is_Connect == "Pass":
        try:
            # startApp.startgame(devices)
            # sleep(1)
            managecase.run_testcase(devices)
            print( devices,"完成测试")
        except Exception as e:
            print(e)
            print(f"初始化游戏失败，{devices}")

def main():
    config_Path = os.path.join(os.getcwd(), "config.ini") # 获取配置路径 D:\AirtestIDE\Case\Common\config.ini
    devices_List = analysis.analysis_config(config_Path, "deviceslist")
    print(gettimer.get_time(), "测试开始")
    try:
        pool = multiprocessing.Pool(processes=len(devices_List))
        print(gettimer.get_time(), "启动进程池")
        processNo = 1 # 设备循环变量
        for i in range(len(devices_List)):
            pool.apply_async(entrance,(i+1, devices_List[i]))

        pool.close()
        pool.join()
        print(gettimer.get_time(), "进程回收完毕")
        print(gettimer.get_time(), "测试结束")
        # report_Path = os.path.join(os.getcwd(), "Report")
        # os.system(f"start explorer {report_Path}")
    except AirtestError as ae:
        print(gettimer.get_time(), "Airtest发生错误" + ae)
    except PocoException as pe:
        print(gettimer.get_time(), "Poco发生错误" + pe)
    except Exception as e:
        print(gettimer.get_time(), "发生未知错误" + e)