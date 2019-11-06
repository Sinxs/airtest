# -*- encoding=utf8 -*-
__author__ = "Lee.li"

from multi_processframe.ProjectTools.common import *
from airtest.core.api import *


def active(start, devices):
    """
    活跃奖励测试脚本
    :param devices:
    :return:
    """
    poco = deviceconnect(devices)
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
                printgreen("活跃奖励界面UI元素显示正常")
            else:
                printred("活跃奖励UI元素显示异常，详情见截图")
                get_screen_shot(start, time.time(), devices, "活跃奖励UI元素显示异常")
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
                    printgreen("活跃奖励模块所有按钮点击正常")
            except Exception as e:
                printred("活跃奖励界面按钮点击流程异常")
                printred(e)
                get_screen_shot(start, time.time(), devices, "活跃奖励界面按钮点击流程异常")
        try:
            with poco.freeze() as freeze_poco:
                count = int(0)
                for i in freeze_poco("DailyActivityDlg(Clone)").offspring("RightView").offspring("Icon"):
                    item = i.parent().get_name()
                    # move(poco,item,devices)
                    name = freeze_poco("DailyActivityDlg(Clone)").offspring("RightView").child(item)\
                        .offspring("Name").get_text()
                    if freeze_poco("DailyActivityDlg(Clone)").offspring("RightView").child(item).child("Go").exists():
                        if name == "兢兢业业":
                            print(f"【{name}】日常任务不点击前往")
                        else:
                            poco("DailyActivityDlg(Clone)").offspring("RightView").child(item).child("Go").click()
                            if poco("Close").exists() and (not poco("DailyActivityDlg(Clone)").exists()):
                                poco("Close").click()
                                if poco("DailyActivityDlg(Clone)").exists():
                                    printgreen(f"【{name}】点击前往正常")
                                else:
                                    printred(f"【{name}】点击前往正常异常")
                                    get_screen_shot(start, time.time(), devices, "流程异常")
                                    initial(poco)
                            else:
                                if poco("BuyFrame").exists():
                                    settouch(1, 96, 486, devices, times=2)
                                    if not poco("BuyFrame").exists():
                                        printgreen(f"【{name}】点击前往正常")
                                    else:
                                        settouch(1, 96, 486, devices, times=2)
                    else:
                        print(f"【{name}】的任务已经完成")
                    count += 1
                    if count == 3:
                        break
        except Exception as e:
            printred("活跃奖励界面前往按钮点击流程异常")
            printred(e)
            get_screen_shot(start, time.time(), devices, "活跃奖励界面前往按钮点击流程异常")
    else:
        printred("活跃奖励界面报错，详情见截图")
        get_screen_shot(start, time.time(), devices, "活跃奖励界面报错")
    return poco(texture="zbx_00").get_name()   # 返回值判断脚本是否执行成功


def move(poco,item,devices):
    for i in range(20):
        position = poco("DailyActivityDlg(Clone)").offspring("RightView").child(item).get_position()
        if position[1] < 0.34:
            setswipe(1, (550, 280), (550, 540), devices)
            time.sleep(1)
        elif position[1] > 0.8:
            setswipe(1, (550, 540), (550, 280), devices)
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


if __name__ == "__main__":
    start = time.localtime()
    active(start, "9b57691d")