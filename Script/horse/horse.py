# -*- encoding=utf8 -*-
__author__ = "Lee.li"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco


def test_Horse(devices):
    """
    1.进入主界面
    2.点击坐骑按钮
    3.依次点击坐骑图标，查看坐骑模型是否正常
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    comparepoMenuExists("SysEHorse",poco) # 调用函数查看主界面坐骑按钮是否可点击
    poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
    petgrid = poco("Grid").child() # 获取目前所有坐骑数量
    swipe((486, 170), (486, 889), 4)
    # for i in range(len(petgrid)):
    for i in range(3):
        if i == 22:
            swipe((486,889),(486,170),6)
            swipe((486,889),(486,170),4)# 滑动界面确保未出现在界面内的坐骑可以点击到
            time.sleep(2)
        item = "item" + str(i)
        time.sleep(2)
        poco("Grid").offspring(item).click() # 点击坐骑icon
        if poco("vehicle_crazydugswing_red").exists(): #判断坐骑模型是否存在
            petname = poco("PetName").offspring("Name").get_text() # 获得当前坐骑的名称
            print(f"{petname}坐骑模型显示正常")
        poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
        time.sleep(1)
    return poco("Btnhave").get_name() # 返回值

def comparepoMenuExists(sysmenu,poco):
    position = poco(sysmenu).get_position()
    if position[0] > 1:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco(texture="switch").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()
