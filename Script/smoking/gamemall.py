"""
商城模块
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import printcolor,adb_connect,screenshot
import random
def butpos(butpos,pos1=0.4,pos2=0.81,high=1330,low=930,lows=482):
    """
把不在屏幕内部的控件滑动到屏幕内，使之可被操作
:param butpos: 控件的坐标值
:param pos1: 希望控件所在屏幕上的最下限
:param pos2: 希望控件所在屏幕上的最上限
:param high: 固定坐标
:param low: 滑动起始或终点位置
:param lows: 滑动起始或终点位置
:return:
    """
    for i in range(30):
        but = butpos.get_position()
        if but[1] < pos1:
            swipe([high, lows], [high, low], 5)
        elif but[1] > pos2:
            swipe([high, low], [high, lows], 5)
        else:
            break


def gamemall(devices):
    poco = adb_connect.device(devices)
    if poco("SysAGameMall").exists():
        poco("SysAGameMall").click()
    else:
        printcolor.printred("主界面找不到商城按钮，请检查")
    Mallbutlist = ["XSys_GameMall_Diamond", "XSys_GameMall_Dragon", "XSys_GameMall_CRYSTAL", "XSys_Mall","XSys_GameMall_Pay"]
    for but in Mallbutlist:
        if poco(but).exists():
            printcolor.printgreen("开始点击商城内 "+poco("GameMall(Clone)").offspring(but).offspring("SelectedTextLabel").get_text()+" 子页签")
            poco(but).click()
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for item in range(len(freeze_poco("TabsFrame").child())):
                item1 = "item" + str(item)
                if freeze_poco("GameMall(Clone)").offspring("TabsFrame").child(item1).exists():
                    if freeze_poco("GameMall(Clone)").offspring("TabsFrame").child(item1).get_position()[1] > 0:
                        if freeze_poco("GameMall(Clone)").offspring("TabsFrame").child(item1).offspring("TextLabel").exists():
                            printcolor.printgreen("点击 "+freeze_poco("GameMall(Clone)").offspring("TabsFrame").child(item1).offspring("TextLabel").get_text()+" 页签")
                            freeze_poco("GameMall(Clone)").offspring("TabsFrame").child(item1).click()
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


def mall(devices):  # 商店功能测试
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("Alphaboard").offspring("SysA_Friends").exists():
        poco("Alphaboard").offspring("SysA_Friends").click()  # 点击社交
        if poco("FriendsDlg(Clone)").offspring("Tabs").child("item2").exists():
            poco("FriendsDlg(Clone)").offspring("Tabs").child("item2").click()  # 点击战队
            if poco("Create").exists():
                poco("Create").click()  # 创建战队
                if poco("Bg2").exists():
                    poco("NameInput").set_text(f"{random.randint(100000, 99999999)}")  # 输战队会名称
                    poco("Highlight").click()  # 点击创建战队
            else:
                print("已经有战队了")
        else:
            printcolor.printred("没有进入社交界面，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "没有进入社交界面")
    else:
        printcolor.printred("主界面没有社交按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面没有社交按钮")
    l_close = poco(texture="l_close_00")
    Close = poco("Close")
    for x in range(4):
        time.sleep(0.5)
        if l_close.exists() and Close.exists():
            time.sleep(1.5)
            l_close.click()
            poco("RecruitPublishView(Clone)").offspring("Close").click()
        elif Close.exists():
            time.sleep(1.5)
            Close.click()
        else:
            break
    if poco("SysAGameMall").exists():
        poco("SysAGameMall").click()
        if poco("XSys_Mall").exists():
            poco("XSys_Mall").click()
        else:
            printcolor.printred("商城界面找不到商店页签，请检查")
            return
    else:
        printcolor.printred("主界面找不到商城按钮，请检查")
        return
    for item in range(len(poco("Grid").child())):
        item1 = "item"+str(item)
        if poco("GameMall(Clone)").offspring("ShopFrame").offspring(item1).exists():  # 商店的子页签
            # if poco("GameMall(Clone)").offspring("ShopFrame").offspring(item1).offspring("shopname").exists():
            pos = poco("GameMall(Clone)").offspring("ShopFrame").offspring(item1)
            butpos(butpos=pos,pos1=0.38,pos2=0.91,high=558,low=643,lows=366)  # 调用butpos方法
            pos.click()  # 点击商店子页签
            sleep(1)
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if not poco("Create").exists():  # 创建公会
                printcolor.printgreen("进入  "+poco("ShopName").get_text()+"  界面")
                if freeze_poco("MallDlg(Clone)").offspring("TabShopFrame").child("item0").exists():
                    for item in range((len(freeze_poco("TabShopFrame").child()) - 4)):  # 点击子商店的子页签
                        item2 = "item" + str(item)
                        if freeze_poco("MallDlg(Clone)").offspring(item2).offspring("TextLabel").exists():  # 商店子页签
                            freeze_poco("MallDlg(Clone)").offspring(item2).offspring("TextLabel").click()
                            if poco("MallDlg(Clone)").offspring("Panel").child("item0").exists():  # 商店商品
                                pass
                            else:
                                printcolor.printgreen(poco("MallDlg(Clone)").offspring("TabShopFrame").child(item2).offspring(
                                    "TextLabel").get_text() + " 页签 没有找到任何售卖道具")
                else:
                    if poco("MallDlg(Clone)").offspring("item0").exists():
                        printcolor.printgreen(poco("ShopName").get_text() + " 页面没有其他子页签，界面检测到售卖道具，显示正确")
                    else:
                        printcolor.printgreen(poco("ShopName").get_text() + " 页面没有其他子页签，没有找到任何售卖道具")
                poco("Close").click()
            else:
                printcolor.printgreen("商店没有开启")
                poco("Close").click()
        else:
            printcolor.printred("商店页面没有子页签，请检查...")
    return poco("item13").child("shopname").get_text()  # 战队商店

