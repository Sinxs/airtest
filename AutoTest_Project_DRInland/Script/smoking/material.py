"""
物资筹备模块-
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from airtest.core.api import *
from multi_processframe.ProjectTools import common


def material(start, devices):
    poco = common.deviceconnect(devices)
    if poco("SysGPrepare").exists():
        poco("SysGPrepare").click()
        if poco("UIRoot(Clone)").offspring("DailyDungeonDlg").offspring("SelectedTextLabel").exists():
            common.printgreen("进入物资筹备界面")
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for Desc in freeze_poco("UIRoot(Clone)").offspring("DailyDungeonDlg").offspring("Desc"):
                common.printgreen(f"点击{Desc.get_text()}")
                Desc.click()
                if poco("UIRoot(Clone)").offspring("DailyDungeonDlg").offspring("WrapContent").exists():
                    poco(texture="l_close_00").click()
    else:
        common.printred("主界面没有物资筹备按钮，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "主界面没有物资筹备按钮")
    return poco("UIRoot(Clone)").offspring("DailyDungeonDlg").offspring("TextLabel").get_text()  # 日常攻略


if __name__ == "__main__":
    start = time.localtime()
    material(start, "e37c0280")