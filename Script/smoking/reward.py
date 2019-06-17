"""
悬赏任务模块自动化脚本
《脚本环境》

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


def reward(devices):
    poco = adb_connect.device(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
    else:
        printcolor.printgreen("主界面缺少日常按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item904").offspring("Background")  # 悬赏任务参加按钮
    if pos.exists():
        butpos(butpos=pos, pos1=0.4, pos2=0.79, high=1055, low=740, lows=466)  # 调用butpos方法
        pos.click()  # 点击日常任务参加按钮
    else:
        printcolor.printgreen("日常界面没有悬赏任务选项，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "日常界面没有悬赏任务选项")
    if not poco(text="联盟悬赏").exists():  # 判断是否已经接了任务
        printcolor.printgreen("还未接取任务，开始接任务")
        sleep(30)
        for i in range(5):
            if poco("TalkTextBg").child("Bg").exists():  # 如果弹出了任务弹窗
                poco("VirtualTab").click()  # 点击下一步
                if poco("BtnOK").exists():  # 如果出现了接受按钮
                    printcolor.printgreen("接受任务")
                    poco("BtnOK").click()  # 点击接受
                    break
    if poco(text="联盟悬赏").exists():  # 判断是否已经接了任务
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        printcolor.printgreen("已经接了悬赏任务，开始检测任务模块控件")
        if freeze_poco("Bg2").exists() and freeze_poco("ChestX").exists() and freeze_poco("RightItem").exists() and \
                freeze_poco("Text").exists() and freeze_poco("TaskRewards").exists() and freeze_poco("RefreshBtn").exists() and \
                freeze_poco("CommitBtn").exists() and freeze_poco("BountyList").exists():
            printcolor.printgreen("悬赏任务模块控件元素判断完毕，开始判断悬赏任务")
            for item in range(len(freeze_poco("BountyList").child())):
                item1 = "item" + str(item)
                if freeze_poco("BountyList").child(item1).exists():
                    pass
                else:
                    printcolor.printred("悬赏任务缺失，请检查...")
                    screenshot.get_screen_shot(time.time(), devices, "悬赏任务缺失")
            printcolor.printgreen("悬赏任务判断完毕，开始判断刷新任务模块")
        if poco("FreeLabel").exists():
            if int(poco("FreeLabel").get_text()[-3]) > 0:  # 刷新次数
                printcolor.printgreen("任务还有刷新次数，点击刷新")
                poco("RefreshBtn").click()
        elif poco(text="刷新").exists():  # 刷新次数
            printcolor.printgreen("任务没有刷新次数了，我准备用龙币刷新，我钱多。。。")
            poco("RefreshBtn").click()
            printcolor.printgreen("好了，我用龙币帮你刷新了。。。\n还有我没有点击前往，因为前往都是模块本身，这些模块都会有自己的脚本。。。")
        else:
            printcolor.printred("刷新按钮缺失，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "刷新按钮缺失")
    return poco("CommitBtn").child("T").get_text()
