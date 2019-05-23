# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import get_screen_size

def startgame(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if os.system(f"adb -s {devices} shell pidof com.playfungame.ggplay.lzgsea") == 1:
        print("游戏未启动，开始启动游戏...")
        stop_app('com.playfungame.ggplay.lzgsea')
        sleep(1)
        start_app('com.playfungame.ggplay.lzgsea')
        sleep(35)
        poco = UnityPoco(device=dev)
        touch([int(get_screen_size._get_screen_size(devices)[0]*0.5),int(get_screen_size._get_screen_size(devices)[1]*0.5)])
        sleep(20)
        if poco(text="进入游戏").exists():
            poco(text="进入游戏").click()
            print("点击进入游戏，开始选择角色。。。")
            sleep(10)
            if poco("Label").exists():
                poco("Label").click()
                print("角色自动寻则成功，点击开始游戏。。。")
                sleep(15)
            else:
                print("进入游戏失败，请检查。。。。")
        else:
            print("进入游戏失败，请检查。。。。")
    else:
        print("游戏已经启动，无需再次启动...")
    for x in range(10):
        l_close = poco(texture="l_close_00")
        Close = poco("Close")
        if l_close.exists() and Close.exists():
            poco(texture="l_close_00").click()
        elif Close.exists():
            Close.click()
        else:
            break
    return None
devices = "127.0.0.1:62001"
startgame(devices)