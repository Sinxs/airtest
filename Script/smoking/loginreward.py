"""
登陆奖励
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from multi_processframe.Tools import printcolor,adb_connect,screenshot

def loginreward(devices):
    poco = adb_connect.device(devices)
    if poco("SysISevenActivity").exists():
        poco("SysISevenActivity").click()
        if poco(texture="SevenReward_Title").exists():
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for WrapItem_ in range(len(freeze_poco("ScrollView").child())):
                WrapItem = "WrapItem_" + str(WrapItem_)
                if freeze_poco(WrapItem).exists() and freeze_poco("Texture").exists():
                    pass
                else:
                    printcolor.printred("登陆奖励缺少元素，请检查。。。")
                    screenshot.get_screen_shot(time.time(), devices, "登陆奖励缺少元素")
            for Label in poco("SevenAwardDlg(Clone)").offspring("GetButton").offspring(text="领 取"):
                Label.click()
                for i in range(10):
                    if poco(text="使用").exists():
                        poco(text="使用").click()
                    else:
                        break
            if not poco("SevenAwardDlg(Clone)").offspring("WrapItem_6").offspring(text="领 取").exists():
                printcolor.printgreen("已经全部领取")
        else:
            printcolor.printred("没有弹出登陆奖励，请检查。。。")
            screenshot.get_screen_shot(time.time(), devices, "主界面没有登陆奖励按钮")
    else:
        printcolor.printred("主界面没有登陆奖励按钮，请检查。。。")
        screenshot.get_screen_shot(time.time(), devices, "主界面没有登陆奖励按钮")
    return poco(texture="SevenReward_Title").get_name()  # Title