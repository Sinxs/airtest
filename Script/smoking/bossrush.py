"""
bossrush模块，有次数就先判断元素在进去然后出来，没有次数就直接判断界面元素
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


def bossrush(devices):
    poco = adb_connect.device(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        printcolor.printgreen("主界面缺少日常按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item48").offspring("Background")  # bossrush参加按钮
    if pos.exists():
        butpos(butpos=pos, pos1=0.4, pos2=0.79, high=1055, low=740, lows=466)  # 调用butpos方法
        pos.click()  # 点击bossrush参加按钮
    else:
        printcolor.printgreen("日常界面没有bossrush选项，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "日常界面没有bossrush选项")
    if poco("BossRushNewDlg(Clone)").child("Bg").child("Boss").exists():
        printcolor.printgreen("成功进入bossrush界面。开始检测界面元素")
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        printcolor.printgreen("检查点 " + freeze_poco("BossRushNewDlg(Clone)").offspring("left").child("RemainTime").get_text() + " 显示正确")
        printcolor.printgreen("检查点 " + freeze_poco("BossRushNewDlg(Clone)").offspring("left").child("Name").get_text() + " 显示正确")
        printcolor.printgreen("检查点 " + freeze_poco(text="攻击").get_text() + " 显示正确")
        printcolor.printgreen("检查点 " + freeze_poco(text="防御").get_text() + " 显示正确")
        printcolor.printgreen("检查点 " + freeze_poco(text="生命").get_text() + " 显示正确")
        printcolor.printgreen("检查点 " + freeze_poco(texture="kz_nk2").child("SkillName").get_text() + " 显示正确")
        if poco("SweepButton").exists():  # 仅判断没有开会员的状态
            printcolor.printgreen("开始判断扫荡控件，仅判断没有开会员的状态")
            poco("SweepButton").click()
            if poco(texture="l_frame_00").exists():  # 提示开会员的弹窗
                printcolor.printgreen("扫荡控件，功能正确")
                poco(text="取消").click()  # 取消扫荡提示框
            else:
                printcolor.printred("扫荡功能没有弹出提示框，请检查.....")
                screenshot.get_screen_shot(time.time(), devices, "扫荡功能没有弹出提示框")

        if int(freeze_poco("BossRushNewDlg(Clone)").child("Num").get_text()[-3]) == 0:  # 判断今日进入次数
            printcolor.printgreen("没有次数了，不能刷新")
            printcolor.printgreen("没有次数了，要不明天在打吧！！！")
        elif int(freeze_poco("BossRushNewDlg(Clone)").child("Num").get_text()[-3]) != 0:  # 判断今日进入次数
            printcolor.printgreen("今天的次数还没有用，现在开始点击刷新\n然后进入bossrush副本")
            poco("Refresh").click()  # 点击刷新按钮，没啥效果，特效我有看不出来
            printcolor.printgreen("点击刷新按钮，没啥效果，特效我又看不出来。。。")
            printcolor.printgreen("现在的bossrush更换为了  "+poco("BossRushNewDlg(Clone)").offspring("left").child("Name").get_text())
            printcolor.printgreen("考虑了一下，不进副本了，每天最多进一次，对于自动化来说，意义更小。所以进入的代码屏蔽掉了")
            # poco("Go").click()  # 进入副本
            # sleep(18)
            # if poco("Avatar").exists():
            #     printcolor.printgreen("进入boosrush成功，并且检测完成，现在开始退出")
            #     poco("Pause").child("p")[0].click()
            #     if poco("Leave").exists():
            #         poco("Leave").click()  # 退出副本
            #         poco("OK").click()  # 确定退出
            #         sleep(15)
            # else:
            #     printcolor.printred("没有进入副本，请检查。。。")
            #     screenshot.get_screen_shot(time.time(), devices, "没有进入副本")
    else:
        printcolor.printgreen("检测到没有进入bossrush界面，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "检测到没有进入bossrush界面")
    return poco("Go").child("T1").get_text()



