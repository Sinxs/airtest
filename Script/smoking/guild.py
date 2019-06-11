# -*- encoding=utf8 -*-
__author__ = "Sinwu"

# from airtest.core.api import *
# from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import printcolor,adb_connect


def guild(devices):
    poco = adb_connect.device(devices)
    guildbutlist = ["BtnSignIn", "BtnGz", "BtnSkill", "BtnRed", "Donation", "BtnMall", "BtnJoker", "Btnfish",
                    "BtnBuild", "BtnConsider", "GuildTreasureIcon"]
    if poco("SysCGuild").exists():
        poco("SysCGuild").click()
        printcolor.printgreen("进入"+poco(texture="tybg_h2Split").child("T").get_text())
    for guildbut in guildbutlist:
        if poco(guildbut).exists():
            poco(guildbut).click()
            # todo:判断进入的子页面的元素，并且点击返回---------------------------
            if poco(texture="l_close_00").exists():
                printcolor.printgreen(poco("Label").get_text() + "显示正确+++")
                poco(texture="l_close_00").click()
            elif poco("Close").exists():
                printcolor.printgreen(poco("T").get_text() + ": 显示正确---")
                poco("Close").click()
            else:
                printcolor.printred("没有进入公会子界面，请检查")
                poco(texture="l_close_00").click()
    return poco("BtnEnter").child("T").get_text()
