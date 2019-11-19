"""
商城模块
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
import random
from multi_processframe.ProjectTools import common


def butpos(devices,butpos,pos1=0.4,pos2=0.81,high=1330,low=930,lows=482):
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
            common.setswipe(1, [high, lows], [high, low], devices)
        elif but[1] > pos2:
            common.setswipe(1, [high, low], [high, lows], devices)
        else:
            break


def gamemall(devices):
    poco = common.deviceconnect(devices)
    if poco("SysAGameMall").exists():
        poco("SysAGameMall").click()
    else:
        common.printred("主界面找不到商城按钮，请检查")
    Mallbutlist = ["XSys_GameMall_Diamond", "XSys_GameMall_Dragon", "XSys_GameMall_CRYSTAL",
                   "XSys_Mall","XSys_GameMall_Pay"]
    for but in Mallbutlist:
        if poco(but).exists():
            common.printgreen("开始点击商城内 " + poco("GameMall(Clone)").offspring(but)
                              .offspring("SelectedTextLabel").get_text() + " 子页签")
            poco(but).click()
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for item in range(len(freeze_poco("TabsFrame").child())):
                item1 = "item" + str(item)
                if freeze_poco("GameMall(Clone)").offspring("TabsFrame").child(item1).exists():
                    if freeze_poco("GameMall(Clone)").offspring("TabsFrame").child(item1).get_position()[1] > 0:
                        if freeze_poco("GameMall(Clone)").offspring("TabsFrame").child(item1)\
                                .offspring("TextLabel").exists():
                            common.printgreen("点击 " + freeze_poco("GameMall(Clone)").offspring("TabsFrame")
                                              .child(item1).offspring("TextLabel").get_text() + " 页签")
                            freeze_poco("GameMall(Clone)").offspring("TabsFrame").child(item1).click()
                            if poco("ailin").exists():
                                common.printgreen("---------->判断 " + poco("GameMall(Clone)").offspring("TabsFrame")
                                                  .child(item1).offspring("TextLabel").get_text() + " 很穷，没有商品...")
                            elif poco("GameMall(Clone)").offspring("item0").exists():
                                common.printgreen("---------->判断 " + poco("GameMall(Clone)").offspring("TabsFrame")
                                                  .child(item1).offspring("TextLabel").get_text() + " 内容显示正确")
                        else:
                            common.printcolor("拿到控件，但是却拿不到text，很有可能是程序多写了无用控件，这句可以无视，"
                                              "因为不会影响用户体验", "blue")
                    else:
                        pass
                else:
                    common.printred("找不到商城子页签，请检查，很有可能是程序多写了无用控件.....")
            if poco("GameMall(Clone)").offspring("ShopFrame").offspring("item0").exists():
                common.printgreen("----------->" + poco("GameMall(Clone)").offspring(but)
                                  .offspring("SelectedTextLabel").get_text() + " 内子界面显示正确")
            elif poco("GameMall(Clone)").offspring("DiamondFrame").offspring("item0").exists():
                common.printgreen("----------->" + poco("GameMall(Clone)").offspring(but)
                                  .offspring("SelectedTextLabel").get_text() + " 内子界面显示正确")
        else:
            common.printred("商城界面缺少子页签，请检查")
    return poco("GameMall(Clone)").child("Bg").child("T").get_text()


def mall(start, devices):  # 商店功能测试
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
            common.printred("没有进入社交界面，请检查...")
            common.get_screen_shot(start, time.time(), devices, "没有进入社交界面")
    else:
        common.printred("主界面没有社交按钮，请检查...")
        common.get_screen_shot(start, time.time(), devices, "主界面没有社交按钮")
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
            common.printred("商城界面找不到商店页签，请检查")
            return
    else:
        common.printred("主界面找不到商城按钮，请检查")
        return

    for item in range(len(poco("Grid").child())):
        item1 = "item"+str(item)
        if poco("GameMall(Clone)").offspring("ShopFrame").offspring(item1).exists():  # 商店的子页签
            # if poco("GameMall(Clone)").offspring("ShopFrame").offspring(item1).offspring("shopname").exists():
            pos = poco("GameMall(Clone)").offspring("ShopFrame").offspring(item1)
            butpos(devices,butpos=pos,pos1=0.38,pos2=0.91,high=558,low=643,lows=366)  # 调用butpos方法
            pos.click()  # 点击商店子页签
            sleep(1)
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if not poco("Create").exists():  # 创建公会
                common.printgreen("进入  " + poco("ShopName").get_text() + "  界面")
                if freeze_poco("MallDlg(Clone)").offspring("TabShopFrame").child("item0").exists():
                    for item in range((len(freeze_poco("TabShopFrame").child()) - 4)):  # 点击子商店的子页签
                        item2 = "item" + str(item)
                        if freeze_poco("MallDlg(Clone)").offspring(item2).offspring("TextLabel").exists():  # 商店子页签
                            freeze_poco("MallDlg(Clone)").offspring(item2).offspring("TextLabel").click()
                            if poco("MallDlg(Clone)").offspring("Panel").child("item0").exists():  # 商店商品
                                pass
                            else:
                                common.printgreen(poco("MallDlg(Clone)").offspring("TabShopFrame").child(item2)
                                                  .offspring("TextLabel").get_text() + " 页签 没有找到任何售卖道具")
                else:
                    if poco("MallDlg(Clone)").offspring("item0").exists():
                        common.printgreen(poco("ShopName").get_text() +
                                          " 页面没有其他子页签，界面检测到售卖道具，显示正确")
                    else:
                        common.printgreen(poco("ShopName").get_text() +
                                          " 页面没有其他子页签，没有找到任何售卖道具")
                poco("Close").click()
            else:
                common.printgreen("商店没有开启")
                poco("Close").click()
        else:
            common.printred("商店页面没有子页签，请检查...")
    return poco("item13").child("shopname").get_text()  # 战队商店


def buy(start, devices):
    """
    测试商城购买功能，前提条件，拥有龙币，水晶，水晶GM  item 14 999999
    :param start:
    :param devices:
    :return:
    """
    poco = common.deviceconnect(devices)
    if poco("SysAGameMall").exists():
        poco("SysAGameMall").click()
    else:
        common.printred("主界面找不到商城按钮，请检查")
    Mallbutlist = ["XSys_GameMall_Dragon", "XSys_GameMall_CRYSTAL"]
    for but in Mallbutlist:
        if poco(but).exists():
            common.printgreen("开始点击商城内 " + poco("GameMall(Clone)").offspring(but)
                              .offspring("SelectedTextLabel").get_text() + " 子页签")
            poco(but).click()
            # 操作装备按钮
            if poco("GameMall(Clone)").offspring("TabsFrame").child("item1").exists():
                poco("GameMall(Clone)").offspring("TabsFrame").child("item1").click()
                if int(poco("Count").child("Label").get_text()) >= 1:  # 判断是否有的卖
                    poco("OK").click()  # 点击购买
                    if poco(texture="l_button_00").exists():
                        common.printred("货币不足，请提供可购买的货币")
                        poco("Cancel").click()  # 点击取消弹窗，否则不好重置换成了
                        common.get_screen_shot(start, time.time(), devices, "货币不足")
                        return None
                else:
                    common.printred("没有物品可以购买")
                    common.get_screen_shot(start, time.time(), devices, "没有物品可以购买")
            else:
                common.printred("没有找到装备页签，请检查")
                common.get_screen_shot(start, time.time(), devices, "主界面没有社交按钮")
    return poco("GameMall(Clone)").child("Bg").child("T").get_text()  # 水晶商城






if __name__ == "__main__":
    start = time.localtime()
    buy(start, "9b57691d")
    # mall(start, "e37c0280")
    # gamemall("e37c0280")