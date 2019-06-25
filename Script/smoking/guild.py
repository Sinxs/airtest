# -*- encoding=utf8 -*-
__author__ = "Sinwu"

# from airtest.core.api import *
# from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import printcolor,adb_connect
import random


def guild(devices):
    poco = adb_connect.device(devices)
    guildbutlist = ["BtnSignIn", "BtnGz", "BtnSkill", "BtnRed", "Donation", "BtnMall", "BtnJoker", "Btnfish",
                    "BtnBuild", "BtnConsider", "GuildTreasureIcon"]
    if poco("SysCGuild").exists():
        poco("SysCGuild").click()  # 点击主界面公会按钮
        if poco("Create").exists():  # 创建公会
            poco("Create").click()
            if poco("GuildListDlg(Clone)").offspring("CreateMenu").child("T")[0].exists():
                poco("NameInput").set_text(f"{random.randint(100000,99999999)}")  # 输入公会名称
                poco("Highlight").click()  # 点击创建公会
        printcolor.printgreen("进入" + poco(texture="tybg_h2Split").child("T").get_text())
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
