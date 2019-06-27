# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import get_screen_size
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
Androidpoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
def startgame(devices):
    dev = connect_device("android:///" + devices)
    sleep(3)
    poco = UnityPoco(device=dev)
    if os.system(f"adb -s {devices} shell pidof com.tencent.tmgp.dragonnest") == 1:
        print("游戏未启动，开始启动游戏...")
        stop_app('com.tencent.tmgp.dragonnest')
        sleep(1)
        start_app('com.tencent.tmgp.dragonnest')
        sleep(10)
        if Androidpoco("android:id/message").exists():
            Androidpoco("android:id/button1").click()
        sleep(30)
        poco = UnityPoco(device=dev)
        touch([int(get_screen_size._get_screen_size(devices)[0]*0.5),int(get_screen_size._get_screen_size(devices)[1]*0.5)])
        sleep(25)
        if poco("Title").exists():
            poco(text="知道啦").click()
        if poco("Texture").exists():
            poco(text="进入游戏").click()
        if poco(text="进入游戏").exists():
            poco(text="进入游戏").click()
            print("点击进入游戏，开始选择角色。。。")
            time.sleep(10)
            if poco("Label").exists():
                poco("Label").click()
                print("角色自动寻找成功，点击开始游戏。。。")
                sleep(15)
            else:
                print("进入游戏失败，请检查。。。。")
        else:
            print("进入游戏失败，请检查。。。。")
    else:
        print("游戏已经启动，无需再次启动...")
    if poco("Pause").exists():
        poco("Pause").click()  # 准备退出副本
        poco("Leave").click()  # 点击退出副本
        sleep(20)
    l_close = poco(texture="l_close_00")
    Close = poco("Close")
    for x in range(4):
        time.sleep(3)
        if l_close.exists() and Close.exists():
            time.sleep(1.5)
            l_close.click()
        elif poco("RecruitPublishView(Clone)").offspring("Close").exists():
            time.sleep(1.5)
            poco("RecruitPublishView(Clone)").offspring("Close").click()
        elif Close.exists():
            time.sleep(1.5)
            Close.click()
        elif poco("Btn").exists():
            if poco("Btn").get_position()[1] < 1 and poco("Btn").get_position()[1] > 0:
                if poco("Btn").get_position()[0] < 1 and poco("Btn").get_position()[0] > 0:
                    time.sleep(1.5)
                    poco("Btn").click()
        else:
            break
    return None