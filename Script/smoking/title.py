"""
称号模块
检查所有称号
"""
from multi_processframe.Tools import printcolor,adb_connect
from airtest.core.api import *
devices = "127.0.0.1:62025"
def card(devices):
    poco = adb_connect.device(devices)
    if poco("SysAItem").get_position()[0] > 1:
        poco(texture="halln_4").click()
        sleep(1)
    else:
        printcolor.printgreen("当前界面就有角色按钮")
    poco("SysAItem").click()  # 点击角色按钮
    if poco("Title").exists():
        printcolor.printgreen("进入角色界面")

    else:

