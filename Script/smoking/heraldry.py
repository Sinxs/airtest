"""
纹章模块
判断纹章模块中的界面元素-点击按钮
"""
from multi_processframe.Tools import printcolor, adb_connect, screenshot
from airtest.core.api import *

def heraldry(devices):
    poco = adb_connect.device(devices)
    if poco("SysAItem").get_position()[0] > 1:
        poco(texture="halln_4").click()
        sleep(1)
    poco("SysAItem").click()  # 点击角色按钮
    if poco("Title").exists():
        printcolor.printgreen("进入角色界面")
        if poco("XSys_Char_Emblem").exists():
            poco("XSys_Char_Emblem").click()  # 点击纹章
            if poco("ItemNewDlg(Clone)").offspring("Items").child("Frame").offspring("T").exists():
                printcolor.printgreen("进入纹章界面，开始测试纹章")

        else:
            printcolor.printred("没有进入角纹章界面，请检查。。")
            screenshot.get_screen_shot(time.time(), devices, "没有进入角色")
    else:
        printcolor.printred("没有进入角色，请检查。。")
        screenshot.get_screen_shot(time.time(), devices, "没有进入角色")




devices = "127.0.0.1:62025"
heraldry(devices)