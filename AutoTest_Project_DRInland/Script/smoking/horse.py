# -*- encoding=utf8 -*-
__author__ = "Lee.li"

from multi_processframe.ProjectTools.common import *
from airtest.core.api import *
import random


def horse(start, devices):
    """
    1.进入主界面
    2.点击坐骑按钮
    3.依次点击坐骑图标，查看坐骑模型是否正常
    """

    poco = deviceconnect(devices)
    check_menu("SysEHorse", poco)  # 调用函数查看主界面坐骑按钮是否可点击
    poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
    for x in range(20):  # 判断第一个坐骑是不是在初始位置
        if poco("Grid").child("item0").get_position()[1] < 0.145:
            setswipe(1, (486, 170), (486, 889), devices)
        else:
            break
    for i in range(3):
        if i == 0:
            item = "item" + str(i)
        else:
            item = "item" + str(random.randint(3, 20))
        if i >= 25:
            for i in range(20):
                if poco("Grid").child(item).get_position()[1] > 0.9:
                    setswipe(1, (200, 560), (200, 180), devices)
                elif poco("Grid").child(item).get_position()[1] < 0.12:
                    setswipe(1, (200, 180), (200, 560), devices)
                else:
                    break
        sleep(1)
        poco("Grid").offspring(item).click()  # 点击坐骑icon
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("Btnhave").exists() or freeze_poco("BtnMount").exists(): #判断坐骑打开是否正常是否存在
            petname = freeze_poco("PetName").offspring("Name").get_text() # 获得当前坐骑的名称
            printgreen(f"{petname}坐骑查看正常", end=",")
            try:
                snapshotnumber = freeze_poco("PetMainDlg(Clone)").child("Bg").child("Snapshot").child().get_name()
                if snapshotnumber.isnumeric() == True:
                    printgreen(f"坐骑模型配置存在", end=",")
                else:
                    printred("坐骑模型配置不存在，请详细查看", end=",")
                    get_screen_shot(start, time.time(), devices, "坐骑模型不显示")
            except Exception as e:
                print(e)
                printred("坐骑模型配置不存在，请详细查看", end=",")
                get_screen_shot(start, time.time(), devices, "坐骑模型不显示")

            if freeze_poco("Btnhave").exists():
                poco("Btnhave").click()
                if poco("ItemToolTipDlg(Clone)").child("Bg").offspring("TopFrame").child("Name").exists():
                    printgreen("获取界面打开正常")
                    touch([0.5, 0.4])
                else:
                    printgreen("没有相关坐骑信息，请查具体查看该坐骑！")
                    get_screen_shot(start, time.time(), devices, "没有获取到该坐骑相关信息")
                    touch([0.5, 0.4])
            else:
                if freeze_poco("BtnMount").exists():
                    print("坐骑已经获得，点击坐骑骑乘")
                    freeze_poco("BtnMount").click()
                    sleep(2)
                    if not poco("BtnMount").exists():
                        printgreen("坐骑骑乘成功")
                        check_menu("SysEHorse", poco)  # 调用函数查看主界面坐骑按钮是否可点击
                    else:
                        printgreen("坐骑骑乘失败")
                        get_screen_shot(start, time.time(), devices, "坐骑骑乘失败")
                else:
                    printred("没有相关坐骑信息，请查具体查看该坐骑！")
                    get_screen_shot(start, time.time(), devices, "没有获取到该坐骑相关信息")
        else:
            printred("没有获取到该坐骑相关信息")
            get_screen_shot(start, time.time(), devices, "没有获取到该坐骑相关信息")
        sleep(1)
        poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
        time.sleep(1)
    return poco("BtnkBtn").get_name()  # 返回值


def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 0.82:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco(texture="switch").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()


if __name__ == "__main__":
    start = time.localtime()
    horse(start, "9b57691d")