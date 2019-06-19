"""
龙穴模块测试
1、检查龙穴一级界面和二级界面的控件，并进行点击和关闭操作
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
def UIjudge(poco,num, devices):
    sleep(3)
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("NestName").exists() and freeze_poco("CurPPT").exists() and \
            freeze_poco("SugPPT").exists() and freeze_poco("SugAttr").exists() and \
            freeze_poco("SugLevel").exists() and freeze_poco("SugMember").exists():
        printcolor.printgreen("检查点： " + freeze_poco("CurPPT").child("T").get_text() + "  " + freeze_poco("CurPPT").get_text() + "       显示正确")
        printcolor.printgreen("检查点： " + freeze_poco("SugPPT").child("T").get_text() + "  " + freeze_poco("SugPPT").get_text() + "       显示正确")
        printcolor.printgreen("检查点： " + freeze_poco("SugAttr").child("T").get_text() + "  " + freeze_poco("SugAttr").get_text() + "       显示正确")
        printcolor.printgreen("检查点： " + freeze_poco("SugLevel").child("T").get_text() + "  " + freeze_poco("SugLevel").get_text() + "       显示正确")
        printcolor.printgreen( "检查点： " + freeze_poco("SugMember").child("T").get_text() + "  " + freeze_poco("SugMember").get_text() + "       显示正确")
        for item in range(len(freeze_poco("NestFrameNormal").child()) - num):
            item1 = "item" + str(item)
            printcolor.printgreen("检查点 "+freeze_poco("DragonNestDlg(Clone)").offspring("NestFrameNormal").child(item1).child("Name").get_text()+"  显示正确")
        printcolor.printgreen("进行点击奖励icon的操作")
        for item in range(len(freeze_poco("ItemList").child()) - 2):
            item2 = "item" + str(item)
            freeze_poco("DragonNestDlg(Clone)").offspring("ItemList").child(item2).click()
            freeze_poco("DragonNestDlg(Clone)").offspring("ItemList").child(item2).click()
        if poco("ItemToolTipDlg(Clone)").child("Bg").exists():
            poco("DragonNestDlg(Clone)").offspring("ItemList").child(item2).click()  # todo:进行两次判断，避免出现点击不及时的情况
        if poco("ItemToolTipDlg(Clone)").child("Bg").exists():
            poco("DragonNestDlg(Clone)").offspring("ItemList").child(item2).click()
        printcolor.printgreen("奖励icon点击完成，报不报红暂时我就不管了")
        printcolor.printgreen("点击  组队进入")
        poco("Enter").child("Text").click()
        if poco(text="队伍").exists():
            printcolor.printgreen("进入组队界面，开始点击返回按钮")
            poco("Close").click()
            if poco("Enter").exists():
                printcolor.printgreen("返回到龙穴界面")
        else:
            printcolor.printred("点击组队后没有进入组队界面")
            screenshot.get_screen_shot(time.time(), devices, "点击组队后没有进入组队界面")


def longxue(devices):
    poco = adb_connect.device(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        printcolor.printgreen("主界面缺少日常按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    if poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item526").offspring("Background").exists():
        pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item526").offspring("Background")  # 龙穴参加按钮
        butpos(butpos=pos, pos1=0.4, pos2=0.79, high=1055, low=740, lows=466)  # 调用butpos方法
        pos.click()  # 点击副本参加按钮
    else:
        printcolor.printgreen("日常界面没有龙穴选项，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "日常界面没有龙穴选项")
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("Panel").exists() and freeze_poco("NestFrameNormal").exists() and \
            freeze_poco("Enter").exists() and freeze_poco("CurPPT").exists() and \
            freeze_poco("SugAttr").exists() and freeze_poco("SugLevel").exists() and freeze_poco("SugMember").exists():
        printcolor.printgreen("进入龙穴界面\n检查点： 四个巢穴\n检查点： 显示副本界面\n检查点： 进入副本按钮\n检查点： 推荐进入要求\n以上全部显示正确 ")
    else:
        printcolor.printred("龙穴界面缺少控件元素，请检查。。。")
        # screenshot.get_screen_shot(time.time(), devices, "龙穴界面缺少控件元素")
    for item in range(len(poco("Panel").child())):
        item1 = "item" + str(item)
        poco("DragonNestDlg(Clone)").offspring(item1).click()  # 点击各个巢穴
        if poco("ToggleDiffEasy").exists():  # 判断是否有简单选项
            poco("DragonNestDlg(Clone)").offspring(item1).child("Bg").child("Label").get_text()
            printcolor.printgreen("<<<<<<<--进入  "+poco("DragonNestDlg(Clone)").offspring(item1).child("Bg").child("Label").get_text()+"  简单模式-->>>>>>>>")
            poco("ToggleDiffEasy").click()  # 点击简单选项
            UIjudge(poco, 2, devices)  # 调用UIjudge判断当前界面的控件
        else:
            printcolor.printgreen(poco("DragonNestDlg(Clone)").offspring(item1).child("Bg").child("Label").get_text() + "  没有简单模式")
        if poco("ToggleDiffNormal").exists():  # 判断是否有普通选项
            printcolor.printgreen("<<<<<<<--进入  "+poco("DragonNestDlg(Clone)").offspring(item1).child("Bg").child("Label").get_text()+"  普通模式-->>>>>>>>")
            poco("ToggleDiffNormal").click()  # 点击普通选项
            UIjudge(poco, 3, devices)  # 调用UIjudge判断当前界面的控件
        else:
            printcolor.printgreen(poco("DragonNestDlg(Clone)").offspring(item1).child("Bg").child("Label").get_text() + "  没有普通模式")
        if poco("ToggleDiffHard").exists():  # 判断是否有困难选项
            printcolor.printgreen("<<<<<<<--进入  "+poco("DragonNestDlg(Clone)").offspring(item1).child("Bg").child("Label").get_text()+"  困难模式-->>>>>>>>")
            poco("ToggleDiffHard").click()  # 点击困难选项
            UIjudge(poco, 3, devices)  # 调用UIjudge判断当前界面的控件
        else:
            printcolor.printgreen(poco("DragonNestDlg(Clone)").offspring(item1).child("Bg").child("Label").get_text() + "  没有困难模式")
    return poco("NestName").get_text()



