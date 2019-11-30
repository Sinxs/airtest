"""
黑暗神殿模块自动化脚本
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


def darkness_ectype(start, devices):
    poco = common.deviceconnect(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        common.printgreen("主界面缺少日常按钮，请检查...")
        common.get_screen_shot(start, time.time(), devices, "主界面缺少日常按钮")
    # 黑暗神殿参加按钮
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item530").offspring("Background")
    if pos.exists():
        butpos(devices,butpos=pos, pos1=0.4, pos2=0.79, high=565, low=511, lows=240)  # 调用butpos方法
        pos.click()  # 点击黑暗神殿参加按钮
    else:
        common.printgreen("日常界面没有黑暗神殿选项，请检查...")
        common.get_screen_shot(start, time.time(), devices, "日常界面没有黑暗神殿选项")
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("GoBattle").exists() and \
            freeze_poco("SweepBtn").exists() and \
            freeze_poco("Reward").exists() and \
            freeze_poco("Stage").exists() and \
            freeze_poco("Stagepanel").exists():
        freeze_poco("Help").click()  # 点击小问号
        if poco("Di").wait().exists():
            poco("Btn").click()
    else:
        print("黑暗神殿界面缺少控件")
        common.get_screen_shot(start, time.time(), devices, "排行榜界面显示错误")
    if poco("Title").exists():  # 排行榜
        poco("Rank").click()
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("1").exists() and \
                freeze_poco("2").exists() and \
                freeze_poco("3").exists() and \
                freeze_poco("4").exists() and \
                freeze_poco("5").exists():
            for i in range(1, 20):
                if freeze_poco(str(i)).child("Label").exists():
                    common.printgreen("检查点 " + freeze_poco(str(i)).child("Label").get_text() + " 显示正确")
            common.printgreen("排行榜首界面显示正确，详细内容不做判断，如果需要，后期优化")
            poco("RankDlg(Clone)").offspring("TabList").offspring("2").child("Bg").click()  # 点击PVE排行，避免影响其他脚本
            poco("Close").click()
        else:
            common.printred("排行榜界面显示错误，请检查....")
            common.get_screen_shot(start, time.time(), devices, "排行榜界面显示错误")
    if poco("FirstBlood").exists():  # 首通奖励
        poco("FirstBlood").click()
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("TeamTowerNewRankreward(Clone)").offspring("item0").exists() and \
                freeze_poco("TeamTowerNewRankreward(Clone)").offspring("item1").exists() and \
                freeze_poco("TeamTowerNewRankreward(Clone)").offspring("item2").exists() and \
                freeze_poco("TeamTowerNewRankreward(Clone)").offspring("item3").exists() and \
                freeze_poco("TeamTowerNewRankreward(Clone)").offspring("item4").exists():
            common.printgreen("首通奖励显示正确...")
            # 关闭当前页签
            poco(texture="l_close_00").click()
            if not poco(texture="l_close_00").exists():
                pass
            else:
                poco(texture="l_close_00").click()
        else:
            common.printred("层数奖励显示错误，请检查.....")
            common.get_screen_shot(start, time.time(), devices, "层数奖励显示错误")
    return poco("FirstBlood").child("Name").get_text()  # 层数奖励


if __name__ == "__main__":
    start = time.localtime()
    darkness_ectype(start, "e37c0280")

