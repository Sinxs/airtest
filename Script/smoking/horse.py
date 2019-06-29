# -*- encoding=utf8 -*-
__author__ = "Lee.li"

from airtest.core.api import *
from multi_processframe.Tools import screenshot, printcolor, adb_connect


def horse(devices):
    """
    1.进入主界面
    2.点击坐骑按钮
    3.依次点击坐骑图标，查看坐骑模型是否正常
    """
    horselist=[1,]
    poco = adb_connect.device(devices)
    check_menu("SysEHorse", poco) # 调用函数查看主界面坐骑按钮是否可点击
    poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
    petgrid = poco("Grid").child() # 获取目前所有坐骑数量
    for x in range(20):
        if poco("Grid").child("item0").get_position()[1] < 0.145:
            swipe((486, 170), (486, 889))
        else:
            break
    for i in range(len(petgrid)):
        item = "item" + str(i)
        if i >= 25:
            for i in range(20):
                if poco("Grid").child(item).get_position()[1] > 0.9:
                    swipe((200, 560), (200, 180))
                elif poco("Grid").child(item).get_position()[1] < 0.12:
                    swipe((200, 180), (200, 560))
                else:
                    break
        poco("Grid").offspring(item).click()  # 点击坐骑icon
        if poco("Btnhave").exists() or poco("BtnMount").exists(): #判断坐骑打开是否正常是否存在
            petname = poco("PetName").offspring("Name").get_text() # 获得当前坐骑的名称
            printcolor.printgreen(f"{petname}坐骑查看正常",end=",")
            try:
                snapshotnumber = poco("PetMainDlg(Clone)").child("Bg").child("Snapshot").child().get_name()
                if snapshotnumber.isnumeric() == True:
                    if any(snapshotnumber != s for s in horselist):  # 判断snapshotnumber是否在horselist中出现过,如果没有
                            printcolor.printgreen(f"坐骑模型编组存在", end=",")
                            horselist.append(snapshotnumber)
                else:
                    printcolor.printred("坐骑模型编组不存在，请详细查看", end=",")
                    screenshot.get_screen_shot(time.time(), devices, "坐骑模型不显示")
            except Exception as e:
                print(e)
                printcolor.printred("坐骑模型编组不存在，请详细查看", end=",")
                screenshot.get_screen_shot(time.time(), devices, "坐骑模型不显示")

            if poco("Btnhave").exists():
                poco("Btnhave").click()
                if poco("ItemToolTipDlg(Clone)").child("Bg").offspring("TopFrame").child("Name").exists():
                    printcolor.printgreen("获取界面打开正常")
                    touch([1140,540],times=2)
                else:
                    printcolor.printgreen("没有相关坐骑信息，请查具体查看该坐骑！")
                    screenshot.get_screen_shot(time.time(), devices, "没有获取到该坐骑相关信息")
                    touch([1140, 540], times=2)
            else:
                if poco("BtnMount").exists():
                    print("坐骑已经获得，没有获取途径")
                else:
                    printcolor.printred("没有相关坐骑信息，请查具体查看该坐骑！")
                    screenshot.get_screen_shot(time.time(), devices, "没有获取到该坐骑相关信息")
        else:
            printcolor.printred("没有获取到该坐骑相关信息")
            screenshot.get_screen_shot(time.time(), devices, "没有获取到该坐骑相关信息")
        poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
        time.sleep(1)
    return poco("Btnhave").get_name() # 返回值

def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 0.82:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco(texture="switch").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()

devices = "127.0.0.1:62001"
horse(devices)