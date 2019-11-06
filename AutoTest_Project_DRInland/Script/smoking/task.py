"""
任务模块自动化脚本
《脚本环境》
1、角色已经接了一个或多个任务
2、角色已经加入公会
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from airtest.core.api import *
from multi_processframe.ProjectTools import common


def butpos(devices, butpos, pos1=0.4, pos2=0.81, high=1330, low=930, lows=482):
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


def task(start,devices):
    poco = common.deviceconnect(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        common.printgreen("主界面缺少日常按钮，请检查...")
        common.get_screen_shot(start,time.time(), devices, "主界面缺少日常按钮")
    # 任务参加按钮
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item886").child("JoinBtn")
    if pos.exists():
        butpos(devices,butpos=pos, pos1=0.4, pos2=0.79, high=565, low=511, lows=240)  # 调用butpos方法
        pos.click()  # 点击日常任务参加按钮
    else:
        common.printgreen("日常界面没有日常任务选项，请检查...")
        common.get_screen_shot(start,time.time(), devices, "日常界面没有日常任务选项")
    if not poco(texture="l_tip_00").exists():
        common.printgreen("还未接取任务，开始接任务")
        poco("TalkTextBg").child("Bg").wait_for_appearance()
        for i in range(5):
            if poco("TalkTextBg").child("Bg").wait(30).exists():  # 如果弹出了任务弹窗
                poco("VirtualTab").click()  # 点击下一步
                if poco("BtnOK").exists():  # 如果出现了接受按钮
                    common.printgreen("接受任务")
                    poco("BtnOK").click()  # 点击接受
                    break
    if poco(texture="l_tip_00").exists():
        common.printgreen("已经接了任务，开始检测任务模块控件")
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        # 检测任务模块控件
        if freeze_poco(texture="DailyTaskText").exists() and \
                freeze_poco("BaseInfo").exists() and \
                freeze_poco("item0").exists() and \
                freeze_poco("item1").exists() and \
                freeze_poco("item2").exists() and \
                freeze_poco("item3").exists() and \
                freeze_poco("Submmit").exists() and \
                freeze_poco("Refresh").exists() and \
                freeze_poco("GuildDailyTask(Clone)").child("Bg")[0].child("T")[0].exists() and \
                freeze_poco("RefreshLogBtn").exists():
            common.printgreen("任务窗口检测各个按钮，控件，奖励 完成")
            if poco("Refresh").exists():  # 点击刷新
                common.printgreen("点击任务刷新按钮，检测任务刷新界面中的元素控件")
                poco("Refresh").click()
                sleep(2)
                freeze_poco = poco.freeze()  # TODO：定义冻结poco
                if freeze_poco("DailyTaskInviteDlg(Clone)").offspring("TaskLevel").exists() and \
                        freeze_poco("TabTpl0").exists() and \
                        freeze_poco("TabTpl1").exists() and \
                        freeze_poco("DailyTaskInviteDlg(Clone)").offspring("Tab0Text").child("T")[0].exists() and \
                        freeze_poco("DailyTaskInviteDlg(Clone)").offspring("Tab0Text").child("T")[1].exists() and \
                        freeze_poco("DailyTaskInviteDlg(Clone)").offspring("Tab0Text").child("T")[2].exists():
                    common.printgreen("刷新任务窗口检测各个按钮，控件，奖励 完成")
                    poco("DailyTaskInviteDlg(Clone)").offspring("Close").click()  # 点击返回
                else:
                    common.printred("任务刷新按钮界面缺少控件元素，请检查。。。")
                    common.get_screen_shot(start,time.time(), devices, "任务刷新按钮界面缺少控件元素")
            else:
                common.printred("界面没有任务刷新按钮，请检查。。。")
                common.get_screen_shot(start,time.time(), devices, "界面没有任务刷新按钮")
            if poco(text="已求助").exists():
                common.printgreen("界面没有求助按钮，已经求助过了")
            elif poco(text="求助").exists():  # 如果界面有求助的话，点击求助按钮
                common.printgreen("开始点击求助按钮")
                pos = poco(text="求助")
                butpos(devices,butpos=pos, pos1=0.29, pos2=0.73, high=1055, low=740, lows=466)  # 调用butpos方法
                poco(text="求助").click()
                common.printgreen("点击求助完成")

            else:
                common.printgreen("界面没有求助按钮，也没有已求助按钮，所以为确保产品质量，建议手动测试一次")
                common.get_screen_shot(start, time.time(), devices, "界面没有求助按钮")
            if poco("RefreshLogBtn").exists():
                poco("RefreshLogBtn").click()
                freeze_poco = poco.freeze()  # TODO：定义冻结poco
                if freeze_poco("LogPanel").child("T").exists():
                    common.printgreen("开始检查任务刷新界面的控件元素")
                    common.printgreen("检查点  " + freeze_poco("LogPanel").offspring("Title").child("T")[0]
                                      .get_text() + "  显示正确")
                    common.printgreen("检查点  " + freeze_poco("LogPanel").offspring("Title").child("T")[1]
                                      .get_text() + "  显示正确")
                    common.printgreen("检查点  " + freeze_poco("LogPanel").offspring("Title").child("T")[2]
                                      .get_text() + "  显示正确")
            else:
                common.printgreen("界面没有刷新纪录，请检查")
                common.get_screen_shot(start,time.time(), devices, "界面没有求助按钮")
    return poco("LogPanel").child("T").get_text()  # 返回 任务刷新记录


if __name__ == "__main__":
    start = time.localtime()
    task(start, "e37c0280")


