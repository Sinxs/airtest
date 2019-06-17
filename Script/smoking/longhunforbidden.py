"""
龙魂禁地模块自动化脚本
《脚本环境》
1、需要有一张入场券
2、如果没有入场券就不进去了---只判断界面元素
"""

from multi_processframe.Tools import printcolor,adb_connect,screenshot
from airtest.core.api import *


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


def longhunforbidden(devices):
    poco = adb_connect.device(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
    else:
        printcolor.printgreen("主界面缺少日常按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item360").offspring("Background")  # 悬赏任务参加按钮
    if pos.exists():
        butpos(butpos=pos, pos1=0.4, pos2=0.79, high=1055, low=740, lows=466)  # 调用butpos方法
        pos.click()  # 点击日常任务参加按钮
    else:
        printcolor.printgreen("日常界面没有龙魂禁地选项，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "日常界面没有龙魂禁地选项")
    if poco("Label").exists():  # 如果龙魂禁地中存在无限噩梦按钮
        poco("AbyssPartyDlg(Clone)").offspring("item0").click()
    else:
        printcolor.printgreen("龙魂禁地界面缺少无限噩梦按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "龙魂禁地界面缺少无限噩梦按钮")
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("NestName").exists() and freeze_poco("CurPPT").exists() and freeze_poco("SugPPT").exists() and \
            freeze_poco("SugLevel").exists() and freeze_poco("SweepBtn10").child("Text").exists() and \
            freeze_poco("FallBtn").exists() and freeze_poco("SweepBtn").exists() and freeze_poco("EnterBtn").exists():
        printcolor.printgreen("龙魂禁地界面元素判断正确，包括标题，进入条件，扫荡，图鉴按钮")
        printcolor.printgreen("开始判断副本选项。。。")
        for Abyss in range(len(freeze_poco("LevelFrame").child())-1):
            Abyss1 = "Abyss" + str(Abyss)
            if freeze_poco(Abyss1).exists():
                pass
        printcolor.printgreen("副本选项判断完毕。。。下面开始进行扫荡操作，请确保有扫荡券。。。没有的话就不扫荡了。。。钱多也不想买")
        if 10 < int(poco("item0").child("value").get_text()) > 0:  # 扫荡券>0
            printcolor.printgreen("扫荡券不足10个只扫荡一次。。")
            poco("SweepBtn").click()  # 点击扫荡一次
        elif int(poco("item0").child("value").get_text()) > 10:  # 扫荡券>10
            printcolor.printgreen("土豪，扫荡券超过10个了，扫荡10次")
            poco("SweepBtn10").click()  # 点击扫荡10次
        elif int(poco("item0").child("value").get_text()) == 0:  # 扫荡券>10
            printcolor.printgreen("没有扫荡券，不进行扫荡操作")
        printcolor.printgreen("开始判断掉落图鉴界面控件元素")
        poco("FallBtn").click()  # 点击掉落图鉴
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("ItemListHandler").child("Bg").child("Tittle").exists():
            printcolor.printgreen("打开掉落图鉴成功，开始判断界面掉落奖品")
            for item in range(len(poco("ItemListHandler").offspring("S").child("Grid").child())):
                item1 = "item" + str(item)
                if freeze_poco("ItemListHandler").offspring("S").offspring(item1).exists():
                    pass
                else:
                    printcolor.printgreen("掉落图鉴界面缺少控件元素，请检查...")
                    screenshot.get_screen_shot(time.time(), devices, "掉落图鉴界面缺少控件元素")
            printcolor.printgreen(f"掉落图鉴奖品判断完毕，一共{item}种道具")
        else:
            printcolor.printgreen("掉落图鉴界面没有打开，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "掉落图鉴界面缺少控件元素")
    else:
        printcolor.printgreen("龙魂禁地界面缺少控件元素，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "龙魂禁地界面缺少控件元素")

    printcolor.printgreen("界面存在进入按钮，但是因为时间问题，可以以后优化，因为想要判断副本结束时间，需要时间。。。")
    return poco("Tittle").get_text()

