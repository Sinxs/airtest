# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import printcolor,adb_connect,screenshot

devices = "127.0.0.1:62025"
def fashion(devices):
    poco = adb_connect.device(devices)
    if poco("SysAItem").get_position()[1] > 1:
        poco(texture="halln_4").click()
    else:
        printcolor.printgreen("当前界面就有角色按钮")
    poco("SysAItem").click()
    if poco("XSys_Fashion").exists():  # 时装界面
        poco("XSys_Fashion").click()
        if poco("ItemNewDlg(Clone)").offspring("Frame").offspring("T").exists():
            printcolor.printgreen("进入时装界面成功...")
    else:
        printcolor.printred("没有找到时装按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "没有找到时装按钮")
    if poco("UIRoot(Clone)").offspring("Title").exists():  # 时装合成界面
        poco("UIRoot(Clone)").offspring("Title").click()
        fashionlist=["S","A","B"]
        for i in fashionlist:
            if poco("UIRoot(Clone)").offspring("FashionCompoundDlg").offspring(f"Level_{i}").child("UnSelectLab").exists():
                printcolor.printgreen("检查 "+poco("UIRoot(Clone)").offspring("FashionCompoundDlg").offspring(f"Level_{i}").child("UnSelectLab")+"存在")
        printcolor.printgreen("进入 "+poco("UIRoot(Clone)").offspring("Title").get_text()+"界面成功")



    else:
        printcolor.printred("没有弹出时装合成界面，请检查。。。")
        screenshot.get_screen_shot(time.time(), devices, "没有弹出时装合成界面")



