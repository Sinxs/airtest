"""
无限幻境模块，有次数就先判断元素,各个控件是否点击
"""

from multi_processframe.Tools import printcolor,adb_connect,screenshot
from airtest.core.api import *

devices = "127.0.0.1:62025"
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


def bossrush(devices):
    poco = adb_connect.device(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
    else:
        printcolor.printgreen("主界面缺少日常按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item927").offspring("Background")  # 无限幻境参加按钮
    if pos.exists():
        butpos(butpos=pos, pos1=0.4, pos2=0.79, high=1055, low=740, lows=466)  # 调用butpos方法
        pos.click()  # 点击无限幻境参加按钮
    else:
        printcolor.printgreen("日常界面没有无限幻境选项，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "日常界面没有无限幻境选项")
    if poco("Title").exists():
        printcolor.printgreen("进入无限幻境界面，开始检测界面控件元素")
        

bossrush(devices)