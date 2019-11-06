"""
变强模块
"""

# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from multi_processframe.ProjectTools import common,common
from multi_processframe.ProjectTools import common
from poco.exceptions import InvalidOperationException


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

    for i in range(10):
        but = butpos.get_position()
        if but[1] < pos1:
            if i < 4 and i > 2:
                common.setswipe(1, [high, low], [high, lows], devices)
            else:
                common.setswipe(1, [high, lows], [high, low], devices)

        elif but[1] > pos2:
            if i < 4 and i > 2:
                common.setswipe(1, [high, lows], [high, low], devices)
            else:
                common.setswipe(1, [high, low], [high, lows], devices)
        else:
            break



def Intensify(devices):  # 主界面点击变强按钮
    """
    主界面点击变强按钮
    :return:
    """
    poco = common.deviceconnect(devices)
    if poco("SysIBq").exists():
        poco("SysIBq").click()  # 主界面变强按钮
    else:
     common.printred("主界面没有找到变强按钮")
    for item in range(len(poco("scroll").child())):
        item1 = "item"+str(item)
        pos = poco("FpStrengthenDlg(Clone)").offspring(item1)  # 获取当前控件
        if pos.exists():
            butpos(devices,butpos=pos, pos1=0.32,pos2=0.81,high=158, low=544, lows=290)  # 调用butpos方法
            common.printgreen("进入" + poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("TextLabel").get_text() + "功能，开始检查子页签")
            pos.click()  # 点击变强子按钮

        else:
            common.printred("没有找到" + poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("TextLabel").get_text() + "按钮，请检查..")
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        for item2 in range(len(freeze_poco("Panel").child())):  # 获取子页签的按钮
            item2 = "item" + str(item2)
            if freeze_poco("FpStrengthenDlg(Clone)").offspring(item2).child("Strengthen").child("TittleLab").exists():
                pos = freeze_poco("FpStrengthenDlg(Clone)").offspring(item2).child("Strengthen").child("TittleLab")
                # butpos(butpos=pos,pos1=0.33,pos2=0.85,high=1330,low=930,lows=482)  # 调用butpos方法
            elif freeze_poco("FpStrengthenDlg(Clone)").offspring(item2).child("Other").child("Label").exists():
                pos = freeze_poco("FpStrengthenDlg(Clone)").offspring(item2).child("Other").child("Label")
                # butpos(butpos=pos, pos1=0.33, pos2=0.85, high=1330, low=930, lows=482)  # 调用butpos方法
            if pos.exists():
                common.printgreen(freeze_poco("FpStrengthenDlg(Clone)").offspring(f"{item1}").offspring("TextLabel").get_text() + "-->>" + pos.get_text() + "-->>显示成功")
            else:
                common.printred("无法获取" + poco("FpStrengthenDlg(Clone)").offspring(f"{item1}").offspring("TextLabel").get_text() + f"选项第{item}个子页签。赶紧检查..")
    return pos.get_text()  # 变强功能最后一个检查点--对应的活跃度宝箱打开随机获得水晶显示成功
