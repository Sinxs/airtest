# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import InitialGame
import LogNew
import Selected_fashion.fashion_1
import os
import time

# if not cli_setup():  # 生成报告文件
#     auto_setup(__file__, logdir=True, devices=[
#             f"Android://{}/172.16.137.64:5555",
#     ])

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
# script content
print("start...")



def Switchroles_1(poco):
    """
    1、重置脚本运行环境
    2、点击头像进入角色选择界面
    :return:
    """
    poco = poco
    # InitialGame.Startgame(poco)  # 初始化脚本运行环境
    if not poco("Open").exists():
        poco("Avatar").click()
        touch((2118, 454))
        poco(text="切换角色").click()
        sleep(10)
    else:
        poco("Avatar").click()
        poco(text="切换角色").click()
        sleep(10)


def Switchroles_2(chroles,poco):
    """
    1、选择账号角色
    :return:
    """
    poco=poco
    Prof = "Prof" +  str(chroles)
    poco(Prof).click()
    sleep(3)
    poco("Label").click()
    sleep(11)

def Skillpos(poco):
    """

    2、在主界面寻找技能按钮
    :return:
    """
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    poco=poco
    # SysBSkill = poco("SysBSkill")
    for x in range(10):
        poco = UnityPoco()
        Close = poco("Close")
        l_close = poco(texture="l_close_00")
        if l_close.exists() and Close.exists():
            poco(texture="l_close_00").click()
        elif Close.exists():
            Close.click()
        else:
            LogNew.log("初始化脚本环境成功。。。")
    Skillpos = poco("SysBSkill").get_position()
    if Skillpos[0] > 1:
        print("当前界面没有技能按钮，点击 + 号")
        LogNew.log("当前界面没有技能按钮，点击 + 号")
        poco(texture="switch").click()
        poco("SysBSkill").click()  # 点击技能按钮
    else:
        print("当前界面就有技能按钮")
        LogNew.log("当前界面就有技能按钮")
        poco("SysBSkill").click()  # 点击技能按钮


def Skillpng(poco):
    """
    在主界面查找技能按钮
    找不到就点击+号
    :return:
    """
    if poco("SkillTree(Clone)").offspring("Type").get_text() == "被动技能":
        print("被动技能不能预览")
        LogNew.log("被动技能不能预览")

    else:
        poco("Play").click()
        print("播放技能预览视频")
        LogNew.log("播放技能预览视频")
        LogNew.log("----------下一个技能----------")



def Skill(poco):
    """
    1、点击技能按钮
    2、判断所有技能控件
    3、点击所有技能并进行演示
    :return:
    """
    poco = poco
    # InitialGame.Startgame(poco)  # 初始化脚本运行环境
    Skillpos(poco)  # 重置Skillpos脚本
    for item in range(len(poco("Tabs").child())):  # 判断当前界面中的角色职业控件元素
        item1 = "item" + str(item)
        poco("SkillTree(Clone)").offspring("Tabs").child(item1).click()
        print("选择" + poco("SkillTree(Clone)").offspring("Tabs").child(item1).child("SelectedTextLabel").get_text() + "职业，开始测试技能模块")
        LogNew.log("选择" + poco("SkillTree(Clone)").offspring("Tabs").child(item1).child("SelectedTextLabel").get_text() + "职业，开始测试技能模块")
        for item2 in range(len(poco("Skill").child())):  # 判断当前职业的所有技能控件元素
            item21 = "Skill" + str(item2 + 1)
            Skillpos_1 = poco("SkillTree(Clone)").offspring(str(item21)).child("Bg").get_position()
            if Skillpos_1[1] > 0.9:  # 判断当前技能元素是不是在屏幕以内
                swipe((1098, 870), (1098, 429), 4)
                swipe((1098, 870), (1098, 429), 4)
                poco("SkillTree(Clone)").offspring(str(item21)).child("Bg").click()
                print("点击" + poco("SkillTree(Clone)").offspring("Name").get_text() + "技能")
                LogNew.log("点击" + poco("SkillTree(Clone)").offspring("Name").get_text() + "技能")
                Skillpng(poco)  # 点击视频预览
            else:
                poco("SkillTree(Clone)").offspring(str(item21)).child("Bg").click()
                print("点击" + poco("SkillTree(Clone)").offspring("Name").get_text() + "技能")
                LogNew.log("点击" + poco("SkillTree(Clone)").offspring("Name").get_text() + "技能")
                Skillpng(poco)  # 点击视频预览
    return poco("SkillTree(Clone)").offspring("Tabs").child("item2").child("SelectedTextLabel").get_text()  # 返回一个当前角色的二转职业


def Prof1_fenzhi(poco):
    """
    判断当前角色是否已经转职，如果已经转职，则重置当前角色
    :return:
    """
    poco("ResetProf").click()  # 点击重置转职
    for i in range(3):
        if poco("GreyModalDlg(Clone)").child("Bg").exists():
            poco("OK").click()
    else:
        print("当前角色还未转职，不需要重新转职")


def Prof1_zhiye(poco):
    """
    选择当前职业并点击确定
    :return:
    """
    poco("TurnProBtn").click()  # 点击转职按钮
    if poco("GreyModalDlg(Clone)").child("Bg").exists():
        poco("OK").click()
        print("当前角色转职为" + poco("SkillTree(Clone)").offspring("Tabs").child("item1").child("SelectedTextLabel").get_text())
    else:
        print("ERROR:转职失败，请检查")


def juexing(poco):
    poco("SkillTree(Clone)").offspring("Tabs").child("item3").click()  # 点击觉醒
    poco("TurnAwakeBtn").click()  # 在觉醒界面点击完成觉醒

def Skill_Switchroles(damo,poco):  # 重置当前职业
    poco=poco
    Switchroles_1(poco)  # 点击切换角色，并重置测试环境
    Switchroles_2(damo, poco)  # 选择角色
    # InitialGame.Startgame(poco)  # 初始化脚本运行环境
    Skillpos(poco)  # 主界面寻找技能按钮。并点击
    Prof1_fenzhi(poco)  # 重置当前角色职业
# os.system("airtest report D:\case\Skill\Skill.py --log_root log/ --outfile log/log.html --lang zh")
