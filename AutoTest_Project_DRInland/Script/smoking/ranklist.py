"""
排行榜模块自动化脚本
《脚本环境》

"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from multi_processframe.ProjectTools.common import *


def ranklist(start, devices):
    poco = deviceconnect(devices)
    if poco("SysC_Rank").exists():  # 角色按钮存在
        if poco("SysC_Rank").get_position()[0] > 1:  # 界面有角色按钮
            poco(texture="halln_4").click()
            poco("SysC_Rank").click()
        else:
            poco("SysC_Rank").click()
        if poco("TabList").exists():
            for item in range(len(poco("Table").child())):
                Rank = [6, 9, 11, 13, 16]
                Rank = str(Rank[item])
                freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                A = freeze_poco("RankDlg(Clone)").offspring("TabList").offspring(str(item+1)).child("Bg").get_position()[1]
                B = (freeze_poco("RankDlg(Clone)").offspring("TabList").offspring(str(item+1)).offspring(Rank)
                    .offspring("SelectedLabel").get_position()[1])
                if B - A < 0.05:
                    poco("RankDlg(Clone)").offspring("TabList").offspring(str(item+1)).child("Bg").click()  # 点击PVP排行榜
                freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                for item1 in freeze_poco("RankDlg(Clone)").offspring("TabList").offspring(str(item+1))\
                        .child("ChildList").offspring("Label"):
                    sleep(0.5)
                    item1.click()
                poco("RankDlg(Clone)").offspring("TabList").offspring(str(item+1)).child("Bg").click()  # 点击PVP排行榜,恢复原状
        else:
            printgreen("主界面没有排行榜按钮，请检查...")
            get_screen_shot(start, time.time(), devices, "主界面没有排行榜按钮")
    return poco("RankDlg(Clone)").offspring("TabList").offspring("5").child("Label").get_text()  # 公会排行

if __name__ == "__main__":
    start = time.localtime()
    ranklist(start, "e37c0280")