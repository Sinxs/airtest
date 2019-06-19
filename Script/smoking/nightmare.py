"""
噩梦庭院模块，判断所有元素,各个控件是否点击
"""

from multi_processframe.Tools import printcolor, adb_connect, screenshot
from airtest.core.api import *


def butpos(butpos, pos1=0.4, pos2=0.81, high=1330, low=930, lows=482):
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


def nightmare(devices):
    poco = adb_connect.device(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        printcolor.printgreen("主界面缺少日常按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item519").offspring("Background")  # 噩梦庭院参加按钮
    if pos.exists():
        butpos(butpos=pos, pos1=0.4, pos2=0.79, high=1055, low=740, lows=466)  # 调用butpos方法
        pos.click()  # 点击bossrush参加按钮
    else:
        printcolor.printgreen("日常界面没有噩梦庭院选项，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "日常界面没有噩梦庭院选项")
    if poco("Tip").exists():  # 如果有红框提示，就去掉
        poco(texture="titanbar_0").click()
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("SeasonRewards").exists() and freeze_poco("SeasonTime").exists() and \
            freeze_poco("Time4").exists() and freeze_poco("CurReachLv").exists() and \
            freeze_poco("Time").exists() and freeze_poco("Text").exists() and freeze_poco("Text1").exists() and \
            freeze_poco("Kaishi").exists() and freeze_poco("Time2").exists():  # 判断噩梦庭院界面的元素
        printcolor.printgreen(poco("RightPanel").child("T").get_text())
        printcolor.printgreen("噩梦庭院界面判断完毕，显示正确")
        poco("GetRewardBtn").click()  # 点击领取按钮
        printcolor.printgreen("领取按钮点击。。。")
        poco("SeasonRewards").click()  # 点击赛季奖励
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        printcolor.printgreen("点击排名奖励，判断界面元素")
        if freeze_poco(text="排名奖励").exists():
            for item in range(len(freeze_poco("ScrollView").child())):
                item1 = "item" + str(item)
                if freeze_poco("NightmareCourtyard(Clone)").offspring("RankRewardHandler").offspring("ScrollView").child(item1).exists():
                    pass
            printcolor.printgreen("排名奖励显示正确")
            poco(texture="l_close_00").click()
        else:
            printcolor.printgreen("排名奖励控件缺失，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "排名奖励控件缺失")
        if not poco(text="排名奖励").exists():
            poco("DisplayAll").click()  # 点击显示全部奖励
            printcolor.printgreen("点击显示全部奖励")
            if poco(text="层数奖励").exists():
                for item in range(len(poco("NightmareCourtyard(Clone)").child("SeasonRewards").offspring("Grid").child())):
                    item1 = "item" + str(item)
                    if poco("NightmareCourtyard(Clone)").child("SeasonRewards").offspring("Grid").child(item1).exists():
                        pass
                printcolor.printgreen("全部奖励显示正确")
                poco(texture="l_close_00").click()
        else:
            printcolor.printgreen("全部奖励控件缺失，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "全部奖励控件缺失")
    printcolor.printgreen("没有进入战斗，因为进入战斗会导致重置脚本的时候存在影响下一个脚本的风险。。。可以单独做战斗方面的脚本还有就是排行榜。。没有信息")
    return poco("SeasonRewards").child("T").get_text()  # 赛季奖励
