# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from airtest.core.api import *
from multi_processframe.Tools import screenshot, printcolor, adb_connect

def active(devices):
    """
    活跃奖励测试脚本
    :param devices:
    :return:
    """
    poco = adb_connect.device(devices)
    poco("Duck").click()
    poco("XSys_Reward_Activity").click()
    if poco("LivenessActivityFrame").exists():  # 判断奖励界面是否存在
        with poco.freeze() as freeze_poco:
            if freeze_poco("DetailsBtn").exists() and \
                    freeze_poco("CurrentExp").exists() and \
                    freeze_poco("Chests").child("item0").exists() and \
                    freeze_poco("Chests").child("item1").exists() and \
                    freeze_poco("Chests").child("item2").exists() and \
                    freeze_poco("Chests").child("item3").exists() and \
                    freeze_poco("Chests").child("item4").exists() and \
                    freeze_poco("LeftView").child("Exp").exists() and \
                    freeze_poco("LeftView").child("Exp500").exists() and \
                    freeze_poco("LeftView").child("Exp1000").exists() and \
                    freeze_poco("LeftView").child("Exp500").child("box").exists() and \
                    freeze_poco("LeftView").child("Exp1000").child("box").exists() and \
                    freeze_poco("DailyActivityDlg(Clone)").offspring("RightView").offspring("Go").exists():
                printcolor.printgreen("活跃奖励界面UI元素显示正常")
            else:
                printcolor.printred("活跃奖励UI元素显示异常，详情见截图")
                screenshot.get_screen_shot(time.time(), devices, "活跃奖励UI元素显示异常")
            try:
                with poco.freeze() as freeze_poco:
                    freeze_poco("DetailsBtn").click()
                    poco(texture="l_close_00").click()
                    for i in freeze_poco("Chests").child():
                        i.click()
                        i.click()
                    freeze_poco("LeftView").child("Exp500").child("box").click()
                    freeze_poco("LeftView").child("Exp500").child("box").click()
                    freeze_poco("LeftView").child("Exp1000").child("box").click()
                    freeze_poco("LeftView").child("Exp1000").child("box").click()
                    if poco("ItemIconListDlg(Clone)").child("Bg").child("ListPanel").exists():
                        freeze_poco("LeftView").child("Exp1000").child("box").click()
                    printcolor.printgreen("活跃奖励模块所有按钮点击正常")
            except Exception as e:
                printcolor.printred("活跃奖励界面按钮点击流程异常")
                printcolor.printred(e)
                screenshot.get_screen_shot(time.time(), devices, "活跃奖励界面按钮点击流程异常")
        try:
            with poco.freeze() as freeze_poco:
                for i in freeze_poco("DailyActivityDlg(Clone)").offspring("RightView").offspring("Icon"):
                    item = i.parent().get_name()
                    move(poco,item)
                    name = freeze_poco("DailyActivityDlg(Clone)").offspring("RightView").child(item).offspring("Name").get_text()
                    if freeze_poco("DailyActivityDlg(Clone)").offspring("RightView").child(item).child("Go").exists():
                        if name == "兢兢业业":
                            print(f"【{name}】日常任务不点击前往")
                        else:
                            poco("DailyActivityDlg(Clone)").offspring("RightView").child(item).child("Go").click()
                            if poco("Close").exists() and (not poco("DailyActivityDlg(Clone)").exists()):
                                poco("Close").click()
                                if poco("DailyActivityDlg(Clone)").exists():
                                    printcolor.printgreen(f"【{name}】点击前往正常")
                                else:
                                    printcolor.printred(f"【{name}】点击前往正常异常")
                                    initial(poco)
                            else:
                                if poco("BuyFrame").exists():
                                    touch([96, 486], times=2)
                                    if not poco("BuyFrame").exists():
                                        printcolor.printgreen(f"【{name}】点击前往正常")
                                    else:
                                        touch([96, 486], times=2)
                    else:
                        print(f"【{name}】的任务已经完成")
            poco("Close").click()
        except Exception as e:
            printcolor.printred("活跃奖励界面前往按钮点击流程异常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "活跃奖励界面前往按钮点击流程异常")
    else:
        printcolor.printred("活跃奖励界面报错，详情见截图")
        screenshot.get_screen_shot(time.time(), devices, "活跃奖励界面报错")
    poco("Close").click()
    return poco("Duck").get_name()   # 返回值poco("Duck").get_name()

def move(poco,item):
    for i in range(20):
        position = poco("DailyActivityDlg(Clone)").offspring("RightView").child(item).get_position()
        if position[1] < 0.34:
            swipe((550,280),(550,540))
            time.sleep(1)
        elif position[1] > 0.8:
            swipe((550, 540), (550, 280))
            time.sleep(1)
        else:
            poco("DailyActivityDlg(Clone)").offspring("RightView").child(item).click()
            break

def initial(poco):
    l_close = poco(texture="l_close_00")
    Close = poco("Close")
    for x in range(4):
        time.sleep(3)
        if l_close.exists() and Close.exists():
            time.sleep(1.5)
            l_close.click()
        elif Close.exists():
            sleep(1.5)
            Close.click()
        else:
            poco("Duck").click()
            poco("XSys_Reward_Activity").click()
            break



devices = "127.0.0.1:62001"
active(devices)