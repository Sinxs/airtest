# -*- encoding=utf8 -*-
__author__ = "Lee.li"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from poco.exceptions import PocoNoSuchNodeException
import time


def EnterEctype(conut_time,poco): # 进入主线深渊
    """
    1.这是一个主线深渊副本初始化函数
    2.每次都会进入主界面，然后在进入深渊副本
    """
    # InitialGame.Startgame() # 初始化游戏
    poco("Duck").click() # 进入日常
    poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item111").child("JoinBtn").click() # 进入主线副本
    poco("DungeonSelect(Clone)").offspring("Normal").child(texture="ICON-XT-gkzx2").click() # 点击主线
    for i in range(conut_time):
        poco("DungeonSelect(Clone)").offspring("Bg").child("Left").click()

def Wartime(ob_level,poco): # 判断战场内的时间，如果在给定时间内完成战斗算正常，超过5分钟算关卡异常
    if poco("WarTime").exists():
        with poco.freeze() as frozen_poco:
            try:
                for item in frozen_poco("WarTime"):
                    wartime = item.get_text()
            except PocoNoSuchNodeException:
                wartime = (0,1)
        for i in range(1):
            if 4 > int(wartime[1]) >= 3:  # 获取战场时间 大于2的时候就要判断是不是卡点了
                swipe([486.0, 1026.0], [243.0, 1026.0], duration=3)  # 左下移动3秒
                swipe([243.0, 1026.0], [486.0, 1026.0], duration=3)  # 右方移动3秒
            elif int(wartime[1]) > 5:
                print(f"{ob_level}关卡异常")
                poco("Pause").click()  # 点击设置
                time.sleep(1)
                poco("Leave").click()  # 点击退出副本
                break

def Skip_Plot(poco):
    """
    1.跳过动画
    2.跳过对话
    3.动画和对白都不存在直接跳过
    """
    if  poco("Pause").exists():
        if not poco("Pause").wait(5).exists():
            if poco("DownBG").exists(): # 判断
                touch([1140,540],times=2)
                if poco("Skip").exists():
                    poco("Skip").click()
            for i in range(15):
                if poco("TalkTextBg").exists():
                    touch([1140,540],times=10)
                else:
                    break
    else:
        if poco("DownBG").exists(): # 判断
            touch([1140,540],times=2)
            if poco("Skip").exists():
                poco("Skip").click()
        for i in range(15):
            if poco("TalkTextBg").exists():
                touch([1140,540],times=10)
            else:
                break
    
def Verdict_AutoPlay(ob_level,poco): # 判断自动战斗按钮是否存在
    """
    判断自动战斗是否开启
    """
    if poco("AutoPlayCancel").exists():
        print("自动战斗中...")
        return None
    elif poco("AutoPlay").exists():
        touch([168,150],times=1)
        print("----------开启自动战斗----------")
        return None
    elif not poco("AutoPlayContent").exists():
        if poco("Pause").exists():
            print(f"关卡{ob_level}没有自动战斗功能，执行副本跳过步棸！！！")
            poco("Pause").click()  # 点击设置
            time.sleep(1)
            poco("Leave").click()  # 点击退出副本

def Complete_Map(action,poco): # 跑图功能
    """
    参数action--需要移动N次才能到达指定章节
    主线第一章执行脚本
    1.获取关卡数
    2.循环找到关卡
    3.进入战斗
    4.判断对白和自动战斗
    5.战斗判断--->获取战斗时间（3分钟之内算没结束战斗，移动角色，5分钟之内未结束战斗算关卡异常）
    :param action:
    :return:
    """
    EnterEctype(action,poco) # 进入副本的函数
    chapter = "chapter" + str(10 - action)
    levels = poco("DungeonSelect(Clone)").offspring(chapter).offspring("Levels").child() # 获取当前关卡数量
    for number in range(1,(len(levels)+1)): # 循环遍历执行关卡通关
        if action >= 1:
            top = 10 - action
            level = str(top) + "0" + str(4)
        else:
            level = "1100" + str(number)

        poco("DungeonSelect(Clone)").offspring(chapter).offspring(level).child("SprBtn").click() # 循环找到关卡
        poco("DungeonSelect(Clone)").offspring("DetailFrame").offspring("Bg").child("GoBattle").click() # 点击战斗按钮
        print(f'----------------开始{level}关卡战斗流程----------------')
        if poco("LoadingProgress").exists():
            time.sleep(5)
            if poco("DownBG").wait(3) or poco("TalkTextBg").wait(3):
                Skip_Plot(poco) # 跳过剧情和对白
            if poco("Pause").exists():
                Verdict_AutoPlay(level, poco)
        for i in range(100):
            if poco("DownBG").exists() or poco("TalkTextBg").exists(): # 判断动画和对白存在的话
                Skip_Plot(poco) # 跳过剧情和对白
            if i ==25 and poco("WarTime").exists():
                Wartime(level,poco) # 判断战斗时间
            if poco("LevelRewardGerenalFrame").child("Bg").offspring("Time").exists(): # 判断通关时间
                print(poco("Time").get_text()) # 获取打印通关时间，有可能获取不到
                try:
                    if poco("Duck").wait_for_appearance(15):
                        print(f"关卡通关回到主界面，{level}关卡流程正常，地图没有卡点!")
                        break
                except:
                     if poco("Duck").exists():  # 如果没有获取到通关时间的话，直接检测日常界面是否存在
                        print(f"关卡通关回到主界面，{level}关卡流程正常，地图没有卡点!")
                        break
                # if not poco("Duck").exists(): # 查找日常控件，找不到等3秒
                #     time.sleep(2)
                #     if poco("Duck").exists(): # 找到日常控件，算流程正常，打印关卡信息
                #         print(f"关卡通关回到主界面，{level}关卡流程正常，地图没有卡点!")
            #            break
            if poco("Duck").exists(): # 如果没有获取到通关时间的话，直接检测日常界面是否存在
                print(f"关卡通关回到主界面，{level}关卡流程正常，地图没有卡点!")
                break
        # time.sleep(2) # 等待两秒
        if number == len(levels):
            print(f"此章节一共{number}关，已经全部通关....")
            break
        else:
            EnterEctype(action,poco) # 执行下一个关卡


def test_Chapter_One(devices):
    """ 主线第一章
    :return:Complete_Map（）参数表示移动多少次可以到达指定章节
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Complete_Map(9,poco)
    return poco("Duck").get_name()

#
# devices = '127.0.0.1:62001'
# test_Chapter_One(devices)

def test_Chapter_Two(devices):
    """ 主线第二章
    :return:Complete_Map（）参数表示移动多少次可以到达指定章节
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Complete_Map(8,poco)
    return poco("Duck").get_name()


def test_Chapter_Three(devices):
    """ 主线第三章
    :return:Complete_Map（）参数表示移动多少次可以到达指定章节
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Complete_Map(7,poco)
    return poco("Duck").get_name()


def test_Chapter_four(devices):
    """ 主线第四章
    :return:Complete_Map（）参数表示移动多少次可以到达指定章节
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Complete_Map(6,poco)
    return poco("Duck").get_name()

def test_Chapter_Five(devices):
    """ 主线第五章
    :return:Complete_Map（）参数表示移动多少次可以到达指定章节
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Complete_Map(5,poco)
    return poco("Duck").get_name()

def test_Chapter_Six(devices):
    """ 主线第六章
    :return:Complete_Map（）参数表示移动多少次可以到达指定章节
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Complete_Map(4,poco)
    return poco("Duck").get_name()

def test_Chapter_Seven(devices):
    """ 主线第七章
    :return:Complete_Map（）参数表示移动多少次可以到达指定章节
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Complete_Map(3,poco)
    return poco("Duck").get_name()

def test_Chapter_Eight(devices):
    """ 主线第八章
    :return:Complete_Map（）参数表示移动多少次可以到达指定章节
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Complete_Map(2,poco)
    return poco("Duck").get_name()

def test_Chapter_Nine(devices):
    """ 主线第九章
    :return:Complete_Map（）参数表示移动多少次可以到达指定章节
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Complete_Map(1,poco)
    return poco("Duck").get_name()

def test_Chapter_Ten(devices):
    """ 主线第十章
    :return:Complete_Map（）参数表示移动多少次可以到达指定章节
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    Complete_Map(0,poco)
    return poco("Duck").get_name()