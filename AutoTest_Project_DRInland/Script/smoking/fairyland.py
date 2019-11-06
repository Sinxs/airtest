"""
无限幻境模块，有次数就先判断元素,各个控件是否点击
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


def fairyland(start, devices):
    poco = common.deviceconnect(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        common.printgreen("主界面缺少日常按钮，请检查...")
        common.get_screen_shot(start, time.time(), devices, "主界面缺少日常按钮")
    # 无限幻境参加按钮
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item927").offspring("Background")
    if pos.exists():
        butpos(devices,butpos=pos, pos1=0.4, pos2=0.79, high=565, low=511, lows=240)  # 调用butpos方法
        pos.click()  # 点击无限幻境参加按钮
    else:
        common.printgreen("日常界面没有无限幻境选项，请检查...")
        common.get_screen_shot(start, time.time(), devices, "日常界面没有无限幻境选项")
    if poco("Title").exists():
        common.printgreen("进入无限幻境界面，开始检测界面控件元素")
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("GoBattle").exists() and \
        freeze_poco("BtnRwd").exists() and \
        freeze_poco("BtnIntroduce").exists() and \
        freeze_poco("BtnMemberRank").exists() and \
        freeze_poco("BtnCharacteristic").exists():
        common.printgreen("无限幻境界面按钮存在")
        if poco("Help").exists():
            freeze_poco("Help").click()  # 点击帮助按钮
            if poco("Di").exists():
                poco("Btn").click()  # 关闭帮助按钮
                if poco("Di").exists():
                    poco("Btn").click()  # 如果没有关闭再点击一次
        poco("BtnRwd").click()  # 点击奖励
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("TeamMysteriousDlg(Clone)").offspring("TabsFrame").child("item0").exists() and \
            freeze_poco("TeamMysteriousDlg(Clone)").offspring("TabsFrame").child("item1").exists() and \
            freeze_poco("TeamMysteriousDlg(Clone)").offspring("TabsFrame").child("item2").exists():  # 判断奖励界面
            freeze_poco("TeamMysteriousDlg(Clone)").offspring("TabsFrame").child("item0").click()  # 遍历奖励子页签
            freeze_poco("TeamMysteriousDlg(Clone)").offspring("TabsFrame").child("item1").click()
            freeze_poco("TeamMysteriousDlg(Clone)").offspring("TabsFrame").child("item2").click()
            freeze_poco(texture="l_close_00").click()
            # 上个界面关掉后
            if not freeze_poco("TeamMysteriousDlg(Clone)").offspring("TabsFrame").child("item0").exists():
                poco("BtnIntroduce").click()  # 点击词缀图鉴
                if poco("ScrollView").exists():
                    poco(texture="l_close_00").click()
            if not poco("ScrollView").exists():  # 上个界面关掉后
                poco("BtnMemberRank").click()  # 点击成员排名
                if poco("Label").exists():
                    poco(texture="l_close_00").click()
            if not poco("Label").exists():
                poco("BtnCharacteristic").click()  # 点击关卡特性
                if poco("Label").exists():
                    poco(texture="l_close_00").click()
    # else:
    #     common.printred("无限幻境界面缺少按钮控件")
    #     common.get_screen_shot(start, time.time(), devices, "无限幻境界面缺少按钮控件")
    return poco("T1").get_text()  # 组队挑战


if __name__ == "__main__":
    start = time.localtime()
    fairyland(start, "e37c0280")
