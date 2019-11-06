"""
羁绊模块-
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from airtest.core.api import *
from multi_processframe.ProjectTools import common
from poco.exceptions import PocoNoSuchNodeException


def fetters(start, devices):
    poco = common.deviceconnect(devices)
    if poco("SysE_NPCFavor").exists():  # 龙魂按钮存在
        if poco("SysE_NPCFavor").get_position()[0] > 1:  # 界面有龙魂按钮
            poco(texture="halln_4").click()
            poco("SysE_NPCFavor").click()
        else:
            poco("SysE_NPCFavor").click()
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("BookBg").exists() and \
            freeze_poco("TabTpl0").exists() and \
            freeze_poco("TabTpl2").exists() and \
            freeze_poco("TabTpl1").exists():
        # 点击好感度
        for TabTp in freeze_poco("Tabs").offspring("Bg"):
            TabTp.click()
            freeze_poco = poco.freeze()  # TODO：定义冻结poco
            try:
                if freeze_poco("WrapContent").offspring("NpcName").exists():
                    for Npcname in freeze_poco("WrapContent").offspring("NpcName"):
                        common.printgreen(f"检查点 {Npcname.get_text()} 显示正确")
                if freeze_poco("WrapContent").offspring("GroupName").exists():
                    for Npcname in freeze_poco("WrapContent").offspring("GroupName"):
                        common.printgreen(f"检查点 {Npcname.get_text()} 显示正确")
            except PocoNoSuchNodeException:
                pass
    else:
        common.printred("羁绊界面控件缺失，请检查")
        common.get_screen_shot(start, time.time(), devices, "羁绊界面控件缺失")
    return poco(texture="l_tip_00").child("T").get_text()  # 羁绊



if __name__ == "__main__":
    start = time.localtime()
    fetters(start, "e37c0280")