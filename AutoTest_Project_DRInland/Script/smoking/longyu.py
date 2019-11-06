# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from multi_processframe.ProjectTools.common import *
from airtest.core.api import *


def item_jade(start, devices):
    poco = deviceconnect(devices)
    check_menu("SysAItem", poco) # 进入角色
    poco("XSys_Item_Jade").click() # 进入龙玉页签
    with poco.freeze() as freeze_poco:
        if freeze_poco("ItemNewDlg(Clone)").offspring("Help").exists() and \
                freeze_poco("JadeShop").exists() and \
                freeze_poco("BtnJadeStreng").exists() and \
                freeze_poco("BtnEqOnekey").exists():
            printgreen("规则按钮，龙玉获取，一键镶嵌按钮检测正常")
        else:
            printred("龙玉界面缺少按钮")
            get_screen_shot(start, time.time(), devices, "龙玉界面缺少按钮")
    if poco("Empty").exists():
        if poco("Empty").child("T").get_text() == "先穿戴装备再来镶嵌龙玉哦": # 判断是不是没有装备
            poco("XSys_Item_Equip").click() # 去穿戴装备
            with poco.freeze() as freeze_poco:
                equipchild = freeze_poco("WrapContent").child()
                for i in equipchild:
                    name = i.get_name()
                    if name[:5] != "empty":
                        equipname = name
                        break
            poco(equipname).click() # 点击装备
            poco("Button1").click() # 穿戴装备
            poco("XSys_Item_Jade").click() # 再次点击龙玉
    else:
        printgreen("龙玉界面穿了装备，直接进行龙玉获取操作")
    poco("BtnJadeStreng").click()
    poco("ItemNewDlg(Clone)").offspring("JadeStrengHandler").offspring("BtnEqOnekey").click()
    printgreen("龙玉强化按钮点击正常")
    poco(texture="l_close_00").click()
    poco("JadeShop").click()
    poco("access212").click()
    printgreen("进入龙玉商店")
    poco("GameMall(Clone)").offspring("item3").offspring("TextLabel").click() # 进入龙玉页签
    for i in range(2):
        poco("OK").click()
    poco("Close").click() # 关闭龙玉商店
    poco("BtnEqOnekey").click() # 一件镶嵌
    if poco("onekeylvup").exists():
        poco("onekeylvup").click() # 一键升级
        printgreen("龙玉升级--一键升级")
        poco("UIRoot(Clone)").offspring("BtnCompose").click() # 确认一键升级
    if poco("Btngroup").exists():
        poco("Btngroup").click()# 龙玉组合
        if poco("UIRoot(Clone)").offspring("JadeGroupPanel").child("Bg").child("Bg").exists():
            printgreen("龙玉组合界面打开成功")
            poco(texture="l_close_00").click() # 关闭龙玉组合界面
        else:
            printred("龙玉组合界面打开失败")
            get_screen_shot(start, time.time(), devices, "龙玉组合界面打开失败")
    else:
        printred("龙玉组合按钮不存在")
        get_screen_shot(start, time.time(), devices, "龙玉组合按钮不存在")
    poco("JadeEquipFrameNew").offspring("Help").click() # 规则按钮
    if poco("CommonHelpTip(Clone)").child("Bg").exists():
        printgreen("龙玉规则界面打开正常")
        poco("Btn").click() # 关闭规则界面
    else:
        printred("龙玉规则界面打开失败")
        get_screen_shot(start, time.time(), devices, "龙玉规则界面打开失败")

    return poco("BtnJadeStreng").get_name()  # 返回值poco("Duck").get_name()


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
    item_jade(start, "9b57691d")