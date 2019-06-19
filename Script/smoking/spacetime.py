"""
时空裂缝模块，判断界面元素，控件点击
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


def space_time(devices):
    poco = adb_connect.device(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        printcolor.printgreen("主界面缺少日常按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item1021").offspring("Background")  # 时空裂缝参加按钮
    if pos.exists():
        butpos(butpos=pos, pos1=0.4, pos2=0.79, high=1055, low=740, lows=466)  # 调用butpos方法
        pos.click()  # 点击无限幻境参加按钮
    else:
        printcolor.printgreen("日常界面没有时空裂缝选项，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "日常界面没有时空裂缝选项")
    if poco(texture="ld_bg_h2Split").exists():
        printcolor.printgreen("进入时空裂缝界面，开始检测界面控件元素")
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("12").exists() and freeze_poco("LevelOne").child("Label").exists() and \
                freeze_poco("LevelOne").offspring("item0").child("T").exists() and \
                freeze_poco("LevelOne").offspring("item1").child("T").exists() and \
                freeze_poco("LevelOne").offspring("item2").child("T").exists() and \
                freeze_poco("Leveltwo").exists() and freeze_poco("Levelthree").exists():
            printcolor.printgreen("时空裂缝界面--显示正确")
            for item in range(len(freeze_poco("Grid").child())):  # 点击奖励小icon
                item1 = "item"+str(item)
                freeze_poco(item1).click()
                freeze_poco(item1).click()
            if poco("ItemToolTipDlg(Clone)").child("Bg").exists():  # 判断是不是小弹窗还在，如果在就点掉
                poco(item1).click()
        if poco("RankDetail").child("p")[1].exists():  # 排行榜
            poco("RankDetail").child("p")[1].click()
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if freeze_poco("ToggleGuild").child("SelectedText").exists() and \
                    freeze_poco("ToggleFriend").child("SelectedText").exists() and \
                    freeze_poco("word").exists() and freeze_poco("title1").exists() and freeze_poco("title3").exists():
                printcolor.printgreen("时空裂缝界面-->>排行榜显示正确")
                poco(texture="l_close_00").click()
            else:
                printcolor.printred("排行榜缺少控件，请检查...")
                screenshot.get_screen_shot(time.time(), devices, "排行榜缺少控件")
        if poco(texture="l_close_00").exists():
            poco(texture="l_close_00").click()  # 二次判断返回按钮，避免出现界面卡死影响下次操作
        if poco(texture="Icon_Treasure1").exists():
            poco(texture="Icon_Treasure1").click()
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if freeze_poco("Title").exists() and freeze_poco(text="排名奖励").exists() and freeze_poco(text="排名进入").exists() and \
                    freeze_poco(text="奖励").exists() and poco("RewardDlg").child("Bg").offspring("item0").exists() and \
                    freeze_poco("RewardDlg").child("Bg").offspring("item2").exists() and \
                    freeze_poco("RewardDlg").child("Bg").offspring("item1").exists() and \
                    freeze_poco("RewardDlg").child("Bg").offspring("item3").exists():
                printcolor.printgreen("时空裂缝界面-->>排名奖励显示正确")
            else:
                printcolor.printred("排名奖励缺少控件，请检查...")
                screenshot.get_screen_shot(time.time(), devices, "排名奖励缺少控件")
    return poco(text="排名奖励").get_text()  # 排名奖励