# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
# if not cli_setup():
#     auto_setup(__file__, logdir=True, devices=[
#             "Android://172.16.132.162:7555/172.16.134.202:7555/172.16.132.139:5555?cap_method=JAVACAP&&ori_method=ADBORI",
#     ])

import InitialGame  # 重置测试环境模块
import LogNew
# script content
print("start...")

# import Startgame  # 启动游戏脚本

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


def Intensify():  # 主界面点击变强按钮
    """
    主界面点击变强按钮
    :return:
    """
    if poco(texture="hall_icon_27").exists():
        poco(texture="hall_icon_27").click()  # 主界面变强按钮
    else:
        LogNew.log("主界面没有找到变强按钮")
def test_Intensify():  # 点击变强内子页签
    """我要变强中的页签...时装...金币...龙币..."""
    # InitialGame.Startgame()  # 运行启动游戏脚本，检查游戏是否在运行中
    poco = UnityPoco()
    Intensify()
    for item in range(len(poco("scroll").child())):  # 辨别出当前控件下的子控件的数量，然后循环点击当前控件
        item2 = "item" + str(item)
        if item == 4:  # 颠倒
            swipe((350, 780), (350, 460), 3)
            swipe((350, 780), (350, 460), 3)
        else:
            poco("FpStrengthenDlg(Clone)").offspring(item2).offspring("TextLabel").click()
            LogNew.log("点击" + poco("FpStrengthenDlg(Clone)").offspring(item2).offspring("TextLabel").get_text() + "按钮测试完成")
            print("点击" + poco("FpStrengthenDlg(Clone)").offspring(item2).offspring("TextLabel").get_text() + "按钮测试完成")
    return poco("Label").get_text()

def test_NameIntensify():  # 点击变强、我要变强内的前往按钮
    """
    1、进入主界面
    2、点击变强按钮
    3、依次点击变强页签内的子按钮，并进行详细判断
    4、签到活动是自动弹出的，在进入游戏有需要进行判断-----不需要做，在初始化运行环境中已经做了判断
    """
    InitialGame.Startgame()  # 运行启动游戏脚本，检查游戏是否在运行中
    poco = UnityPoco()
    Intensify()
    """
       1、在主界面点击变强
       2、依次点击变强界面的UI控件
    """

    for item in range(len(poco("Panel").child())):  #
        item1 = "item" + str(item)
        for i in range(5):
            sysmenu = poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("T")
            position = sysmenu.get_position()
            if position[1] > 0.85:  # 对比pos点，得到的pos列表中，第二个元素 > 0.85 说明在屏幕外面
                swipe((1098, 870), (1098, 429), 4)
                time.sleep(1)
            elif position[1] < 0.38:
                swipe((1098, 429), (1098, 870), 4)
                time.sleep(1)
            else:
                pass
        sysmenu.click()
        poco("Close").click()
        LogNew.log("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("TittleLab").get_text() + "前往测试完成")
        print("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child( "TittleLab").get_text() + "前往测试完成")
    return poco("Label").get_text()

def test_ITofashion():  # 我要时装按钮测试
    InitialGame.Startgame()  # 运行启动游戏脚本，检查游戏是否在运行中
    poco = UnityPoco()
    Intensify()

    if poco("FpStrengthenDlg(Clone)").offspring("item2").offspring("TextLabel").exists():
        poco("FpStrengthenDlg(Clone)").offspring("item2").offspring("TextLabel").click()  # 点击变强中的“我要时装按”按钮，然后点击我要时装页签的所有子页签
    else:
        LogNew.log("ERROR: 我要变强按钮没有找到")
    for item in range(len(poco("Panel").child())):  #
        item1 = "item" + str(item)
        for i in range(5):
            sysmenu = poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("T")
            position = sysmenu.get_position()
            if position[1] > 0.85:  # 对比pos点，得到的pos列表中，第二个元素 > 0.85 说明在屏幕外面
                swipe((1098, 870), (1098, 429), 4)
                time.sleep(1)
            elif position[1] < 0.38:
                swipe((1098, 429), (1098, 870), 4)
                time.sleep(1)
            else:
                pass
        sysmenu.click()
        poco("Close").click()
        LogNew.log("点击" + poco("FpStrengthenDlg(Clone)").offspring("item0").child("Other").child("Label").get_text() + "前往测试完成")
        print("点击" + poco("FpStrengthenDlg(Clone)").offspring("item0").child("Other").child("Label").get_text() + "前往测试完成")
    return poco("Label").get_text()


def test_ITogold():  # 我要金币页签点击
    InitialGame.Startgame()  # 运行启动游戏脚本，检查游戏是否在运行中
    poco = UnityPoco()
    Intensify()

    if poco("FpStrengthenDlg(Clone)").offspring("item3").offspring("TextLabel").exists():
        poco("FpStrengthenDlg(Clone)").offspring("item3").offspring("TextLabel").click()
    else:
        LogNew.log("ERROR: 我要金币按钮没有找到")
    for item in range(len(poco("Panel").child())):  #
        item1 = "item" + str(item)
        for i in range(5):
            sysmenu = poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("T")
            position = sysmenu.get_position()
            if position[1] > 0.85:  # 对比pos点，得到的pos列表中，第二个元素 > 0.85 说明在屏幕外面
                swipe((1098, 870), (1098, 429), 4)
                time.sleep(1)
            elif position[1] < 0.38:
                swipe((1098, 429), (1098, 870), 4)
                time.sleep(1)
            else:
                pass
        sysmenu.click()
        poco("Close").click()
        LogNew.log("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
        print("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
    return poco("Label").get_text()


def test_IToLB():  # 我要龙币页签点击
    InitialGame.Startgame()  # 运行启动游戏脚本，检查游戏是否在运行中
    poco = UnityPoco()
    Intensify()

    if poco("FpStrengthenDlg(Clone)").offspring("item4").offspring("TextLabel").exists():
        poco("FpStrengthenDlg(Clone)").offspring("item4").offspring("TextLabel").click()
    else:
        LogNew.log("ERROR: 我要龙币按钮没有找到")
    for item in range(len(poco("Panel").child())):  #
        item1 = "item" + str(item)
        for i in range(5):
            sysmenu = poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("T")
            position = sysmenu.get_position()
            if position[1] > 0.85:  # 对比pos点，得到的pos列表中，第二个元素 > 0.85 说明在屏幕外面
                swipe((1098, 870), (1098, 429), 4)
                time.sleep(1)
            elif position[1] < 0.38:
                swipe((1098, 429), (1098, 870), 4)
                time.sleep(1)
            else:
                pass
        sysmenu.click()
        poco("Close").click()
        LogNew.log("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
        print("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
    return poco("Label").get_text()


def tets_IToEquip():  # 我要装备子页签点击
    InitialGame.Startgame()  # 运行启动游戏脚本，检查游戏是否在运行中
    poco = UnityPoco()
    Intensify()

    if poco("FpStrengthenDlg(Clone)").offspring("item5").offspring("TextLabel").exists():
        poco("FpStrengthenDlg(Clone)").offspring("item5").offspring("TextLabel").click()
    else:
        LogNew.log("ERROR: 我要装备按钮没有找到")
    for item in range(len(poco("Panel").child())):  #
        item1 = "item" + str(item)
        for i in range(5):
            sysmenu = poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("T")
            position = sysmenu.get_position()
            if position[1] > 0.85:  # 对比pos点，得到的pos列表中，第二个元素 > 0.85 说明在屏幕外面
                swipe((1098, 870), (1098, 429), 4)
                time.sleep(1)
            elif position[1] < 0.38:
                swipe((1098, 429), (1098, 870), 4)
                time.sleep(1)
            else:
                pass
        sysmenu.click()
        poco("Close").click()
        LogNew.log("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
        print("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
    return poco("Label").get_text()


def test_IToIntensify():  # 我要强化子页签点击
    InitialGame.Startgame()  # 运行启动游戏脚本，检查游戏是否在运行中
    poco = UnityPoco()
    Intensify()

    if poco("FpStrengthenDlg(Clone)").offspring("item6").offspring("TextLabel").exists():
        poco("FpStrengthenDlg(Clone)").offspring("item6").offspring("TextLabel").click()
    else:
        LogNew.log("ERROR: 我要强化按钮没有找到")
    for item in range(len(poco("Panel").child())):  #
        item1 = "item" + str(item)
        for i in range(5):
            sysmenu = poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("T")
            position = sysmenu.get_position()
            if position[1] > 0.85:  # 对比pos点，得到的pos列表中，第二个元素 > 0.85 说明在屏幕外面
                swipe((1098, 870), (1098, 429), 4)
                time.sleep(1)
            elif position[1] < 0.38:
                swipe((1098, 429), (1098, 870), 4)
                time.sleep(1)
            else:
                pass
        sysmenu.click()
        poco("Close").click()
        LogNew.log("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
        print("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
    return poco("Label").get_text()


def test_IToGad():  # 点击我要纹章子页签
    InitialGame.Startgame()  # 运行启动游戏脚本，检查游戏是否在运行中
    poco = UnityPoco()
    Intensify()
    swipe((350, 780), (350, 460), 3)
    swipe((350, 780), (350, 460), 3)

    if poco("FpStrengthenDlg(Clone)").offspring("item7").offspring("TextLabel").exists():
        poco("FpStrengthenDlg(Clone)").offspring("item7").offspring("TextLabel").click()
    else:
        LogNew.log("ERROR: 我要纹章按钮没有找到")

    for item in range(len(poco("Panel").child())):  #
        item1 = "item" + str(item)
        for i in range(5):
            sysmenu = poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("T")
            position = sysmenu.get_position()
            if position[1] > 0.85:  # 对比pos点，得到的pos列表中，第二个元素 > 0.85 说明在屏幕外面
                swipe((1098, 870), (1098, 429), 4)
                time.sleep(1)
            elif position[1] < 0.38:
                swipe((1098, 429), (1098, 870), 4)
                time.sleep(1)
            else:
                pass
        sysmenu.click()
        poco("Close").click()
        LogNew.log("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
        print("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
    return poco("Label").get_text()


def test_IToLY():  # 点击我要龙玉子页签
    InitialGame.Startgame()  # 运行启动游戏脚本，检查游戏是否在运行中
    poco = UnityPoco()
    Intensify()
    swipe((350, 780), (350, 460), 3)  # 向上滑动两次最大化保证可以拿到当前需要的按钮
    swipe((350, 780), (350, 460), 3)

    if poco("FpStrengthenDlg(Clone)").offspring("item8").offspring("TextLabel").exists():
        poco("FpStrengthenDlg(Clone)").offspring("item8").offspring("TextLabel").click()
    else:
        LogNew.log("ERROR: 我要龙玉按钮没有找到")

    for item in range(len(poco("Panel").child())):  #
        item1 = "item" + str(item)
        for i in range(5):
            sysmenu = poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("T")
            position = sysmenu.get_position()
            if position[1] > 0.85:  # 对比pos点，得到的pos列表中，第二个元素 > 0.85 说明在屏幕外面
                swipe((1098, 870), (1098, 429), 4)
                time.sleep(1)
            elif position[1] < 0.38:
                swipe((1098, 429), (1098, 870), 4)
                time.sleep(1)
            else:
                pass
        sysmenu.click()
        poco("Close").click()
        LogNew.log("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
        print("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
    return poco("Label").get_text()

def test_IToSkill():  # 点击我要技能点
    InitialGame.Startgame()  # 运行启动游戏脚本，检查游戏是否在运行中
    poco = UnityPoco()
    Intensify()
    swipe((350, 780), (350, 460), 3)  # 向上滑动两次最大化保证可以拿到当前需要的按钮
    swipe((350, 780), (350, 460), 3)

    if poco("FpStrengthenDlg(Clone)").offspring("item9").offspring("TextLabel").exists():
        poco("FpStrengthenDlg(Clone)").offspring("item9").offspring("TextLabel").click()
    else:
        LogNew.log("ERROR: 我要龙玉按钮没有找到")

    for item in range(len(poco("Panel").child())):  #
        item1 = "item" + str(item)
        for i in range(5):
            sysmenu = poco("FpStrengthenDlg(Clone)").offspring(item1).offspring("T")
            position = sysmenu.get_position()
            if position[1] > 0.85:  # 对比pos点，得到的pos列表中，第二个元素 > 0.85 说明在屏幕外面
                swipe((1098, 870), (1098, 429), 4)
                time.sleep(1)
            elif position[1] < 0.38:
                swipe((1098, 429), (1098, 870), 4)
                time.sleep(1)
            else:
                pass
        sysmenu.click()
        poco("Close").click()
        LogNew.log("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
        print("点击" + poco("FpStrengthenDlg(Clone)").offspring(item1).child("Strengthen").child("Label").get_text() + "前往测试完成")
    return poco("Label").get_text()


