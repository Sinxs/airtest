# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from multi_processframe.Tools import initial
from poco.drivers.unity3d import *
poco = UnityPoco()

def Fashionpos(poco):  # 进入时装收集界面
    """
    在主界面寻找角色按钮，如果没找到就点击 + 号
    进入时装收集界面
    :return:
    """
    SysAItem = poco("SysAItem")
    AItempos = SysAItem.get_position()
    if AItempos[0] > 1:
        print("当前界面没有技能按钮，点击 + 号")
        poco(texture="switch").click()  # 点击+号
        if poco("SysAItem").exists():
            poco("SysAItem").click()  # 点击角色按钮
        if poco("ItemNewDlg(Clone)").offspring("XSys_Fashion").offspring("SelectedTextLabel").exists():  # 判断时装按钮并点击
            poco("ItemNewDlg(Clone)").offspring("XSys_Fashion").offspring("SelectedTextLabel").click()
        if poco("Btnclothes").exists():  # 判断衣柜换装并点击
            poco("Btnclothes").click()
        if poco("FashionRecord").exists():
            poco("FashionRecord").click()
    else:
        print("当前界面就有角色按钮")
        if poco("SysAItem").exists():
            poco("SysAItem").click()  # 点击角色按钮
        if poco("ItemNewDlg(Clone)").offspring("XSys_Fashion").offspring("SelectedTextLabel").exists():  # 判断时装按钮并点击
            poco("ItemNewDlg(Clone)").offspring("XSys_Fashion").offspring("SelectedTextLabel").click()
        if poco("Btnclothes").exists():  # 判断衣柜换装并点击
            poco("Btnclothes").click()
        if poco("FashionRecord").exists():
            poco("FashionRecord").click()


def Fashiontextpos(poco):  # 寻找最后一个时装并获取该控件的text
    """
    寻找最后一个时装
    拿到该控件的text值
    :return:
    """
    A = 425
    B = 830
    for i in range(15):  # TODO：15次是为了保证最大概率能滑到底部-----其实并不严谨，因为设备卡爆了的情况也不是没有-_-!!!
        swipe((A, B), (A, 417), 150)
        sleep(1)
        A -= 1
        B += 3
    if poco("Select").offspring("item0").exists():
        if poco("Select").offspring("item0").get_position()[1] > 0.8:
            pass
    else:
        Fashiontextpos(poco)
    Fashiontext = poco("Select").offspring("item0").offspring("TextLabel").get_text()  # 获取最后一件时装的text值
    print("最后一个是-->>>>"+Fashiontext)
    return Fashiontext


def Fashion_text7(item,poco):  # 七件套装 or 五件套装数量
    """
    七件套装测试
    :param item: = 套装数量
    :return:
    """
    for item_1 in range(int(item)):  # 获取当前时装的件数，然后点击当前时装的件数
        item1 = "Part" + str(item_1)
        print(f"点击第 {item1} 件时装")
        poco(item1).child("Icon").child("Icon").click()
        if poco("FashionStorageFashionToolTip(Clone)").child("Bg").offspring("ItemTpl").child("Icon").exists():
            if poco(texture="l_close_00").exists():
                poco(texture="l_close_00").click()
            else:
                touch((1968, 419), times=1)  # 点击屏边角位置，达到取消弹窗的目的
        else:
            print("ERROR:时装显示错误，请检查。。。。")


def Fashion_text3(poco):  # 三件时装测试
    """
    三件时装测试
    :return:
    """
    for i in range(7,10):
        item1 = "Part" + str(i)
        print(f"点击第 {item1} 件时装")
        if poco(item1).exists():
            poco(item1).click()
            if poco("FashionStorageFashionToolTip(Clone)").child("Bg").offspring("ItemTpl").child("Icon").exists():
                if poco(texture="l_close_00").exists():
                    poco(texture="l_close_00").click()
                else:
                    touch((1968, 419), times=1)  # 点击屏边角位置，达到取消弹窗的目的
            else:
                print("ERROR:时装显示错误，请检查。。。。")

def Fashion_text2(poco):  # 2件时装测试
    """
    两件时装测试
    :return:
    """
    for i in range(5,7):
        item1 = "Part" + str(i)
        print(f"点击第 {item1} 件时装")
        if poco(item1).exists():
            poco(item1).click()
            if poco("FashionStorageFashionToolTip(Clone)").child("Bg").offspring("ItemTpl").child("Icon").exists():
                if poco(texture="l_close_00").exists():
                    poco(texture="l_close_00").click()
                else:
                    touch((1968, 419), times=1)  # 点击屏边角位置，达到取消弹窗的目的
            else:
                print("ERROR:时装显示错误，请检查。。。。")

def findtext1(Fashiontext,poco):  # 依次点击最新的
    for i in range(11):
        item1 = "item" + str(i)
        if poco("Select").offspring(item1).offspring("TextLabel").exists():
            item = poco("Select").offspring(item1).offspring("TextLabel").get_text()
        else:
            continue
        print(item)
        item2 = int(item[-2]) # 获取当前text值的倒数第二个属性
        print("当前时装有    " + str(item2) + "    件")
        if poco("Select").offspring(item1).offspring("TextLabel").exists():  # 点击当前控件
            poco("Select").offspring(item1).offspring("TextLabel").click()  # 点击当前控件
        else:
            continue
        if item2 == 7 or item2 == 5:
            Fashion_text7(item2,poco)
            if Fashiontext == item:  # 如果点到了最后就停止
                break
        if item2 == 3:
            Fashion_text3(poco)
            if Fashiontext == item:  # 如果点到了最后就停止
                break
        if item2 == 2:
            Fashion_text2(poco)
            if Fashiontext == item:  # 如果点到了最后就停止
                break
        for i in range(5):  # TODO：为了应付手机的卡顿问题，特意容错5次，够意思了吧！！！不在坐标内的控件就滑动到坐标内
            pos = poco("Select").offspring(item1).offspring("TextLabel").get_position()
            global test
            test = poco("Select").offspring(item1).offspring("TextLabel").get_text()
            if pos[1] > 0.7:  #  滑动时装控件
                swipe((425, 816), (425, 545))
            elif pos[1] < 0.33:
                swipe((425, 545), (425, 816))
            else:
                break
            # test = poco("Select").offspring(item1).offspring("TextLabel").get_text()
    return test


def Fashion_text1(poco):
    """
    获取最后一件时装的text值，以便于进行对比
    :return:
    """
    Fashionpos(poco)  # 进入时装收集界面
    Fashiontext = Fashiontextpos(poco)  # 翻到最后底部并且拿到
    print(Fashiontext)
    for x in range(10):
        l_close = poco(texture="l_close_00")
        Close = poco("Close")
        if l_close.exists() and Close.exists():
            poco(texture="l_close_00").click()
        elif Close.exists():
            Close.click()
        else:
            break
    Fashionpos(poco)
    for i in range(5):
        findtext2 = findtext1(Fashiontext,poco)
        print(findtext2)
        findtext3 = findtext2
        if findtext3 == Fashiontext:
            break


def Switchroles_1(poco):
    """
    1、重置脚本运行环境
    2、点击头像进入角色选择界面
    :return:
    """
    if not poco("Open").exists():
        poco("Avatar").click()
        touch((2255, 1026))  # 点击GM出现的确定控件
        poco(text="切换角色").click()
        sleep(10)
    else:
        poco("Avatar").click()
        poco(text="切换角色").click()
        sleep(10)



def Switchroles_2(chroles, poco):
    """
    1、选择账号角色
    :return:
    """
    Prof = "Prof"+ str(chroles)
    poco(Prof).click()
    sleep(3)
    poco("Label").click()
    sleep(11)
    for x in range(10):
        l_close = poco(texture="l_close_00")
        Close = poco("Close")
        if l_close.exists() and Close.exists():
            poco(texture="l_close_00").click()
        elif Close.exists():
            Close.click()
        else:
            break







def test_fashionwarrior(devices):  # Prof1-转职为战士分支、剑圣分支、月之领主职业
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Switchroles_1(poco)
    Switchroles_2(1, poco)
    Fashion_text1(poco)
    return poco("title_back").child("Title").get_text()


def test_fashionarcher(devices):  # Prof2-转职为弓箭手分支、箭神分支、魔羽分支
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Switchroles_1(poco)
    Switchroles_2(2, poco)
    Fashion_text1(poco)
    return poco("title_back").child("Title").get_text()


def test_fashionmagic(devices):  # Prof3-转职为魔法师分支、元素分支、冰灵分支
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Switchroles_1(poco)
    Switchroles_2(3, poco)
    Fashion_text1(poco)
    return poco("title_back").child("Title").get_text()


def test_fashionpastor(devices): # Prof4-转职为牧师分支、祭祀分支、雷神分支
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Switchroles_1(poco)
    Switchroles_2(4, poco)
    Fashion_text1(poco)
    return poco("title_back").child("Title").get_text()


def test_fashionscholar(devices):  # Prof5-转职为学者分支、工程师分支、重炮手分支
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Switchroles_1(poco)
    Switchroles_2(5, poco)
    Fashion_text1(poco)
    return poco("title_back").child("Title").get_text()


def test_fashionthug(devices):  # Prof6-转职为刺客分支、暗之使徒分支、烈分支
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Switchroles_1(poco)
    Switchroles_2(6, poco)
    Fashion_text1(poco)
    return poco("title_back").child("Title").get_text()


def test_fashiondance(devices):  # Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Switchroles_1(poco)
    Switchroles_2(7, poco)
    Fashion_text1(poco)
    return poco("title_back").child("Title").get_text()
