# -*- encoding=utf8 -*-
__author__ = "Lee.li"

from airtest.core.api import *
from multi_processframe.Tools import screenshot, printcolor, adb_connect

# 福利模块

def welfare(devices):
    poco = adb_connect.device(devices)
    if poco("SysGWelfare").exists():
        poco("SysGWelfare").click()
        print("测试福利模块")
        with poco.freeze() as freezepoco:
            name = freezepoco("TabList").offspring("TabGrid").child()
            print(f"福利中一共有{len(name)}个模块，分别为：")
            number = 1
            for c in name:
                item = c.get_name()
                uiname = freezepoco("WelfareDlg(Clone)").offspring(item).child("Title").get_text()
                print(f"{number}.{uiname}")
                number += 1
            for i in name:
                item = i.get_name()
                uiname = freezepoco("WelfareDlg(Clone)").offspring(item).child("Title").get_text()
                if uiname == "珍藏礼包":
                    zhencang(poco,item,devices)
                elif uiname == "潘多拉":
                    panduola(poco,item,devices)
                elif uiname == "异域集市":
                    yiyu(poco,item,devices)
                elif uiname == "王国特权":
                    vip(poco,item,devices)
                elif uiname == "王国礼包":
                    wangguo(poco,item,devices)
                elif uiname == "首充礼包":
                    shouchong(poco,item,devices)
                elif uiname == "签到奖励":
                    qiandao(poco,item,devices)
                elif uiname == "金币宝箱":
                    jinbi(poco,item,devices)
                elif uiname == "每日体力":
                    tili(poco,item,devices)
                elif uiname == "奖励找回":
                    zhaohui(poco,item,devices)
            poco("Close").click()
    else:
        printcolor.printred("主界面没有找到福利模块")
        screenshot.get_screen_shot(time.time(), devices, "竞技界面缺少元素，请详细查看")
    return poco("Duck").get_name()  # 返回主界面上的按钮


def move(poco,item):
    for i in range(20):
        position = poco("WelfareDlg(Clone)").offspring(item).get_position()
        if position[1] < 0.12:
            swipe((43,130),(43,400))
            time.sleep(1)
        elif position[1] > 0.95:
            swipe((43, 400), (43, 130))
            time.sleep(1)
        else:
            poco("WelfareDlg(Clone)").offspring(item).click()
            break

def zhencang(poco,item,devices): # 珍藏礼包
    move(poco,item)
    with poco.freeze() as freezepoco:
        if freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item0").child("Btn").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item1").child("Btn").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item2").child("Btn").exists() and \
            len(freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item0").offspring("List").child()) >0 and \
            len(freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item1").offspring("List").child()) >0 and \
            len(freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item2").offspring("List").child()) >0 and \
            freezepoco("DailyGift1").exists() or \
            freezepoco("DailyGift2").exists():
            printcolor.printgreen("每日领奖按钮，购买按钮，礼包奖品数目UI元素显示正常")
        else:
            printcolor.printred("珍藏礼包界面缺少UI元素，详情见截图")
            screenshot.get_screen_shot(time.time(), devices, "珍藏礼包界面缺少UI元素")
        try:
            if freezepoco("DailyGift1").exists():
                poco("DailyGift1").click()
            poco("WelfareDlg(Clone)").offspring("Grid").child("item0").child("Btn").click()
            poco("WelfareDlg(Clone)").offspring("Grid").child("item1").child("Btn").click()
            poco("WelfareDlg(Clone)").offspring("Grid").child("item2").child("Btn").click()
            printcolor.printgreen("珍藏礼包界面按钮点击正常")
        except Exception as e:
            printcolor.printred("珍藏礼包界面按钮点击异常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "珍藏礼包界面按钮点击异常")

def panduola(poco,item,devices): # 潘多拉
    move(poco, item)
    with poco.freeze() as freezepoco:
        if freezepoco("WelfareDlg(Clone)").offspring("Pandora").offspring("Display0").offspring("Point").exists() and \
                freezepoco("WelfareDlg(Clone)").offspring("Pandora").offspring("Display0").child("Label").exists() and \
                freezepoco("WelfareDlg(Clone)").offspring("Pandora").offspring("Display1").offspring("Point").exists() and \
                freezepoco("WelfareDlg(Clone)").offspring("Pandora").offspring("Display1").child("Label").exists() and \
                freezepoco("WelfareDlg(Clone)").offspring("Pandora").offspring("Display2").offspring("Point").exists() and \
                freezepoco("WelfareDlg(Clone)").offspring("Pandora").offspring("Display2").child("Label").exists() and \
                freezepoco("Once").child("Label").exists() and \
                freezepoco("Ten").child("Label").exists() and \
                freezepoco("ItemList").exists():
            printcolor.printgreen("潘多拉模型框，名称，奖励预览，开箱按钮等UI元素显示正常")
        else:
            printcolor.printred("潘多拉界面缺少UI元素，详情见截图")
            screenshot.get_screen_shot(time.time(), devices, "潘多拉界面缺少UI元素")
        try:
            poco("ItemList").click()
            poco(texture="l_close_00").click()
            poco("Once").click()
            if poco("access212").exists():
                poco(texture="l_close_00").click()
            else:
                time.sleep(3)
                poco("OK").click()
            poco("Ten").click()
            if poco("access212").exists():
                poco(texture="l_close_00").click()
            else:
                time.sleep(3)
                poco("OK").click()
            printcolor.printgreen("潘多拉界面按钮点击正常")
        except Exception as e:
            printcolor.printred("潘多拉界面按钮点击异常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "潘多拉界面按钮点击异常")

def yiyu(poco,item,devices): # 异域集市
    move(poco, item)
    with poco.freeze() as freezepoco:
        if freezepoco("ShopItemList").exists() and \
            freezepoco("Privilege").exists() and \
            freezepoco("Detail").exists() and \
            freezepoco("BtnRefresh").exists() and \
            freezepoco("Tip").exists():
            printcolor.printgreen("商品框，查看商品，刷新UI元素显示正常")
        else:
            printcolor.printred("异域集市界面缺少UI元素，详情见截图")
            screenshot.get_screen_shot(time.time(), devices, "异域集市界面缺少UI元素")
        try:
            poco("WelfareDlg(Clone)").offspring("item5").child("BtnBuy").click()
            if poco("Cancel").exists():
                poco("Cancel").click()
            poco("Detail").click()
            poco(texture="l_close_00").click()
            poco("BtnRefresh").click()
            if poco("OK").exists():
                poco("OK").click()
            poco("BtnRefresh").click()
            if poco("OK").exists():
                poco("OK").click()
            poco("WelfareDlg(Clone)").offspring("item0").child("BtnBuy").click()
            if poco("Cancel").exists():
                poco("Cancel").click()
            printcolor.printgreen("异域集市界面按钮点击正常")
        except Exception as e:
            printcolor.printred("异域集市界面按钮点击异常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "异域集市界面按钮点击异常")

def vip(poco,item,devices): # 王国特权
    move(poco, item)
    with poco.freeze() as freezepoco:
        if freezepoco("WelfareDlg(Clone)").offspring("item0").child("Detail").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("item1").child("Detail").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("item2").child("Detail").exists() and \
            freezepoco(texture="l_tq_02").exists() and \
            freezepoco(texture="l_tq_03").exists() and \
            freezepoco(texture="l_tq_01").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("item0").child("Btn").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("item1").child("Btn").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("item2").child("Btn").exists():
            printcolor.printgreen("购买按钮，详情介绍，会员标识UI元素显示正常")
        else:
            printcolor.printred("王国特权界面缺少UI元素，详情见截图")
            screenshot.get_screen_shot(time.time(), devices, "王国特权界面缺少UI元素")
        try:
            poco("WelfareDlg(Clone)").offspring("item0").child("Detail").click()
            poco(texture="l_button_00").click()
            poco("WelfareDlg(Clone)").offspring("item1").child("Detail").click()
            poco(texture="l_button_00").click()
            poco("WelfareDlg(Clone)").offspring("item2").child("Detail").click()
            poco(texture="l_button_00").click()
            poco("WelfareDlg(Clone)").offspring("item0").child("Btn").click()
            poco("WelfareDlg(Clone)").offspring("item1").child("Btn").click()
            poco("WelfareDlg(Clone)").offspring("item2").child("Btn").click()
            printcolor.printgreen("王国特权界面按钮点击正常")
        except Exception as e:
            printcolor.printred("王国特权界面按钮点击异常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "王国特权界面按钮点击异常")

def wangguo(poco,item,devices): # 王国礼包
    move(poco, item)
    with poco.freeze() as freezepoco:
        if freezepoco(texture="l_hy_02").exists() and \
            freezepoco(texture="l_hy_03").exists() and \
            freezepoco(texture="l_hy_01").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item2").offspring("List").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item1").offspring("List").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item0").offspring("List").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item0").child("Btn").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item1").child("Btn").exists() and \
            freezepoco("WelfareDlg(Clone)").offspring("Grid").child("item2").child("Btn").exists():
            printcolor.printgreen("王国礼包图片，奖励列表，购买按钮UI元素显示正常")
        else:
            printcolor.printred("王国礼包界面缺少UI元素，详情见截图")
            screenshot.get_screen_shot(time.time(), devices, "王国礼包界面缺少UI元素")
        try:
            poco("WelfareDlg(Clone)").offspring("Grid").child("item0").child("Btn").click()
            poco("WelfareDlg(Clone)").offspring(item).click()
            poco("WelfareDlg(Clone)").offspring("Grid").child("item1").child("Btn").click()
            poco("WelfareDlg(Clone)").offspring(item).click()
            poco("WelfareDlg(Clone)").offspring("Grid").child("item2").child("Btn").click()
            poco("WelfareDlg(Clone)").offspring(item).click()
            printcolor.printgreen("王国礼包界面按钮点击正常")
        except Exception as e:
            printcolor.printred("王国礼包界面按钮点击异常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "王国礼包界面按钮点击异常")

def shouchong(poco,item,devices): # 首充礼包
    move(poco, item)
    with poco.freeze() as freezepoco:
        if poco("Recharge").exists() and \
            poco("WelfareDlg(Clone)").offspring("item0").exists() and \
            poco("WelfareDlg(Clone)").offspring("item1").exists() and \
            poco("WelfareDlg(Clone)").offspring("item2").exists() and \
            poco("WelfareDlg(Clone)").offspring("item3").exists() and \
            poco("WelfareDlg(Clone)").offspring("item4").exists() and \
            poco("WelfareDlg(Clone)").offspring("item5").exists():
            printcolor.printgreen("充值按钮，6个奖励UI元素显示正常")
        else:
            printcolor.printred("首充礼包界面缺少UI元素，详情见截图")
            screenshot.get_screen_shot(time.time(), devices, "首充礼包界面缺少UI元素")
        try:
            poco("Background").click()
            poco("Close").click()
            poco("WelfareDlg(Clone)").offspring("item0").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item0").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item1").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item1").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item2").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item2").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item3").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item3").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item4").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item4").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item5").child("Icon").click()
            poco("WelfareDlg(Clone)").offspring("item5").child("Icon").click()

            printcolor.printgreen("首充礼包界面按钮点击正常")
        except Exception as e:
            printcolor.printred("首充礼包界面按钮点击异常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "首充礼包界面按钮点击异常")

def qiandao(poco,item,devices): # 签到奖励
    move(poco, item)
    with poco.freeze() as freezepoco:
        if poco("Panel").exists() and \
            poco("Check").exists() and \
            poco(text="商会成员特权可享受大量奖励翻倍福利").exists() and \
            poco("WelfareDlg(Clone)").offspring("LoginFrame").child("T")[0].child("p").exists() and \
            poco(text="每月1号重置签到奖励").exists():
            printcolor.printgreen("会员特权，签到按钮，奖励列表UI元素显示正常")
        else:
            printcolor.printred("签到奖励界面缺少UI元素，详情见截图")
            screenshot.get_screen_shot(time.time(), devices, "签到奖励界面缺少UI元素")
        try:
            if poco("Check").child("Cost").exists():
                poco("Check").click()
                poco("OK").click()
            else:
                poco("Check").click()
            printcolor.printgreen("签到奖励界面按钮点击正常")
        except Exception as e:
            printcolor.printred("签到奖励界面按钮点击异常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "签到奖励界面按钮点击异常")

def jinbi(poco,item,devices): # 金币宝箱
    move(poco, item)
    with poco.freeze() as freezepoco:
        if freezepoco("WelfareDlg(Clone)").offspring("Help").exists() and \
            freezepoco("Btn_ExchangeOne").exists() or \
            freezepoco("Btn_ExchangeTen").exists():
            printcolor.printgreen("帮助信息，兑换按钮UI元素显示正常")
        else:
            printcolor.printred("金币宝箱界面缺少UI元素，详情见截图")
            screenshot.get_screen_shot(time.time(), devices, "金币宝箱界面缺少UI元素")
        try:
            poco("Btn_ExchangeOne").click()
            poco("Btn_ExchangeOne").click()
            poco("Btn_ExchangeTen").click()
            printcolor.printgreen("兑换按钮点击正常")
        except Exception as e:
            printcolor.printred("兑换按钮点击正常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "兑换按钮点击异常")

def tili(poco,item,devices): # 每日体力
    move(poco, item)
    with poco.freeze() as freezepoco:
        if poco("GetReward").exists() or ((poco("L").child("T2").exists() and poco("R").child("T2").exists())):
            printcolor.printgreen("每日体力UI元素显示正常")
        else:
            printcolor.printred("每日体力界面缺少UI元素，详情见截图")
            screenshot.get_screen_shot(time.time(), devices, "每日体力界面缺少UI元素")
        try:
            if freezepoco("GetReward").exists():
                freezepoco("GetReward").click()
            else:
                print("今日体力已经领取")

            printcolor.printgreen("每日体力界面按钮点击正常")
        except Exception as e:
            printcolor.printred("每日体力界面按钮点击异常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "每日体力界面按钮点击异常")

def zhaohui(poco,item,devices): # 奖励找回
    move(poco, item)
    if poco("buttons").exists():
        with poco.freeze() as freezepoco:
            if freezepoco("SelectPerfect").exists() and \
                freezepoco("Reward").exists() and \
                freezepoco("WelfareDlg(Clone)").offspring("item0").child("Go").exists():
                printcolor.printgreen("完美找回，普通找回，奖励显示正常")
            else:
                printcolor.printred("奖励找回界面缺少UI元素，详情见截图")
                screenshot.get_screen_shot(time.time(), devices, "奖励找回界面缺少UI元素")
            try:
                poco("SelectNormal").click()
                poco("SelectPerfect").click()
                poco("WelfareDlg(Clone)").offspring("item0").child("Go").click()
                poco("BtnOK").click()
                printcolor.printgreen("奖励找回界面按钮点击正常")
            except Exception as e:
                printcolor.printred("奖励找回界面按钮点击异常")
                printcolor.printred(e)
                screenshot.get_screen_shot(time.time(), devices, "珍藏礼包界面按钮点击异常")
    else:
        print("奖励找回界面没有需要找回的内容")



# devices = "127.0.0.1:62001"
# welfare(devices)