"""
背包
"""
# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from multi_processframe.ProjectTools.common import *
from airtest.core.api import *


def bag_item(start, devices):
    poco = deviceconnect(devices)
    check_menu("SysAItem", poco) # 进入角色
    if poco("XSys_Bag_Item").exists(): # 进入背包
        poco("XSys_Bag_Item").click()
        with poco.freeze() as freeze_poco:
            if freeze_poco(texture="l_zl").exists() and \
                    freeze_poco("PowerPoint").exists() and \
                    poco("TabsFrame").exists() and \
                    freeze_poco("DragObj").exists() and \
                    freeze_poco("add").exists() and \
                    freeze_poco("TabList").exists() and \
                    freeze_poco("BagNum").exists():
                printgreen("战力，背包分类，背包扩展UI元素显示正常")
            else:
                printred("背包界面UI元素显示异常，详情见截图")
                get_screen_shot(start, time.time(), devices, "背包界面UI元素显示异常")
            try:
                with poco.freeze() as freeze_poco:
                    countbegin = int(freeze_poco("BagNum").get_text().split("/", 1)[1])
                    for name in poco("TabsFrame").child():
                        freeze_poco("ItemNewDlg(Clone)").offspring(name.get_name()).click()
                    freeze_poco("TabList").child("Prof").child("P").click()
                    item_Len = poco("Grid").child()
                    if len(item_Len) == 8:
                        printgreen("背包可选项是8条")
                    else:
                        printred("背包条目不是8条，条目异常！！！")
                    freeze_poco("TabList").child("Prof").child("P").click()  # 收回列表栏
                    freeze_poco("add").click()  # 点击增加背包按钮
                    number = int(poco("GreyModalDlg(Clone)").offspring("Bg").child("Label").get_text()[4:7].split("个")[0]) # 获取需要几个背包扩充券
                    poco("OK").click()
                    if poco("ListPanel").exists():
                        poco("ListPanel").click()
                        for i in range(number-1):
                            poco("BuycardFrame").offspring("Add").click()
                        poco("OK").click()
                        poco("Close").click()
                        freeze_poco("add").click()
                        poco("OK").click()
                    if poco("ListPanel").exists():
                        poco(texture="l_close_00").click()
                        printred("背包扩充券与要求不符")
                        printred("背包扩充失败")
                    else:
                        countend = int(poco("BagNum").get_text().split("/", 1)[1])
                        if (countend - countbegin) == 5:
                            printgreen("背包扩充成功")
                        else:
                            printred("使用背包扩充券后，背包扩充失败，请检查背包扩充问题！！！")
                printgreen("背包按钮点击正常")
            except Exception as e:
                printred("背包按钮点击异常")
                printred(e)
                get_screen_shot(start, time.time(), devices, "背包按钮点击异常")
    else:
        printred("背包功能暂未开放，请提升等级角色")
        get_screen_shot(start, time.time(), devices, "背包功能暂未开放")
    return poco("XSys_Bag_Item").get_name()   # 返回值poco("Duck").get_name()


def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 1:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco("MenuSwitchBtn").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()


if __name__ == "__main__":
    start = time.localtime()
    bag_item(start, "9b57691d")