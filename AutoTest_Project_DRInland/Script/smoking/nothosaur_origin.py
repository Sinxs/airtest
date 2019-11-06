"""
幻龙起源
"""
# -*- encoding=utf8 -*-
__author__ = "sinwu"
from multi_processframe.ProjectTools.common import *
from airtest.core.api import *


def nothosaur_origin(start, devices):
    poco = deviceconnect(devices)
    if poco("SysFuWenL").exists():
        poco("SysFuWenL").click()
        # todo:定义冻结poco
        with poco.freeze() as freeze_poco:
            if freeze_poco("NestName") and \
                freeze_poco("BtnHotfix") and \
                freeze_poco(texture="l_button_00") and \
                freeze_poco("ItemList").child("item0") and \
                    freeze_poco("ItemList").child("item1").exists():
                for item in freeze_poco("Panel").offspring("BgNormal"):
                    printgreen("开始进入" + poco("NestName").get_text() + " 界面，开始进行控件点击测试")
                    item.click()
                    with poco.freeze() as freeze_poco:
                        for icon in freeze_poco("ItemList").offspring("Icon").child("Icon"):
                            icon.click()
                            icon.click()
                        if poco("ItemToolTipDlg(Clone)").child("Bg").exists():
                            icon.click()
                        # 打开通官榜
                        poco("RankBtn").click()
                        if poco("Tittle").exists():
                            printgreen("通关榜打开完成")
                            # 关闭通关榜
                            poco(texture="l_close_00").click()
                        else:
                            printred("通关榜打开失败，请检查...")
                            get_screen_shot(start, time.time(), devices, "通关榜打开失败")
                        # 打开首通榜单
                        poco("FirstPassBtn").click()
                        if poco("RedPoint").exists():
                            printgreen("首通榜单打开完成")
                            # 关闭首通榜单
                            poco("BackBtn").click()
                        else:
                            printred("首通榜单打开失败，请检查...")
                            get_screen_shot(start, time.time(), devices, "首通榜单打开失败")
    else:
        printred("主界面没有找到幻龙起源按钮，请检查...")
        get_screen_shot(start, time.time(), devices, "主界面没有找到幻龙起源按钮")
    return poco("NestName").get_text()  # 噩梦之境-巅峰

if __name__ == "__main__":
    start = time.localtime()
    nothosaur_origin(start, "e37c0280")