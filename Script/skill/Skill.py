# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import get_screen_size
print("start...")


def devicesize(devices):
   return touch((get_screen_size._get_screen_size(devices)[0] * 0.93, get_screen_size._get_screen_size(devices)[1] * 0.52))

def Switchroles_1(poco):
    """
    1、重置脚本运行环境
    2、点击头像进入角色选择界面
    :return:
    """

    if not poco("Open").exists():
        poco("Avatar").click()
        print(device)
        # todo:相对坐标的改动较大，暂时延后
        # devicesize(poco)
        touch((2255, 1026))  # 点击GM出现的确定控件
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
    Prof = "Prof"+str(chroles)
    poco(Prof).click()
    sleep(3)
    poco("Label").click()
    sleep(11)

def Skillpos(poco):
    """
    2、在主界面寻找技能按钮
    :return:
    """
    # SysBSkill = poco("SysBSkill")
    for x in range(10):
        Close = poco("Close")
        l_close = poco(texture="l_close_00")
        if l_close.exists() and Close.exists():
            poco(texture="l_close_00").click()
        elif Close.exists():
            Close.click()
        else:
            break
    Skillpos = poco("SysBSkill").get_position()
    if Skillpos[0] > 1:
        print("当前界面没有技能按钮，点击 + 号")
        poco(texture="switch").click()
        poco("SysBSkill").click()  # 点击技能按钮
    else:
        print("当前界面就有技能按钮")
        poco("SysBSkill").click()  # 点击技能按钮


def Skillpng(poco):
    """
    在主界面查找技能按钮
    找不到就点击+号
    :return:
    """
    if poco("SkillTree(Clone)").offspring("Type").get_text() == "被动技能":
        print("被动技能不能预览")

    else:
        poco("Play").click()
        print("播放技能预览视频")
        print("----------下一个技能----------")



def Skill(poco):
    """
    1、点击技能按钮
    2、判断所有技能控件
    3、点击所有技能并进行演示
    :return:
    """
    poco = poco
    Skillpos(poco)  # 重置Skillpos脚本
    for item in range(len(poco("Tabs").child())):  # 判断当前界面中的角色职业控件元素
        item1 = "item" + str(item)
        poco("SkillTree(Clone)").offspring("Tabs").child(item1).click()
        print("选择" + poco("SkillTree(Clone)").offspring("Tabs").child(item1).child("SelectedTextLabel").get_text() + "职业，开始测试技能模块")
        for item2 in range(len(poco("Skill").child())):  # 判断当前职业的所有技能控件元素
            item21 = "Skill" + str(item2 + 1)
            Skillpos_1 = poco("SkillTree(Clone)").offspring(str(item21)).child("Bg").get_position()
            if Skillpos_1[1] > 0.9:  # 判断当前技能元素是不是在屏幕以内
                swipe((950, 770), (950, 480), 10)
                swipe((950, 770), (950, 480), 10)
                poco("SkillTree(Clone)").offspring(str(item21)).child("Bg").click()
                print("点击" + poco("SkillTree(Clone)").offspring("Name").get_text() + "技能")
                Skillpng(poco)  # 点击视频预览
            else:
                poco("SkillTree(Clone)").offspring(str(item21)).child("Bg").click()
                print("点击" + poco("SkillTree(Clone)").offspring("Name").get_text() + "技能")
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


from airtest.core.api import *

"""
---------------------------------------------以下为战士分支----------------------------------
"""

def test_warrior_1(devices):  # Prof1-转职为战士分支、剑圣分支、月之领主职业
    """
    转职为战士分支、剑圣分支、月之领主职业
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof1-转职为战士分支、剑圣分支、月之领主职业")
    Skill_Switchroles(1, poco)  # 重置当前角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择剑圣职业
    Prof1_zhiye(poco)  # 转职为战士分支剑圣职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # 点击月之领主职业
    Prof1_zhiye(poco)  # 转职为战士分支、剑圣分支、月之领主职业
    """点击月之领主职业"""
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块

def test_warrior_2(devices):  #  Prof1-转职为战士分支、剑圣分支、剑皇职业
    """
     转职为战士分支、剑圣分支、剑皇职业
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof1-转职为战士分支、剑圣分支、月之领主职业")
    Skill_Switchroles(1, poco)  # 重置当前角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择剑圣职业
    Prof1_zhiye(poco)  # 转职为战士分支剑圣职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # 点击月之领主职业
    Prof1_zhiye(poco)  # 转职为战士分支、剑圣分支、剑皇职业
    """点击月之领主职业"""
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块



def test_warrior_3(devices): #  Prof1- 转职为战士分支、剑圣分支、复仇者、黑暗复仇者职业
    """
     转职为战士分支、剑圣分支、复仇者、黑暗复仇者职业
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof1-转职为战士分支、剑圣分支、黑暗复仇者职业")
    Skill_Switchroles(1, poco)  # 重置当前角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail3").click()  # 点击选择剑圣职业
    Prof1_zhiye(poco)  # 转职为战士分支剑圣职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # 点击黑暗复仇者职业
    """点击黑暗复仇者职业"""
    Prof1_zhiye(poco)  # 转职为战士分支、剑圣分支、黑暗复仇者职业
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_warrior_4(devices):  # Prof1- 转职为战士分支、战皇分支、狂战士者职业
    """
       Prof1- 转职为战士分支、战皇分支、狂战士职业
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof1-转职为战士分支、剑圣分支、狂战士职业")
    Skill_Switchroles(1, poco)  # 重置当前角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择剑圣职业
    Prof1_zhiye(poco)  # 转职为战士分支剑圣职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # 点击狂战士职业
    """点击狂战士职业"""
    Prof1_zhiye(poco)  # Prof1- 转职为战士分支、战皇分支、狂战士者职业
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_warrior_5(devices):  # Prof1- 转职为战士分支、战神分支、毁灭者者职业
    """
       Prof1- 转职为战士分支、战神分支、毁灭者者职业
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof1- 转职为战士分支、战神分支、毁灭者者职业")
    Skill_Switchroles(1, poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择战神职业
    Prof1_zhiye(poco)  # 转职为战士分支战神职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # 点击毁灭者职业
    """点击毁灭者职业"""
    Prof1_zhiye(poco)  # Prof1- 转职为战士分支、战皇分支、毁灭者者职业
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


"""
---------------------------------------------以下为弓箭手分支-----------------------------------
"""


def test_Archer_1(devices):  # Prof2-转职为弓箭手分支、箭神分支、魔羽分支
    """
       Prof2-转职为弓箭手分支、箭神分支、魔羽分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof2-转职为弓箭手分支、箭神分支、魔羽分支")
    Skill_Switchroles(2,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择箭神职业
    Prof1_zhiye(poco)  # 转职为弓箭手分支、箭神分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # 转职为弓箭手分支、箭神分支、魔羽分支
    """点击魔羽职业"""
    Prof1_zhiye(poco)  # Prof1- 转职为弓箭手分支、箭神分支、魔羽分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_Archer_2(devices):  # Prof2-转职为弓箭手分支、箭神分支、狙翎分支
    """
       Prof2-转职为弓箭手分支、箭神分支、魔羽分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof2-转职为弓箭手分支、箭神分支、狙翎分支")
    Skill_Switchroles(2,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择箭神职业
    Prof1_zhiye(poco)  # 转职为弓箭手分支、箭神分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof1- 转职为弓箭手分支、箭神分支、狙翎分支
    """点击魔羽职业"""
    Prof1_zhiye(poco)  # Prof1- 转职为弓箭手分支、箭神分支、狙翎分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_Archer_3(devices):  # Prof2-转职为弓箭手分支、猎人分支、银色猎人分支
    """
       Prof2-转职为弓箭手分支、猎人分支、银色猎人分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof2-转职为弓箭手分支、箭神分支、银色猎人分支")
    Skill_Switchroles(2,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail3").click()  # 点击选择猎人职业
    Prof1_zhiye(poco)  # 转职为弓箭手分支、猎人分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # 转职为弓箭手分支、猎人分支、银色猎人分支
    """点击银色猎人职业"""
    Prof1_zhiye(poco)  # Prof1- 转职为弓箭手分支、猎人分支、银色猎人分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_Archer_4(devices):  # Prof2-转职为弓箭手分支、游侠分支、风行者分支
    """
       Prof2-转职为弓箭手分支、游侠分支、风行者分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof2-转职为弓箭手分支、游侠分支、风行者分支")
    Skill_Switchroles(2, poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择猎人职业
    Prof1_zhiye(poco)  # 转职为弓箭手分支、游侠分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof2-转职为弓箭手分支、游侠分支、风行者分支
    """点击风行者分支职业"""
    Prof1_zhiye(poco)  # Prof2-转职为弓箭手分支、游侠分支、风行者分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_Archer_5(devices):  # Prof2-转职为弓箭手分支、游侠分支、影舞者分支
    """
       Prof2-转职为弓箭手分支、游侠分支、影舞者分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof2-转职为弓箭手分支、游侠分支、影舞者分支")
    Skill_Switchroles(2,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择猎人职业
    Prof1_zhiye(poco)  # 转职为弓箭手分支、游侠分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof2-转职为弓箭手分支、游侠分支、影舞者分支
    """点击、影舞者职业"""
    Prof1_zhiye(poco)  # Prof2-转职为弓箭手分支、游侠分支、影舞者分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


"""
---------------------------------------------以下为魔法师分支--------------------------------------------
"""


def test_magic_1(devices):  # Prof3-转职为魔法师分支、元素分支、冰灵分支
    """
       Prof3-转职为魔法师分支、元素分支、冰灵分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof3-转职为魔法师分支、元素分支、冰灵分支")
    Skill_Switchroles(3,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择元素职业
    Prof1_zhiye(poco)  # 转职为魔法师分支、元素分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof3-转职为魔法师分支、元素分支、冰灵分支
    """点击冰灵分支职业"""
    Prof1_zhiye(poco)  # Prof3-转职为魔法师分支、元素分支、冰灵分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_magic_2(devices):  # Prof3-转职为魔法师分支、元素分支、火舞分支
    """
        Prof3-转职为魔法师分支、元素分支、火舞分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof3-转职为魔法师分支、元素分支、火舞分支")
    Skill_Switchroles(3,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择元素职业
    Prof1_zhiye(poco)  # 转职为魔法师分支、元素分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  #  Prof3-转职为魔法师分支、元素分支、火舞分支
    """点击火舞分支职业"""
    Prof1_zhiye(poco)  #  Prof3-转职为魔法师分支、元素分支、火舞分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_magic_3(devices):  # Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支
    """
       Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支")
    Skill_Switchroles(3,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择魔导师分支
    Prof1_zhiye(poco)  # 转职为魔法师分支、魔导师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  #  Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支
    """点击黑暗女王分职业"""
    Prof1_zhiye(poco)  #  Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_magic_4(devices):  # Prof3-转职为魔法师分支、魔导师分支、时空领主分支
    """
       Prof3-转职为魔法师分支、魔导师分支、时空领主分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof3-转职为魔法师分支、魔导师分支、时空领主分支")
    Skill_Switchroles(3, poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择魔导师分支
    Prof1_zhiye(poco)  # 转职为魔法师分支、魔导师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  #  Prof3-转职为魔法师分支、魔导师分支、时空领主分支
    """点击时空领主分支职业"""
    Prof1_zhiye(poco)  #  Prof3-转职为魔法师分支、魔导师分支、时空领主分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


"""
---------------------------------------------以下为牧师分支---------------------------------------------
"""


def test_pastor_1(devices):  # Prof4-转职为牧师分支、祭祀分支、雷神分支
    """
        Prof4-转职为牧师分支、祭祀分支、雷神分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof4-转职为牧师分支、祭祀分支、雷神分支")
    Skill_Switchroles(4,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 转职为牧师分支、祭祀分支
    Prof1_zhiye(poco)  # 转职为牧师分支、祭祀分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof4-转职为牧师分支、祭祀分支、雷神分支
    """点击雷神分支职业"""
    Prof1_zhiye(poco)  # Prof4-转职为牧师分支、祭祀分支、雷神分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_pastor_2(devices):  # Prof4-转职为牧师分支、祭祀分支、圣徒分支
    """
        Prof4-转职为牧师分支、祭祀分支、圣徒分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof4-转职为牧师分支、祭祀分支、圣徒分支")
    Skill_Switchroles(4,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 转职为牧师分支、祭祀分支
    Prof1_zhiye(poco)  # 转职为牧师分支、祭祀分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof4-转职为牧师分支、祭祀分支、圣徒分支
    """点击圣徒分支职业"""
    Prof1_zhiye(poco)  # Prof4-转职为牧师分支、祭祀分支、圣徒分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_pastor_3(devices):  # Prof4-转职为牧师分支、贤者分支、十字军分支
    """
        Prof4-转职为牧师分支、贤者分支、十字军分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof4-转职为牧师分支、贤者分支、十字军分支")
    Skill_Switchroles(4,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 转职为牧师分支、祭祀分支
    Prof1_zhiye(poco)  # 转职为牧师分支、祭祀分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # PProf4-转职为牧师分支、贤者分支、十字军分支
    """点击十字军分支职业"""
    Prof1_zhiye(poco)  # Prof4-转职为牧师分支、贤者分支、十字军分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_pastor_4(devices):  # Prof4-转职为牧师分支、贤者分支、圣骑士分支
    """
        Prof4-转职为牧师分支、贤者分支、圣骑士分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof4-转职为牧师分支、贤者分支、圣骑士分支")
    Skill_Switchroles(4,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 转职为牧师分支、祭祀分支
    Prof1_zhiye(poco)  # 转职为牧师分支、祭祀分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof4-转职为牧师分支、贤者分支、圣骑士分支
    """点击圣骑士分支职业"""
    Prof1_zhiye(poco)  # Prof4-转职为牧师分支、贤者分支、圣骑士分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


"""
---------------------------------------------以下为学者分支---------------------------------------------
"""


def test_scholar_1(devices):  # Prof5-转职为学者分支、工程师分支、重炮手分支
    """
        Prof5-转职为学者分支、工程师分支、重炮手分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof5-转职为学者分支、工程师分支、重炮手分支")
    Skill_Switchroles(5,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # Prof5-转职为学者分支、工程师分支
    Prof1_zhiye(poco)  # Prof5-转职为学者分支、工程师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof5-转职为学者分支、工程师分支、重炮手分支
    """点击重炮手职业"""
    Prof1_zhiye(poco)  # Prof5-转职为学者分支、工程师分支、重炮手分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_scholar_2(devices):  # Prof5-转职为学者分支、工程师分支、机械大师分支
    """
        Prof5-转职为学者分支、工程师分支、机械大师分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof5-转职为学者分支、工程师分支、机械大师分支")
    Skill_Switchroles(5,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # Prof5-转职为学者分支、工程师分支
    Prof1_zhiye(poco)  # Prof5-转职为学者分支、工程师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof5-转职为学者分支、工程师分支、机械大师分支
    """点击机械大师职业"""
    Prof1_zhiye(poco)  # Prof5-转职为学者分支、工程师分支、机械大师分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


def test_scholar_3(devices):  # Prof5-转职为学者分支、炼金术士分支、炼金圣士分支
    """
        Prof5-转职为学者分支、炼金术士分支、炼金圣士分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof5-转职为学者分支、炼金术士分支、炼金圣士分支")
    Skill_Switchroles(5,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof5-转职为学者分支、炼金术士分支
    Prof1_zhiye(poco)  # Prof5-转职为学者分支、工程师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof5-转职为学者分支、炼金术士分支、炼金圣士分支
    """点击炼金圣士职业"""
    Prof1_zhiye(poco)  # Prof5-转职为学者分支、炼金术士分支、炼金圣士分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块




def test_scholar_4(devices):  # Prof5-转职为学者分支、炼金术士分支、药剂师分支
    """
         Prof5-转职为学者分支、炼金术士分支、药剂师分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof5-转职为学者分支、炼金术士分支、药剂师分支")
    Skill_Switchroles(5,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof5-转职为学者分支、炼金术士分支
    Prof1_zhiye(poco)  # Prof5-转职为学者分支、工程师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  #  Prof5-转职为学者分支、炼金术士分支、药剂师分支
    """点击药剂师分支职业"""
    Prof1_zhiye(poco)  #  Prof5-转职为学者分支、炼金术士分支、药剂师分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块



"""
---------------------------------------------以下为刺客分支---------------------------------------------
"""


def test_thug_1(devices):  # Prof6-转职为刺客分支、暗之使徒分支、烈分支
    """
         Prof6-转职为刺客分支、暗之使徒分支、烈分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof6-转职为刺客分支、暗之使徒分支、烈分支")
    Skill_Switchroles(6,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # Prof6-转职为刺客分支、暗之使徒分支
    Prof1_zhiye(poco)  # Prof6-转职为刺客分支、暗之使徒分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof6-转职为刺客分支、暗之使徒分支、烈分支
    """点击烈职业"""
    Prof1_zhiye(poco)  #  PProf6-转职为刺客分支、暗之使徒分支、烈分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块





def test_thug_2(devices):  # Prof6-转职为刺客分支、暗之使徒分支、影分支
    """
         Prof6-转职为刺客分支、暗之使徒分支、影分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof6-转职为刺客分支、暗之使徒分支、烈分支")
    Skill_Switchroles(6,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # Prof6-转职为刺客分支、暗之使徒分支
    Prof1_zhiye(poco)  # Prof6-转职为刺客分支、暗之使徒分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof6-转职为刺客分支、暗之使徒分支、影分支
    """点击影职业"""
    Prof1_zhiye(poco)  # Prof6-转职为刺客分支、暗之使徒分支、影分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块





def test_thug_3(devices):  # Prof6-转职为刺客分支、光明之怒分支、耀分支
    """
         Prof6-转职为刺客分支、光明之怒分支、耀分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof6-转职为刺客分支、光明之怒分支、耀分支")
    Skill_Switchroles(6,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof6-转职为刺客分支、光明之怒分支
    Prof1_zhiye(poco)  # Prof6-转职为刺客分支、光明之怒分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof6-转职为刺客分支、光明之怒分支、耀分支
    """点击耀职业"""
    Prof1_zhiye(poco)  # Prof6-转职为刺客分支、光明之怒分支、耀分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块





def test_thug_4(devices):  # Prof6-转职为刺客分支、光明之怒分支、暗分支
    """
         Prof6-转职为刺客分支、光明之怒分支、暗分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof6-转职为刺客分支、光明之怒分支、暗分支")
    Skill_Switchroles(6,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof6-转职为刺客分支、光明之怒分支
    Prof1_zhiye(poco)  # Prof6-转职为刺客分支、光明之怒分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof6-转职为刺客分支、光明之怒分支、暗分支
    """点击暗职业"""
    Prof1_zhiye(poco)  # Prof6-转职为刺客分支、光明之怒分支、暗分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块


"""
---------------------------------------------以下为舞娘分支---------------------------------------------
"""





def test_dance_1(devices):  # Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
    """
         Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支")
    Skill_Switchroles(7,poco)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # PProf7-转职为舞娘分支、呐喊者分支
    Prof1_zhiye(poco)  # Prof7-转职为舞娘分支、呐喊者分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
    """点击噬魂者职业"""
    Prof1_zhiye(poco)  # Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块






def test_dance_2(devices):  # Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支
    """
         Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支")
    Skill_Switchroles(7, poco)  # 选择角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # PProf7-转职为舞娘分支、呐喊者分支
    Prof1_zhiye(poco)  # Prof7-转职为舞娘分支、呐喊者分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支
    """点击黑暗萨满职业"""
    Prof1_zhiye(poco)  # Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块



def test_dance_3(devices):  # Prof7-转职为舞娘分支、舞者分支、灵魂舞者分支
    """
         Prof7-转职为舞娘分支、舞者分支、灵魂舞者分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print(" Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支")
    Skill_Switchroles(7,poco)  # 选择角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof7-转职为舞娘分支、舞者分支
    Prof1_zhiye(poco)  # Prof7-转职为舞娘分支、舞者分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof7-转职为舞娘分支、舞者分支、灵魂舞者分支
    """点击灵魂舞者职业"""
    Prof1_zhiye(poco)  # Prof7-转职为舞娘分支、舞者分支、灵魂舞者分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块




def test_dance_4(devices):  # Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支
    """
         Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    print("Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支")
    Skill_Switchroles(7, poco)  # 选择角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof7-转职为舞娘分支、舞者分支
    Prof1_zhiye(poco)  # Prof7-转职为舞娘分支、舞者分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支
    """点击刀锋舞者职业"""
    Prof1_zhiye(poco)  # Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    juexing(poco)  # 点击觉醒
    return Skill(poco)  # 测试技能模块

