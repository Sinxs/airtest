# -*- encoding=utf8 -*-
__author__ = "Lee.li"
"""
命名规则：
1.模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)
2.类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
3.函数名一律小写，如有多个单词，用下划线隔开，私有函数在函数前加一个下划线_
4.变量名首字母尽量小写, 如有多个单词，用下划线隔开，后续字母大写
5.常量采用全大写，如有多个单词，使用下划线隔开
"""

import inspect
import queue
import threading
from multi_processframe.ProjectTools import common
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android.adb import ADB
from airtest.utils.apkparser import APK

index_print = print
adb = ADB().adb_path  # 获取内置adb路径
queue = queue.Queue()  # queue线程通讯


def print(*args, **kwargs):
    index_print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)


class AndroidTools:

    def __init__(self, momentDevices=""):

        self._parentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # 获取当前文件上层路径
        self._rootPath = os.path.dirname(os.path.abspath(self._parentPath))  # 获取当前目录根目录
        self._configPath = self._rootPath + '\\config.ini'  # 获取config.ini的路径
        self._testCase = common.get_value(self._configPath, 'testCase')  # 获取测试列表
        self._email = common.get_value(self._configPath, 'email')[0]  # 获取邮箱
        self._packageName = common.get_value(self._configPath, 'packageName')[0]  # 获取安装包名称
        self._packagePath = common.get_value(self._configPath, 'packagePath')[0]  # 获取安装包路径
        self._devicesList = common.get_value(self._configPath, 'devicesList')  # 获取配置设备列表
        self._installApk = common.get_value(self._configPath, 'installApk')[0]  # 获取安装测试包开关 1 为打开 0 为关闭
        self._testType = common.get_value(self._configPath, 'testType')[0]  # 获取测试类型开关 1 兼容 0 为分布
        self._performanceType = common.get_value(self._configPath, 'performanceType')[0]  # 获取性能测试开关 1 为打开 0 为关闭
        self._storage_by_exce = common.get_value(self._configPath, "storage_by_exce")[0]  # 获取性能报告方式 1 为excle 0 为json
        self._username = common.get_value(self._configPath, 'username')  # 获取账号
        self._password = common.get_value(self._configPath, 'password')[0]  # 获取密码
        self._server = common.get_value(self._configPath, 'server')[0]  # 获取server
        if self._server == "1server":
            self._server = "日补丁qq android一服"
        elif self._server == "2server":
            self._server = "日补丁qq android二服"
        self._momentDevices = momentDevices  # 获取连接的设备
        if ':' in self._momentDevices:
            self._devicesName = self._momentDevices.split(':')[1]
        else:
            self._devicesName = self._momentDevices

        self._activityName = common.get_value(self._configPath, 'activityName')[0]  # 获取测试包的界面活动名
        if self._activityName == '':
            self._activityName = APK(self.get_apkpath()).activities[0]  # 如果活动包名没有填，就通过APK的activities方法，用包的路径获取活动名


    def get_server(self):
        """
        获取config中的账号名称
        :return:
        """
        return self._server


    def get_password(self):
        """
        获取config中的账号名称
        :return:
        """
        return self._password

    def get_username(self):
        """
        获取config中的账号名称
        :return:
        """
        return self._username

    def get_rootpath(self):
        """
        获取当前路径的根目录绝对路径
        :return:
        """
        return self._rootPath

    def get_configpath(self):
        """
        获取config路径
        :return:
        """
        return self._configPath

    def get_testcase(self):
        """
        获取需要测试的测试用例
        :return:
        """
        return self._testCase

    def get_email(self):
        """
        获取需要测试的测试用例
        :return:
        """
        return self._email

    def get_packagename(self):
        """
        获得config配置中的包名
        :return:
        """
        return self._packageName

    def get_apkpath(self):
        """
        获取apk的本地路径
        :return:
        """
        return self._packagePath

    def get_deviceslist(self):
        """
        获得config配置中的设备列表
        :return:
        """
        return self._devicesList

    def get_installapk(self):
        """
        获取是否需要安装开关
        :return:
        """
        return self._installApk

    def get_testtype(self):
        """
        获取测试类型开关 1 兼容 0 为分布
        :return:
        """
        return self._testType

    def get_performancetype(self):
        """
        获取性能测试开关 1 为打开 0 为关闭
        :return:
        """
        return self._performanceType

    def get_momentdevices(self):
        """
        获取当前设备
        :return:
        """
        return self._momentDevices

    def get_devicesname(self):
        """
        获取当前设备的ID
        :return:
        """
        return self._devicesName

    def get_activityname(self):
        """
        获得config配置中的Activity类名
        :return:
        """
        return self._activityName

    def get_storage_by_excel(self):
        """
        获得config配置中的excel配置 1 使用exlce 0 使用json
        :return:
        """
        return self._storage_by_exce

    def get_workdevices(self):
        """
        实时读取连接的设备
        :return:
        """
        deviceslist = []
        for devices in os.popen(adb + " devices"):
            if "\t" in devices:
                if devices.find("emulator") < 0:
                    if devices.split("\t")[1] == "deviceconnect\n":
                        deviceslist.append(devices.split("\t")[0])
        return deviceslist

    def thread_installapk(self):
        """
        采用多线程进行安装包操作
        :return:
        """
        installapk = self.get_installapk()
        if installapk == 'False':
            return 'Skip'
        device = self.get_momentdevices()
        try:
            installthread = threading.Thread(target=self.install, args=(self,))
            installthread.start()
            installresult = queue.get()
            authorization = threading.Thread(target=self.authorization, args=(self,))
            authorization.start()
            installthread.join()
            authorization.join()
            if installresult == "Install Success":
                return "Success"
            else:
                return "Fail"
        except Exception as e:
            print(e)
        pass

    def install(self):
        """
        实现测试包安装
        :return:
        """
        devices = self.get_momentdevices()
        apkpath = self.get_apkpath()
        packname = self.get_packagename()
        installapk = self.get_installapk()
        if installapk == 'False':
            return 'Skip'
        try:
            if self.check_install():
                uninstallcommand = adb + " -s " + str(devices) + " uninstall " + packname
                print(f"正在卸载{devices}上的游戏.................")
                os.popen(uninstallcommand)
            time.sleep(3)
            installcommand = adb + " -s " + str(devices) + " install -r " + apkpath
            print(f"正在给{devices}安装游戏.................")
            os.popen(installcommand)
            time.sleep(150)
            if self.check_install():
                print(f'{devices}上安装成功')
                return "Success"
            else:
                print(f'{devices}上安装失败')
                return "Fail"
        except Exception as e:
            print(f'{devices}上安装异常，{e}')
            return "Fail"

    # def install(self):
    #     """
    #     实现测试包安装
    #     :return:
    #     """
    #     devices = self.get_momentdevices()
    #     apkpath = self.get_apkpath()
    #     packname = self.get_packagename()
    #     installapk = self.get_installapk()
    #     if installapk == 'False':
    #         return 'Skip'
    #     try:
    #         if self.check_install():
    #             uninstallcommand = adb + " -s " + str(devices) + " uninstall " + packname
    #             print(f"正在卸载{devices}上的游戏.................")
    #             os.popen(uninstallcommand)
    #         time.sleep(7)
    #         installcommand = adb + " -s " + str(devices) + " install -r " + apkpath
    #         print(f"正在给{devices}安装游戏.................")
    #         os.popen(installcommand)
    #         time.sleep(15)
    #         if self.check_install():
    #             print(f'{devices}上安装成功')
    #             queue.put("Install Success")
    #             return True
    #         else:
    #             print(f'{devices}上安装失败')
    #             queue.put("Install Fail")
    #             return False
    #     except Exception as e:
    #         print(f'{devices}上安装异常，{e}')
    #         queue.put("Install Fail")

    def check_install(self):
        """
        检查设备否安装测试包
        :return:
        """
        devices = self.get_momentdevices()
        testpackage = self.get_packagename()
        command = adb + f" -s {devices} shell pm list packages"
        print(command)
        temp = os.popen(command)
        for packagename in temp:
            if testpackage in packagename and testpackage != '':
                print(f"设备{devices}已经安装了游戏")
                return True
        print(f"设备{devices}没有安装{testpackage}")
        return False

    def authorization(self):
        """
        安卓手机权限点击
        TODO 此方法暂未完成，后续需要根据设备型号来编写授权操作
        :return:
        """
        devices = self.get_momentdevices()
        pocoandroid = AndroidUiautomationPoco(device=devices, use_airtest_input=True, screenshot_each_action=False)
        times = 5
        if devices == "127.0.0.1:62001":
            count = 0
            # 找n次或找到对象以后跳出，否则等5秒重试。
            while True:
                print(devices, "安装点击，循环第", count, "次")
                if count >= times:
                    break
                if pocoandroid("vivo:id/vivo_adb_install_ok_button").exists():
                    pocoandroid("vivo:id/vivo_adb_install_ok_button").click()
                    time.sleep(2)
                    if pocoandroid("android.widget.FrameLayout").offspring("android:id/buttonPanel").offspring(
                            "android:id/button1").exists():
                        pocoandroid("android.widget.FrameLayout").offspring("android:id/buttonPanel").offspring(
                            "android:id/button1").click()
                    break
                else:
                    time.sleep(5)
                count += 1
        elif devices == "127.0.0.1:62025":
            count = 0
            while True:
                print(devices, "安装点击，循环第", count, "次")
                if count >= times:
                    break
                if pocoandroid("com.android.packageinstaller:id/continue_button").exists():
                    pocoandroid("com.android.packageinstaller:id/continue_button").click()
                else:
                    time.sleep(5)
                count += 1

    def get_androidversion(self):
        """
        获取安卓版本号
        :return: 返回安卓大版本号转换为int类型
        """
        command = adb + f' -s {self.get_momentdevices()} shell getprop ro.build.version.release'
        version = os.popen(command).read()[0]
        return int(version)

    def get_allocated_memory(self):
        """
        判断给定设备运行指定apk时的内存占用
        :return:返回内存数据，当程序退出返回N/a
        """
        command = adb + f' -s {self.get_momentdevices()} shell dumpsys meminfo {self.get_packagename()}'
        tempmemory = os.popen(command)
        for line in tempmemory:
            memorylist = line.strip().split(' ')
            if memorylist[0] == 'TOTAL':
                while '' in memorylist:
                    memorylist.remove('')
                packagememory = format(int(memorylist[1]) / 1024, ".2f")
                queue.put(packagememory)
                return packagememory
        queue.put('N/a')
        return 'N/a'

    def get_totalmemory(self):
        """
        设备运行内存总占用
        :return:
        """
        command = adb + f' -s {self.get_momentdevices()} shell dumpsys meminfo'
        tempmemory = os.popen(command)
        totalram = 0
        for line in tempmemory:
            memorylist = line.strip().split(':')
            if memorylist[0] == 'Total RAM':
                if self.get_androidversion() <= 6:
                    totalram = format(int(memorylist[1].split(" ")[1]) / 1024, '.2f')
                else:
                    totalram = format(int(memorylist[1].split("K")[0].replace(',', '')) / 1024, '.2f')
                break
        queue.put(totalram)
        return totalram

    def get_freememory(self):
        """
        设备运行空闲内存
        :return:
        """
        command = adb + f' -s {self.get_momentdevices()} shell dumpsys meminfo'
        tempmemory = os.popen(command)
        freeram = 0
        for line in tempmemory:
            memorylist = line.strip().split(':')
            if memorylist[0] == 'Free RAM':
                if self.get_androidversion() <= 6:
                    freeram = format(int(memorylist[1].split(" ")[1]) / 1024, '.2f')
                else:
                    freeram = format(int(memorylist[1].split("K")[0].replace(',', '')) / 1024, '.2f')
                break
        queue.put(freeram)
        return freeram

    def get_usedmemory(self):
        """
        设备运行总使用内存
        :return:
        """
        command = adb + f' -s {self.get_momentdevices()} shell dumpsys meminfo'
        tempmemory = os.popen(command)
        usedram = 0
        for line in tempmemory:
            memorylist = line.strip().split(':')
            if memorylist[0] == 'Used RAM':
                if self.get_androidversion() <= 6:
                    usedram = format(int(memorylist[1].split(" ")[1]) / 1024, '.2f')
                else:
                    usedram = format(int(memorylist[1].split("K")[0].replace(',', '')) / 1024, '.2f')
                break
        queue.put(usedram)
        return usedram

    def get_memoryinfo(self):
        """
        一次dump获取Total/Free/Used内存
        :return:
        """
        command = adb + f' -s {self.get_momentdevices()} shell dumpsys meminfo'
        tempmemory = os.popen(command)
        androidversion = self.get_androidversion()
        for line in tempmemory:
            memorylist = line.strip().split(':')
            if memorylist[0] == 'Total RAM':
                if androidversion <= 6:
                    totalram = format(int(memorylist[1].split(" ")[1]) / 1024, '.2f')
                else:
                    totalram = format(int(memorylist[1].split("K")[0].replace(',', '')) / 1024, '.2f')
            elif memorylist[0] == 'Free RAM':
                if androidversion <= 6:
                    freeram = format(int(memorylist[1].split(" ")[1]) / 1024, '.2f')
                else:
                    freeram = format(int(memorylist[1].split("K")[0].replace(',', '')) / 1024, '.2f')
            elif memorylist[0] == 'Used RAM':
                if androidversion <= 6:
                    usedram = format(int(memorylist[1].split(" ")[1]) / 1024, '.2f')
                else:
                    usedram = format(int(memorylist[1].split("K")[0].replace(',', '')) / 1024, '.2f')
        queue.put(totalram, freeram, usedram)
        return totalram, freeram, usedram

    def get_totalcpu(self):
        """
        CPU总占用，os8以上CPU不一定是100%，
        :return:
        """
        command = adb + f' -s {self.get_momentdevices()} shell top -n 1'
        tempcpu = os.popen(command)
        totalcpu = ''
        maxcpu = ''
        for line in tempcpu:
            temp = line.strip().split(' ')
            while '' in temp:
                temp.remove('')
            if len(temp) > 8:
                if '%cpu' in temp[0]:
                    maxcpu = temp[0]
                    totalcpu = f"{int(temp[0].replace('%cpu', '')) - int(temp[4].replace('%idle', ''))}%"
                    break
        queue.put(totalcpu, maxcpu)
        return totalcpu, maxcpu

    def get_allocated_cpu(self):
        """
        获取运行的测试包占用的cpu
        :return:
        """
        packname = self.get_packagename()[0:15]
        command = adb + f' -s {self.get_momentdevices()} shell top -n 1 |findstr {packname}'
        tempcpu = os.popen(command).read()
        cpu = ''
        if tempcpu == '':
            queue.put('N/a')
            return 'N/a'
        else:
            tempcpu = tempcpu.split(' ')
            while '' in tempcpu:
                tempcpu.remove('')
            if tempcpu.count(f'{packname}') == 2:
                tempcpu = tempcpu[(tempcpu.index(f'{packname}\n')) + 1:]
                cpu = f'{tempcpu[8]}%'
            else:
                cpu = f'{tempcpu[8]}%'
            queue.put(cpu)
            return cpu

    def get_fps(self):
        device = self.get_momentdevices()
        package = self.get_packagename()
        activity = self.get_activityname()
        androidversion = self.get_androidversion()
        command = ""
        if androidversion < 7:
            command = adb + " -s {} shell dumpsys SurfaceFlinger --latency 'SurfaceView'".format(device)
        elif androidversion == 7:
            command = adb + " -s {} shell \"dumpsys SurfaceFlinger --latency 'SurfaceView - {}/{}'\"".format(device,
                                                                                                             package,
                                                                                                             activity)
        elif androidversion > 7:
            command = adb + " -s {} shell \"dumpsys SurfaceFlinger --latency 'SurfaceView - {}/{}#0'\"".format(device,
                                                                                                               package,
                                                                                                               activity)
        tempdata = os.popen(command)
        if not tempdata:
            print("nothing")
            return (None, None)
        timestamps = []
        nanoseconds_per_second = 1e9  # 定义纳秒
        refresh_period = 16666666 / nanoseconds_per_second  # 定义刷新间隔
        pending_fence_timestamp = (1 << 63) - 1  # 定义挂起时间戳
        for line in tempdata:
            temp = line.strip().split("\t")
            if len(temp) != 3:  # 剔除非数据列
                continue
            timestamp = float(temp[1])  # 取中间一列数据
            if timestamp == pending_fence_timestamp:  # 当时间戳等于挂起时间戳时，舍弃
                continue
            timestamp /= nanoseconds_per_second
            if timestamp != 0:  # 安卓7的adbdump提供255行数据，127行0以及128行真实数据，所以需要将0行剔除
                timestamps.append(timestamp)
        frame_count = len(timestamps)  # 获得总帧数
        frame_lengths, normalized_frame_lengths = self.GetNormalizedDeltas(timestamps, refresh_period,
                                                                           0.5)  # 获取帧列表总长、规范化帧列表总长
        if len(frame_lengths) < frame_count - 1:
            print('Skipping frame lengths that are too short.')
        frame_count = len(frame_lengths) + 1
        # 数据不足时，返回None
        if not refresh_period or not len(timestamps) >= 3 or len(frame_lengths) == 0:
            print("未收集到有效数据")
            return "N/a"
        # 总秒数为时间戳序列最后一位减第一位
        seconds = timestamps[-1] - timestamps[0]
        fps = int(round((frame_count - 1) / seconds))
        return fps

    def GetNormalizedDeltas(self, data, refresh_period, min_normalized_delta=None):
        deltas = [t2 - t1 for t1, t2 in zip(data, data[1:])]
        if min_normalized_delta != None:
            deltas = filter(lambda d: d / refresh_period >= min_normalized_delta, deltas)
        return (list(deltas), [delta / refresh_period for delta in deltas])


if __name__ == "__main__":
    device = "127.0.0.1:62001"
    common.deviceconnect(device)
    P = AndroidTools(device)
    P.install()
    print(P)  # 启动app
    # p = Performance()
    # p.check_install()
    # device = "127.0.0.1:62001"
    # p = Performance()
    # while 1 == 1:
    #     print(p.get_allocated_cpu(device))
    #     print(p.get_totalcpu(device))
    # p.get_workdevices()
    # p.get_storage_by_excel()
    # print(p.get_workdevices())
    # print(p.get_storage_by_excel())