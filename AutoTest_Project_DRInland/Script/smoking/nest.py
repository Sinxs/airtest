"""
巢穴模块测试
巢穴排行榜
巢穴奖励
通关巢穴
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from airtest.core.api import *
from multi_processframe.ProjectTools import initial
from multi_processframe.ProjectTools import common


def butpos(devices,butpos,pos1=0.4,pos2=0.81,high=1330,low=930,lows=482):
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
            common.setswipe(1, [high, lows], [high, low], devices)
        elif but[1] > pos2:
            common.setswipe(1, [high, low], [high, lows], devices)
        else:
            break


def nest(start, devices):
    poco = common.deviceconnect(devices)

    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        common.printgreen("主界面缺少日常按钮，请检查...")
        common.get_screen_shot(start, time.time(), devices, "主界面缺少日常按钮")
    if poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item110")\
            .offspring("Background").exists():
        # 副本参加按钮
        pos = (poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item110")
               .offspring("Background"))
        butpos(devices, butpos=pos, pos1=0.4, pos2=0.79, high=565, low=511, lows=240)  # 调用butpos方法
        # 点击副本参加按钮
        poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item110").\
            offspring("Background").click()
        sleep(2)
        poco("Hard").click()  # 点击巢穴按钮
        sleep(4)
    else:
        common.printgreen("副本界面控件缺失，请检查...")
        common.get_screen_shot(start, time.time(), devices, "副本界面控件缺失")

    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("Label").exists() and freeze_poco(texture="l_frame_09").exists() and \
            freeze_poco("Btn2").exists() and freeze_poco("Btn1").exists() and \
            freeze_poco("Member").exists() and  freeze_poco("Level").exists() and \
            freeze_poco("PPT").exists() and freeze_poco("MyPPT").exists():
        common.printgreen("检查点 " + freeze_poco("Member").offspring("T").get_text() + "  显示正确")
        common.printgreen("检查点 " + freeze_poco("Level").offspring("T").get_text() + "  显示正确")
        common.printgreen("检查点 " + freeze_poco("PPT").offspring("T").get_text() + "  显示正确")
        common.printgreen("检查点 " + freeze_poco("MyPPT").offspring("T").get_text() + "  显示正确")
        common.printgreen("检查点 " + freeze_poco("Btn2").offspring("T").get_text() + "  显示正确")
        common.printgreen("检查点 " + freeze_poco("Btn1").offspring("T").get_text() + "  显示正确")
    else:
        common.printred("巢穴界面控件缺失，请检查...")
        common.get_screen_shot(start, time.time(), devices, "巢穴界面控件缺失")
    poco("Btn2").click()  # 点击排行榜
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("Tittle").exists() and freeze_poco("T1").exists() and freeze_poco("T2").exists() and \
            freeze_poco("T3").exists() and freeze_poco("T4").exists():
        common.printgreen("检查点 " + freeze_poco("T3").get_text() + "  显示正确")
        common.printgreen("检查点 " + freeze_poco("Tittle").get_text() + "  显示正确")
        common.printgreen("检查点 " + freeze_poco("T2").get_text() + "  显示正确")
        common.printgreen("检查点 " + freeze_poco("T4").get_text() + "  显示正确")
        common.printgreen("检查点 " + freeze_poco("T1").get_text() + "  显示正确")
        poco(texture="l_close_00").click()  # 点击返回巢穴界面
    else:
        common.printgreen("排行榜界面控件缺失，请检查...")
        common.get_screen_shot(start, time.time(), devices, "排行榜界面控件缺失")
    poco("Btn1").click()  # 点击奖励
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("Tittle").exists():
        common.printgreen("进入奖励预览界面")
        for item in range(len(freeze_poco("List").child())):
            item = str(item)
            common.printgreen("检查点 " + freeze_poco("NestStarReward").offspring(item)
                              .offspring("T").get_text() + "  显示正确")
        poco(texture="l_close_00").click()  # 点击返回到巢穴界面
    else:
        common.printgreen("奖励界面控件缺失，请检查...")
        common.get_screen_shot(start, time.time(), devices, "奖励界面控件缺失")
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    for item in range(len(freeze_poco("ItemList").child())-1):
        item = "item"+str(item)
        if freeze_poco("TheExpDlg(Clone)").offspring(item).exists():
            freeze_poco("TheExpDlg(Clone)").offspring(item).click()
            freeze_poco("TheExpDlg(Clone)").offspring(item).click()
        if poco("main").exists():
            freeze_poco("TheExpDlg(Clone)").offspring(item).click()
    # for i in range(20):
    #     if poco("Left").exists():
    #         freeze_poco("Left").click()  # 点击下一个页签
    #         freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    #         for item in range(len(freeze_poco("ItemList").child()) - 1):
    #             item = "item" + str(item)
    #             if freeze_poco("TheExpDlg(Clone)").offspring(item).exists():
    #                 freeze_poco("TheExpDlg(Clone)").offspring(item).click()
    #                 freeze_poco("TheExpDlg(Clone)").offspring(item).click()
    #             if poco("main").exists():
    #                 freeze_poco("TheExpDlg(Clone)").offspring(item).click()
    #     else:
    #         break
    if poco("Diff4").exists():
        poco("Diff4").click()  # 点击地狱模式
        if poco("Do").exists():
            poco("Do").click()  # 点击进入游戏
            if poco(texture="l_frame_00").exists():
                common.printgreen("提示战力不足，建议提升战力")
                common.get_screen_shot(start, time.time(), devices, "提示战力不足")
                poco(text="强行闯关").click()
                # 进入队伍界面
            if poco("BtnCreate").exists():
                poco("Close").click()  # 点击返回
                if poco("BtnCreate").exists():
                    poco("Close").click()  # 点击返回
        return poco("Btn1").child("T").get_text()  # 查看奖励
    else:
        common.printgreen("巢穴界面地狱选项控件缺失，请检查...")
        common.get_screen_shot(start, time.time(), devices, "地狱选项控件缺失")
                # if poco("BtnCreate").exists():
                #     common.printgreen("没有队伍，开始创建队伍")
                #     poco("BtnCreate").click()
                #
                # if poco("BtnStart").exists():
                #     common.printgreen("队伍已经创建，开始进入战斗")
                #     poco("BtnStart").click()  # 点击进入战斗
                #     sleep(40)
                #     if poco("Indicate").child("Bg").exists() and poco("BtnDamageStatistics").exists():
                #         common.printgreen("进入巢穴，因为没有自动战斗，结束战斗....")
                #         if poco("Pause").exists():
                #             poco("Pause").click()  # 准备退出副本
                #             poco("Leave").click()  # 点击退出副本
                #         sleep(20)
                #         if poco("Title").exists():
                #             common.printgreen("已经跑完巢穴模块，回到主界面，脚本完成...开始离开队伍")
                #             if poco("BtnLeave").exists():
                #                 poco("BtnLeave").click()  # 点击退出组队
                #                 if poco("BtnCreate").exists():
                #                     common.printgreen("已经离开队伍")
                # else:
                #     common.printred("没有回到主界面，脚本未完成")
                #     common.get_screen_shot(start, time.time(), devices, "没有回到主界面")
        # else:
        #     common.printgreen("巢穴界面地狱选项控件缺失，请检查...")
        #     common.get_screen_shot(start, time.time(), devices, "地狱选项控件缺失")
    # finally:
    #     common.printgreen("验证队伍是否真的离开。。。")
    #     initial.startgame(devices)
    #     if poco("Team").child("Selected").exists():
    #         poco("Team").child("Selected").click()  # 点击队伍
    #         poco("Team").click()  # 点击创建队伍
    #         if poco("BtnLeave").exists():
    #             poco("BtnLeave").click()  # 点击退出组队
    #             if poco("BtnCreate").exists():
    #                 common.printgreen("已经离开队伍")
    #         else:
    #             common.printgreen("已经离开队伍")
    # return poco("Title").get_text()


if __name__ == "__main__":
    start = time.localtime()
    nest(start, "e37c0280")