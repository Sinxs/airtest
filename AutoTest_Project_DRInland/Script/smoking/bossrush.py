"""
bossrush模块，有次数就先判断元素在进去然后出来，没有次数就直接判断界面元素
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from airtest.core.api import *
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


def bossrush(start, devices):
    poco = common.deviceconnect(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        common.printgreen("主界面缺少日常按钮，请检查...")
        common.get_screen_shot(start, time.time(), devices, "主界面缺少日常按钮")
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item48")\
        .offspring("Background")  # bossrush参加按钮
    if pos.exists():
        butpos(devices,butpos=pos, pos1=0.4, pos2=0.79, high=565, low=511, lows=240)  # 调用butpos方法
        pos.click()  # 点击bossrush参加按钮
    else:
        common.printgreen("日常界面没有bossrush选项，请检查...")
        common.get_screen_shot(start, time.time(), devices, "日常界面没有bossrush选项")
    if poco(texture="l_frame_00").exists():
        common.printgreen("出现幸运盒子，很幸运。。。现在把幸运盒子的弹窗点掉")
        poco("OK").click()
    if poco("BossRushNewDlg(Clone)").child("Bg").child("Boss").exists():
        common.printgreen("成功进入bossrush界面。开始检测界面元素")
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        common.printgreen("检查点 " + freeze_poco("BossRushNewDlg(Clone)").offspring("left").child("RemainTime")
                          .get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco("BossRushNewDlg(Clone)").offspring("left").child("Name")
                          .get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco(text="攻击").get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco(text="防御").get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco(text="生命").get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco(texture="kz_nk2").child("SkillName").get_text() + " 显示正确")
        if poco("SweepButton").exists():  # 仅判断没有开会员的状态
            common.printgreen("开始判断扫荡控件，仅判断没有开会员的状态")
            poco("SweepButton").click()
            if poco(texture="l_frame_00").exists():  # 提示开会员的弹窗
                common.printgreen("扫荡控件，功能正确")
                poco(text="取消").click()  # 取消扫荡提示框
            else:
                common.printred("扫荡功能没有弹出提示框，请检查.....")
                common.get_screen_shot(start, time.time(), devices, "扫荡功能没有弹出提示框")
        if int(freeze_poco("BossRushNewDlg(Clone)").child("Num").get_text()[-3]) == 0:  # 判断今日进入次数
            common.printgreen("没有次数了，不能刷新, 要不明天在打吧！！！")
            return poco(text="今日剩余通关次数：").get_text()
        elif int(freeze_poco("BossRushNewDlg(Clone)").child("Num").get_text()[-3]) != 0:  # 判断今日进入次数
            common.printgreen("今天的次数还没有用，现在开始点击刷新")
            poco("Refresh").click()  # 点击刷新按钮
            if poco(texture="l_frame_00").exists():
                common.printgreen("点击刷新后出现幸运盒子，很幸运。。。现在把幸运盒子的弹窗点掉")
                poco("OK").click()
            common.printgreen("点击刷新按钮，没啥效果，特效我又看不出来。。。但是可以拿到结果")
            common.printgreen("现在的bossrush更换为了  " + poco("BossRushNewDlg(Clone)").offspring("left")
                              .child("Name").get_text())
    else:
        common.printgreen("检测到没有进入bossrush界面，请检查...")
        common.get_screen_shot(start, time.time(), devices, "检测到没有进入bossrush界面")
    return poco("BossRushNewDlg(Clone)").offspring("right").child("T2").get_text()  # 本次挑战增益


if __name__ == "__main__":
    start = time.localtime()
    bossrush(start, "3150a7eb")
