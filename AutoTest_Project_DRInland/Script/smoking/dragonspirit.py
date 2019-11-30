"""
龙魂模块-
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from airtest.core.api import *
from multi_processframe.ProjectTools import common


def dragonspirit(start, devices):
    poco = common.deviceconnect(devices)
    if poco("SysG_DragonSpirit").exists():  # 龙魂按钮存在
        if poco("SysG_DragonSpirit").get_position()[0] > 1:  # 界面有龙魂按钮
            poco(texture="halln_4").click()
            poco("SysG_DragonSpirit").click()
        else:
            poco("SysG_DragonSpirit").click()
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("DragonSpiritDlg(Clone)").offspring("AvatarPanel").child("item0").exists() and \
        freeze_poco("DragonSpiritDlg(Clone)").offspring("AvatarPanel").child("item1").exists():
        for item in poco("AvatarPanel").offspring("HeadIcon"):
            item.click()
            freeze_poco = poco.freeze()  # TODO：定义冻结poco
            # 程序隐藏了5个控件，所以以下只点击5次
            count = 0
            for icon in freeze_poco("DragonSpiritDlg(Clone)").offspring("Panel").offspring("lock"):
                icon.click()
                sleep(0.5)
                icon.click()
                count += 1
                if count >= 5:
                    break
            if poco("DragonSpiritSkillPreView").child("Bg").child("p").exists():
                icon.click()
            # 点击激活按钮
            # poco("ActivationBtn").click()
            if poco(texture="l_frame_00").exists():
                common.printred("没有激活道具。请补充。。")
                poco("ActivationBtn").click()
                break
            if poco("LevelUpBtn").exists():
                common.printgreen("已经激活，开始喂养")
                poco("LevelUpBtn").click()
                if not poco("Title").exists():  # 如果没有弹出就重新点击
                    poco("LevelUpBtn").click()
                if poco("Title").exists():  # 喂养界面
                    if poco("DragonSpiritHandler").offspring("LevelUpBtn").exists():  # 如果有喂养按钮
                        poco("DragonSpiritHandler").offspring("LevelUpBtn").click()  # 点击喂养
                        poco(texture="l_close_00").click()  # 点击关闭
                    elif poco("DirectUpBtn").exists():  # 如果有突破按钮
                        poco("DirectUpBtn").click()  # 点击突破
                        poco(texture="l_close_00").click()  # 点击关闭
                else:
                    common.printred("没有弹出喂养界面，请检查。。。")
                    common.get_screen_shot(start, time.time(), devices, "没有弹出喂养界面")
            if poco("ItemAccessDlg(Clone)").offspring("Title").exists():
                freeze_poco("ActivationBtn").click()
    else:
        common.printred("龙魂界面控件缺失，请检查")
        common.get_screen_shot(start, time.time(), devices, "龙魂界面控件缺失")
    return poco("Total").child("Text").get_text()  # 龙魂总属性


if __name__ == "__main__":
    start = time.localtime()
    dragonspirit(start, "e37c0280")