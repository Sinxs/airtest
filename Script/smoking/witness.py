"""
观战模块
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from multi_processframe.Tools import printcolor,adb_connect,screenshot


def witness(devices):
    poco = adb_connect.device(devices)
    if poco("SysG_Live").exists():
        poco("SysG_Live").click()
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("SpectateDlg(Clone)").offspring("Name").exists():
            for Label in freeze_poco("SpectateDlg(Clone)").offspring("SpectateFrame").offspring("Bg").offspring("TextLabel"):
                Label.click()  # 点击观战的多项子页签
            freeze_poco("Refresh").click()  # 点击刷新按钮
            freeze_poco("1").click()  # 点击我的记录
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if freeze_poco("Watch").exists() and freeze_poco("Commend").exists():
                pass
            poco("Text").click()  # 点击观战设置
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if freeze_poco("BtnDeny").exists() and freeze_poco("BtnAllow").exists() and freeze_poco("Ok").exists():
                freeze_poco("SpectateDlg(Clone)").offspring("BtnDeny").child("BtnHigh").click()  # 点击不允许被观战
                printcolor.printgreen("点击不允许被观战")
                screenshot.get_screen_shot(time.time(), devices, "点击不允许被观战")
                freeze_poco("SpectateDlg(Clone)").offspring("BtnAllow").child("BtnHigh").click()  # 点击允许被观战
                printcolor.printgreen("点击允许被观战")
                sleep(0.5)
                screenshot.get_screen_shot(time.time(), devices, "点击不允许被观战")
                return poco("Label").get_text()  # 保存设置
        else:
            printcolor.printred("没有进入观战界面，请检查。。。")
            screenshot.get_screen_shot(time.time(), devices, "没有进入观战界面")
    else:
        printcolor.printred("主界面没有有观战按钮，请检查。。。")
        screenshot.get_screen_shot(time.time(), devices, "主界面没有有观战按钮")
