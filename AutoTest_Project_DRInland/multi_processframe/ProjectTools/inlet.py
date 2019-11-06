# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from multiprocessing import Process, Value
from airtest.core.error import *
from poco.exceptions import *
from multi_processframe.performance import *
from multi_processframe.ProjectTools import managecase
from multi_processframe.ProjectTools.androidtools import AndroidTools as tool
from multi_processframe.ProjectTools import initial


def main():
    """
    多进程用例分配
    根据设备数量创建进程
    :return:
    """
    common.del_progress()
    deviceslist = tool().get_deviceslist()
    performancetype = tool().get_performancetype()
    is_storaged_by_excel = tool().get_storage_by_excel()
    is_storaged_by_excel = True if is_storaged_by_excel == "1" else False
    print("测试开始")
    if deviceslist:
        try:
            print("启动进程池")
            templist = []
            for i in range(len(deviceslist)):
                sleep(1)
                start = time.localtime()
                sample = tool(deviceslist[i])  # 实例化类，循环加入devices
                flag = Value('i', 0)
                if performancetype == 'True':
                    performanceprocess = Process(target=enter_performance, args=(sample, flag, start, is_storaged_by_excel))  # 进行性能测试
                    performanceprocess.start()
                    templist.append(performanceprocess)
                functionprocess = Process(target=enter_processing, args=(i+1, sample, flag, start,))  # 进行功能测试
                functionprocess.start()
                templist.append(functionprocess)
            for stop in templist:
                stop.join()
            print("进程回收完毕")
            print("测试结束")
        except AirtestError as ae:
            print("Airtest发生错误" + traceback.format_exc())
        except PocoException as pe:
            print("Poco发生错误" + traceback.format_exc())
        except Exception as e:
            print("发生未知错误" + traceback.format_exc())
    else:
        print("未找到设备，测试结束")


def enter_processing(processNo, sample, flag, start):
    """
    1.连接设备
    2.根据配置条件是否进行安装包操作
    :param processNo: 进程号
    :param sample: 实例化参数
    :param flag: 进程通讯标识
    :param start: 报告截图唯一标识
    :return:
    """
    devices = sample.get_momentdevices()  # 获取当前连接的设备
    package = sample.get_packagename()
    print(f"进入第《-{processNo}-》进程----{devices}")
    is_connect = ""
    try:
        connect_device("Android:///" + devices)
        time.sleep(2)
        auto_setup(__file__)
        is_connect = "Pass"
        print(f"连接设备{devices}成功")
        stop_app(f"{package}")  # 首次运行的时候杀掉进程重新进入
        installapkflag = ''
        if is_connect == "Pass":
            try:
                if sample.get_installapk() == "True":  # 设备安装，如果是install_Apk=True，就是需要重新安装包
                    print(f"设备{devices}正在重新安装测试包.................")
                    # install_result = sample.thread_installapk()
                    install_result = sample.install()
                    if install_result == "Success":
                        installapkflag = "Success"
                        packname = tool(devices).get_packagename()
                        username = sample.get_username()[processNo - 1]  # 获取游戏账号
                        password = sample.get_password()  # 获取游戏密码
                        server = sample.get_server()  # 获取服务器
                        print(
                            f"进入第《-{processNo}-》进程----{devices},获取账号----{username},获取密码----"
                            f"{password},获取服务器----{server}")
                        initial.firststartgame(username, password, packname, devices, server)
            except Exception as e:
                print(f'{devices}安装失败，结果是{install_result}，{traceback.format_exc(), e}')

            if installapkflag == "Success":
                print(f'{devices}测试包安装成功')
            managecase.run_testcase(sample, start)
            print(devices, "完成测试")
        else:
            print(f"连接设备{devices}失败")
    except Exception as e:
        print(f"连接设备{devices}失败。{traceback.format_exc()}")
    flag.value = 1


if __name__ == "__main__":
    devices = "2d9096f3"
    packname = tool(devices).get_packagename()
    print(packname)