"""
巢穴模块测试
巢穴排行榜
巢穴奖励
通关巢穴
"""

from multi_processframe.Tools import printcolor,adb_connect,screenshot
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
Androidpoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from multi_processframe.Tools import initial



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


def nest(devices):
    poco = adb_connect.device(devices)
    try:
        if poco("Duck").exists():
            poco("Duck").click()
            sleep(2)
        else:
            printcolor.printgreen("主界面缺少日常按钮，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
        if poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item110").offspring("Background").exists():
            pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item110").offspring("Background")  # 副本参加按钮
            butpos(butpos=pos, pos1=0.4, pos2=0.79, high=1055, low=740, lows=466)  # 调用butpos方法
            poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item110").offspring("Background").click()  # 点击副本参加按钮
            sleep(2)
            poco("Hard").click()  # 点击巢穴按钮
            sleep(4)
        else:
            printcolor.printgreen("副本界面控件缺失，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "副本界面控件缺失")

        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("Label").exists() and freeze_poco(texture="l_frame_09").exists() and \
                freeze_poco("Btn2").exists() and freeze_poco("Btn1").exists() and \
                freeze_poco("Member").exists() and  freeze_poco("Level").exists() and \
                freeze_poco("PPT").exists() and freeze_poco("MyPPT").exists():
            printcolor.printgreen("检查点 " + freeze_poco("Member").offspring("T").get_text() + "  显示正确")
            printcolor.printgreen("检查点 " + freeze_poco("Level").offspring("T").get_text() + "  显示正确")
            printcolor.printgreen("检查点 " + freeze_poco("PPT").offspring("T").get_text() + "  显示正确")
            printcolor.printgreen("检查点 " + freeze_poco("MyPPT").offspring("T").get_text() + "  显示正确")
            printcolor.printgreen("检查点 " + freeze_poco("Btn2").offspring("T").get_text() + "  显示正确")
            printcolor.printgreen("检查点 " + freeze_poco("Btn1").offspring("T").get_text() + "  显示正确")
        else:
            printcolor.printred("巢穴界面控件缺失，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "巢穴界面控件缺失")
        poco("Btn2").click()  # 点击排行榜
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("Tittle").exists() and freeze_poco("T1").exists() and freeze_poco("T2").exists() and \
                freeze_poco("T3").exists() and freeze_poco("T4").exists():
            printcolor.printgreen("检查点 " + freeze_poco("T3").get_text() + "  显示正确")
            printcolor.printgreen("检查点 " + freeze_poco("Tittle").get_text() + "  显示正确")
            printcolor.printgreen("检查点 " + freeze_poco("T2").get_text() + "  显示正确")
            printcolor.printgreen("检查点 " + freeze_poco("T4").get_text() + "  显示正确")
            printcolor.printgreen("检查点 " + freeze_poco("T1").get_text() + "  显示正确")
            poco(texture="l_close_00").click()  # 点击返回巢穴界面
        else:
            printcolor.printgreen("排行榜界面控件缺失，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "排行榜界面控件缺失")
        poco("Btn1").click()  # 点击奖励
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("Tittle").exists():
            printcolor.printgreen("进入奖励预览界面")
            for item in range(len(freeze_poco("List").child())):
                item = str(item)
                printcolor.printgreen("检查点 " + freeze_poco("NestStarReward").offspring(item).offspring("T").get_text() + "  显示正确")
            poco(texture="l_close_00").click()  # 点击返回到巢穴界面
        else:
            printcolor.printgreen("奖励界面控件缺失，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "奖励界面控件缺失")
        if poco("Diff4").exists():
            poco("Diff4").click()  # 点击地狱模式
            if poco("Do").exists():
                poco("Do").click()  # 点击进入游戏
                if poco(texture="l_frame_00").exists():
                    printcolor.printgreen("脚本环境没有调整好，战力不足，接下来强制运行剩余脚本")
                    poco(text="强行闯关").click()
                if poco("BtnCreate").exists():
                    printcolor.printgreen("没有队伍，开始创建队伍")
                    poco("BtnCreate").click()

                if poco("BtnStart").exists():
                    printcolor.printgreen("队伍已经创建，开始进入战斗")
                    poco("BtnStart").click()  # 点击进入战斗
                    sleep(50)
                    if poco("Indicate").child("Bg").exists() and poco("BtnDamageStatistics").exists():
                        printcolor.printgreen("进入巢穴，因为没有自动战斗，所以直接GM结束战斗....")
                        poco("Avatar").click()  # 点击头像，输入MG指令结束战斗
                        text("gmwin")  # 输入GM指令
                        Androidpoco("android.widget.Button").click()
                        sleep(50)
                        if poco("Title").exists():
                            printcolor.printgreen("已经跑完巢穴模块，回到主界面，脚本完成...开始离开队伍")
                            if poco("BtnLeave").exists():
                                poco("BtnLeave").click()  # 点击退出组队
                                if poco("BtnCreate").exists():
                                    printcolor.printgreen("已经离开队伍")
                    else:
                        printcolor.printred("没有回到主界面，脚本未完成")
                        screenshot.get_screen_shot(time.time(), devices, "没有回到主界面")
        else:
            printcolor.printgreen("巢穴界面地狱选项控件缺失，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "地狱选项控件缺失")
    finally:
        printcolor.printgreen("验证队伍是否真的离开。。。")
        initial.startgame(devices)
        if poco("Team").child("Selected").exists():
            poco("Team").child("Selected").click()  # 点击队伍
            poco("BtnCreate").click()  # 点击创建队伍
            if poco("BtnLeave").exists():
                poco("BtnLeave").click()  # 点击退出组队
                if poco("BtnCreate").exists():
                    printcolor.printgreen("已经离开队伍")
            else:
                printcolor.printgreen("已经离开队伍")
    return poco("Title").get_text()
