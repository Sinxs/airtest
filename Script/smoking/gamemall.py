# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import printcolor

def butpos(butpos,pos1=0.4,pos2=0.81,high=1330,low=930,lows=482):
    """
把不在屏幕内部的控件滑动到屏幕内，使之可被操作
:param butpos: 控件的坐标值
:param pos1: 希望控件所在屏幕上的最低限
:param pos2: 希望控件所在屏幕上的最上限
:param high: 固定坐标
:param low: 滑动起始或终点位置
:param lows: 滑动起始或终点位置
:return:
    """
    for i in range(20):
        but = butpos.get_position()
        if but[1] < pos1:
            swipe([high, lows], [high, low], 5)
        elif but[1] > pos2:
            swipe([high, low], [high, lows], 5)
        else:
            break


def gamemall(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Mallbutlist = ["XSys_GameMall_Diamond", "XSys_GameMall_Dragon", "XSys_GameMall_CRYSTAL", "XSys_Mall", "XSys_GameMall_Pay"]
    if poco("SysAGameMall").exists():
        poco("SysAGameMall").click()
    else:
        printcolor.printred("主界面找不到商城按钮，请检查")
    for but in Mallbutlist:
        if poco(but).exists():
            printcolor.printgreen("开始点击商城内 "+poco("GameMall(Clone)").offspring(but).offspring("SelectedTextLabel").get_text()+" 子页签")
            poco(but).click()
            for item in range(len(poco("TabsFrame").child())):
                item1 = "item" + str(item)
                if poco("GameMall(Clone)").offspring("TabsFrame").child(item1).exists():
                    if poco("GameMall(Clone)").offspring("TabsFrame").child(item1).get_position()[1] > 0:
                        if poco("GameMall(Clone)").offspring("TabsFrame").child(item1).offspring("TextLabel").exists():
                            printcolor.printgreen("点击 "+poco("GameMall(Clone)").offspring("TabsFrame").child(item1).offspring("TextLabel").get_text()+" 页签")
                            poco("GameMall(Clone)").offspring("TabsFrame").child(item1).click()
                            if poco("ailin").exists():
                                printcolor.printgreen("---------->判断 "+poco("GameMall(Clone)").offspring("TabsFrame").child(item1).offspring("TextLabel").get_text() + " 很穷，没有商品...")
                            elif poco("GameMall(Clone)").offspring("item0").exists():
                                printcolor.printgreen("---------->判断 " + poco("GameMall(Clone)").offspring("TabsFrame").child(item1).offspring("TextLabel").get_text() + " 内容显示正确")
                        else:
                            printcolor.printred("拿到控件，但是却拿不到text，很有可能是程序多写了无用控件.....")
                    else:
                        pass
                else:
                    printcolor.printred("找不到商城子页签，请检查，很有可能是程序多写了无用控件.....")
            if poco("GameMall(Clone)").offspring("ShopFrame").offspring("item0").exists():
                printcolor.printgreen("----------->"+poco("GameMall(Clone)").offspring(but).offspring("SelectedTextLabel").get_text() + " 内子界面显示正确")
            elif poco("GameMall(Clone)").offspring("DiamondFrame").offspring("item0").exists():
                printcolor.printgreen("----------->"+poco("GameMall(Clone)").offspring(but).offspring("SelectedTextLabel").get_text() + " 内子界面显示正确")
        else:
            printcolor.printred("商城界面缺少子页签，请检查")
    return poco("GameMall(Clone)").child("Bg").child("T").get_text()

def mall(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Mallbutlist = ["XSys_GameMall_Diamond", "XSys_GameMall_Dragon", "XSys_GameMall_CRYSTAL", "XSys_Mall",
                   "XSys_GameMall_Pay"]
    if poco("SysAGameMall").exists():
        poco("SysAGameMall").click()
        if poco("XSys_Mall").exists():
            poco("XSys_Mall").click()
        else:
            printcolor.printred("商城界面找不到商店页签，请检查")
    else:
        printcolor.printred("主界面找不到商城按钮，请检查")
    for item in range(len(poco("Grid").child())):
        item1 = "item"+str(item)
        if poco("GameMall(Clone)").offspring("ShopFrame").offspring(item1).exists():
            printcolor.printgreen("点击-->>"+poco("GameMall(Clone)").offspring("ShopFrame").offspring("item0").offspring("shopname"))
            poco("GameMall(Clone)").offspring("ShopFrame").offspring(item1).click()
            if poco("ShopName").exists():
                poco("MallDlg(Clone)").offspring("TabShopFrame").child("item0").click()
                if poco("MallDlg(Clone)").offspring("Panel").child("item0").exists():
                    printcolor.printgreen(poco("MallDlg(Clone)").offspring("TabShopFrame").child("item0").offspring("TextLabel").get_text()+" 界面显示正常")
                else:
                    printcolor.printred(poco("MallDlg(Clone)").offspring("TabShopFrame").child("item0").offspring("TextLabel").get_text()+" 界面没有商品")

        else:
            printcolor.printred("商店界面缺少子页签，请检查...")





