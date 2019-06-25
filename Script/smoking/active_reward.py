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
    else:
        printcolor.printred("活跃奖励界面报错，详情见截图")
        screenshot.get_screen_shot(time.time(), devices, "活跃奖励界面报错")
    poco("Close").click()
    return poco("Duck").get_name()   # 返回值poco("Duck").get_name()


# devices = "127.0.0.1:62001"
# active(devices)