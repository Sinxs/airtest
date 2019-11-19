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
            if freeze_poco("RankBtn") and \
                freeze_poco("NestName") and \
                freeze_poco("RankBtn") and \
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
                            if poco("ItemToolTipDlg(Clone)").child("Bg").exists():
                                icon.click()
                        # 打开通官榜
                        poco("RankBtn").click()
                        if not poco("Tittle").exists():
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
                        if not poco("RedPoint").exists():
                            poco("FirstPassBtn").click()
                        if poco("RedPoint").exists():
                            printgreen("首通榜单打开完成")
                            # 关闭首通榜单
                            poco("BackBtn").click()
                        else:
                            printred("首通榜单打开失败，请检查...")
                            get_screen_shot(start, time.time(), devices, "首通榜单打开失败")
            else:
                printred("幻龙起源界面缺少控件元素。请检查。。。")
                get_screen_shot(start, time.time(), devices, "主界面没有找到幻龙起源按钮")
    else:
        printred("主界面没有找到幻龙起源按钮，请检查...")
        get_screen_shot(start, time.time(), devices, "主界面没有找到幻龙起源按钮")
    printgreen("开始测试消弱功能")
    if poco("BtnHotfix").exists():  # 点击消弱
        printred("没有消弱道具，请补充。。。")
        return None
    if poco("Btn").exists():
        A = int(poco("ProgressBar").child("T").get_text().split("/")[0].split("（")[1])
        poco("Btn").click()
        # todo:上面的按钮显示太骚了，有道具和无道具的削弱控件不一致，导致每次进入页面的时候都要进行判断，估计以后会改，
        # todo：以下代码先留着
        # if poco("ItemAccessDlg(Clone)").offspring("Title").exists():
        #     printred("没有消弱道具，请补充。。。")
        #     get_screen_shot(start, time.time(), devices, "没有消弱道具")
        #     poco(texture="l_close_00").click()
        #     return None
        B = int(poco("ProgressBar").child("T").get_text().split("/")[0].split("（")[1])
        if A < B:
            print("消弱成功")
        else:
            printred("消弱未生效，请检查。。")
            get_screen_shot(start, time.time(), devices, "主界面没有找到幻龙起源按钮")
    else:
        printred("消弱按钮不存在，请检查。。")
        get_screen_shot(start, time.time(), devices, "消弱按钮不存在")
    return poco("NestName").get_text()  # 噩梦之境-巅峰


if __name__ == "__main__":
    start = time.localtime()
    nothosaur_origin(start, "9b57691d")