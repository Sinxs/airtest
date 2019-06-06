# -*- encoding=utf8 -*-
__author__ = "Lee.li"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import screenshot, printcolor


def horse(devices):
    """
    1.进入主界面
    2.点击坐骑按钮
    3.依次点击坐骑图标，查看坐骑模型是否正常
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    check_menu("SysEHorse", poco) # 调用函数查看主界面坐骑按钮是否可点击
    poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
    petgrid = poco("Grid").child() # 获取目前所有坐骑数量
    swipe((486, 170), (486, 889), 4)
    swipe((486, 170), (486, 889), 4)
    swipe((486, 170), (486, 889), 4)
    for i in range(len(petgrid)):
        if i == 22 or i == 42 or i ==62:
            swipe((486,889),(486,170),6)
            time.sleep(2)
        item = "item" + str(i)
        time.sleep(2)
        poco("Grid").offspring(item).click() # 点击坐骑icon
        if poco("Btnhave").exists() or poco("BtnMount").exists(): #判断坐骑打开是否正常是否存在
            petname = poco("PetName").offspring("Name").get_text() # 获得当前坐骑的名称
            printcolor.printgreen(f"{petname}坐骑查看正常",end=",")
            if poco("Btnhave").exists():
                poco("Btnhave").click()
                name = poco("ItemToolTipDlg(Clone)").child("Bg").offspring("TopFrame").child("Name").get_text()
                printcolor.printgreen(f"{name}获取界面打开正常")
                touch([1140,540],times=2)
            else:
                if poco("BtnMount").exists():
                    print("坐骑已经获得，没有获取途径")
                else:
                    printcolor.printred("没有相关坐骑信息，请查具体查看该坐骑！")
        else:
            printcolor.printred("没有获取到该坐骑相关信息")
            # screenshot.get_screen_shot(time.time(), devices, "没有拿到这个坐骑的模型")
        poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
        time.sleep(1)
    return poco("Btnhave").get_name() # 返回值

def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 1:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco(texture="switch").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()

# devices = "127.0.0.1:62001"
# horse(devices)