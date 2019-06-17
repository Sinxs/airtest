"""
任务模块自动化脚本
《脚本环境》
1、角色已经接了一个或多个任务
2、角色已经加入公会
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


def task(devices):
    poco = adb_connect.device(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
    else:
        printcolor.printgreen("主界面缺少日常按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item886").child("JoinBtn")  # 龙穴参加按钮
    if pos.exists():
        butpos(butpos=pos, pos1=0.4, pos2=0.79, high=1055, low=740, lows=466)  # 调用butpos方法
        pos.click()  # 点击日常任务参加按钮
    else:
        printcolor.printgreen("日常界面没有日常任务选项，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "日常界面没有日常任务选项")
    if not poco(texture="l_tip_00").exists():
        printcolor.printgreen("还未接取任务，开始接任务")
        sleep(30)
        for i in range(5):
            if poco("TalkTextBg").child("Bg").exists():  # 如果弹出了任务弹窗
                poco("VirtualTab").click()  # 点击下一步
                if poco("BtnOK").exists():  # 如果出现了接受按钮
                    printcolor.printgreen("接受任务")
                    poco("BtnOK").click()  # 点击接受
                    break
    if poco(texture="l_tip_00").exists():
        printcolor.printgreen("已经接了任务，开始检测任务模块控件")
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco(texture="DailyTaskText").exists() and freeze_poco("BaseInfo").exists() and freeze_poco("item0").exists() and \
                freeze_poco("item1").exists() and freeze_poco("item2").exists() and freeze_poco("item3").exists() and \
                freeze_poco("Submmit").exists() and freeze_poco("Refresh").exists() and \
                freeze_poco("GuildDailyTask(Clone)").child("Bg")[0].child("T")[0].exists() and freeze_poco("RefreshLogBtn").exists():  # 检测任务模块控件
            printcolor.printgreen("任务窗口检测各个按钮，控件，奖励 完成")
            if poco("Refresh").exists():  # 点击刷新
                printcolor.printgreen("点击任务刷新按钮，检测任务刷新界面中的元素控件")
                poco("Refresh").click()
                sleep(2)
                freeze_poco = poco.freeze()  # TODO：定义冻结poco
                if freeze_poco("DailyTaskInviteDlg(Clone)").offspring("TaskLevel").exists() and \
                        freeze_poco("TabTpl0").exists() and freeze_poco("TabTpl1").exists() and \
                        freeze_poco("DailyTaskInviteDlg(Clone)").offspring("Tab0Text").child("T")[0].exists() and \
                        freeze_poco("DailyTaskInviteDlg(Clone)").offspring("Tab0Text").child("T")[1].exists() and \
                        freeze_poco("DailyTaskInviteDlg(Clone)").offspring("Tab0Text").child("T")[2].exists() and \
                        freeze_poco("DailyTaskInviteDlg(Clone)").offspring("item0").exists():
                    printcolor.printgreen("刷新任务窗口检测各个按钮，控件，奖励 完成")
                    poco("DailyTaskInviteDlg(Clone)").offspring("Close").click()  # 点击返回
                else:
                    printcolor.printred("任务刷新按钮界面缺少控件元素，请检查。。。")
                    screenshot.get_screen_shot(time.time(), devices, "任务刷新按钮界面缺少控件元素")
            else:
                printcolor.printred("界面没有任务刷新按钮，请检查。。。")
                screenshot.get_screen_shot(time.time(), devices, "界面没有任务刷新按钮")
            if poco(text="求助").exists():  # 如果界面有求助的话，点击求助按钮
                printcolor.printgreen("开始点击求助按钮")
                pos = poco(text="求助")
                butpos(butpos=pos, pos1=0.29, pos2=0.73, high=1055, low=740, lows=466)  # 调用butpos方法
                poco(text="求助").click()
                printcolor.printgreen("点击求助完成")
            elif poco(text="已求助").exists():
                printcolor.printgreen("界面没有求助按钮，已经求助过了")
            else:
                printcolor.printgreen("界面没有求助按钮，也没有以求助按钮，所以为确保产品质量，建议手动测试一次")
                screenshot.get_screen_shot(time.time(), devices, "界面没有求助按钮")
            if poco("RefreshLogBtn").exists():
                poco("RefreshLogBtn").click()
                freeze_poco = poco.freeze()  # TODO：定义冻结poco
                if freeze_poco("LogPanel").child("T").exists():
                    printcolor.printgreen("开始检查任务刷新界面的控件元素")
                    printcolor.printgreen("检查点  "+freeze_poco("LogPanel").offspring("Title").child("T")[0].get_text()+"  显示正确")
                    printcolor.printgreen("检查点  "+freeze_poco("LogPanel").offspring("Title").child("T")[1].get_text()+"  显示正确")
                    printcolor.printgreen("检查点  "+freeze_poco("LogPanel").offspring("Title").child("T")[2].get_text()+"  显示正确")
            else:
                printcolor.printgreen("界面没有刷新纪录，请检查")
                screenshot.get_screen_shot(time.time(), devices, "界面没有求助按钮")
    return poco("LogPanel").child("T").get_text()  # 返回 任务刷新记录



