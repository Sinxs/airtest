# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from Skill_1 import Skill
import InitialGame
# if not cli_setup():
#     auto_setup(__file__, logdir=True, devices=[
#             "Android://127.0.0.1:5037/172.16.137.64:5555",
#     ])
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
# script content
print("start...")
# generate html report
from airtest.report.report import simple_report
simple_report(__file__, logpath=True)

"""
---------------------------------------------以下为战士分支----------------------------------
"""
from Common.Tools import getdevices
def test_Prof1_1(poco):  # Prof1-转职为战士分支、剑圣分支、月之领主职业
    """
    转职为战士分支、剑圣分支、月之领主职业
    :return:
    """
    poco=poco
    print("Prof1-转职为战士分支、剑圣分支、月之领主职业")
    Skill.Skill_Switchroles(1, poco)  # 重置当前角色职业
    print("+++++++++++++++++++++++++++++")
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择剑圣职业
    Skill.Prof1_zhiye(poco)  # 转职为战士分支剑圣职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # 点击月之领主职业
    Skill.Prof1_zhiye(poco)  # 转职为战士分支、剑圣分支、月之领主职业
    """点击月之领主职业"""
    Skill.juexing(poco)  # 点击觉醒
    return Skill.Skill(poco)  # 测试技能模块


def test_Prof1_2():  #  Prof1-转职为战士分支、剑圣分支、剑皇职业
    """
     转职为战士分支、剑圣分支、剑皇职业
    :return:
    """
    print("Prof1-转职为战士分支、剑圣分支、剑皇职业职业")
    Skill.Skill_Switchroles(1)  # 重置当前角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择剑圣职业
    Skill.Prof1_zhiye()  # 转职为战士分支剑圣职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # 点击剑皇职业
    Skill.Prof1_zhiye()  # 转职为战士分支、剑圣分支、剑皇职业
    """点击剑皇职业"""
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


def test_Prof1_3():  #  Prof1- 转职为战士分支、剑圣分支、复仇者、黑暗复仇者职业
    """
     转职为战士分支、剑圣分支、复仇者、黑暗复仇者职业
    :return:
    """
    print("Prof1-转职为战士分支、剑圣分支、黑暗复仇者职业")
    Skill.Skill_Switchroles(1)  # 重置当前角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail3").click()  # 点击选择剑圣职业
    Skill.Prof1_zhiye()  # 转职为战士分支剑圣职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # 点击黑暗复仇者职业
    """点击黑暗复仇者职业"""
    Skill.Prof1_zhiye()  # 转职为战士分支、剑圣分支、黑暗复仇者职业
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


def test_Prof1_4():  # Prof1- 转职为战士分支、战皇分支、狂战士者职业
    """
       Prof1- 转职为战士分支、战皇分支、狂战士职业
    :return:
    """
    print("Prof1-转职为战士分支、剑圣分支、狂战士职业")
    Skill.Skill_Switchroles(1)  # 重置当前角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择剑圣职业
    Skill.Prof1_zhiye()  # 转职为战士分支剑圣职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # 点击狂战士职业
    """点击狂战士职业"""
    Skill.Prof1_zhiye()  # Prof1- 转职为战士分支、战皇分支、狂战士者职业
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


def test_Prof1_5():  # Prof1- 转职为战士分支、战神分支、毁灭者者职业
    """
       Prof1- 转职为战士分支、战神分支、毁灭者者职业
    :return:
    """
    print("Prof1- 转职为战士分支、战神分支、毁灭者者职业")
    Skill.Skill_Switchroles(1)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择战神职业
    Skill.Prof1_zhiye()  # 转职为战士分支战神职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # 点击毁灭者职业
    """点击毁灭者职业"""
    Skill.Prof1_zhiye()  # Prof1- 转职为战士分支、战皇分支、毁灭者者职业
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


"""
---------------------------------------------以下为弓箭手分支-----------------------------------
"""
def test_Prof1_6():  # Prof2-转职为弓箭手分支、箭神分支、魔羽分支
    """
       Prof2-转职为弓箭手分支、箭神分支、魔羽分支
    :return:
    """
    print("Prof2-转职为弓箭手分支、箭神分支、魔羽分支")
    Skill.Skill_Switchroles(2)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择箭神职业
    Skill.Prof1_zhiye()  # 转职为弓箭手分支、箭神分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # 转职为弓箭手分支、箭神分支、魔羽分支
    """点击魔羽职业"""
    Skill.Prof1_zhiye()  # Prof1- 转职为弓箭手分支、箭神分支、魔羽分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块



def test_Prof1_7():  # Prof2-转职为弓箭手分支、箭神分支、狙翎分支
    """
       Prof2-转职为弓箭手分支、箭神分支、魔羽分支
    :return:
    """
    print("Prof2-转职为弓箭手分支、箭神分支、狙翎分支")
    Skill.Skill_Switchroles(2)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择箭神职业
    Skill.Prof1_zhiye()  # 转职为弓箭手分支、箭神分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof1- 转职为弓箭手分支、箭神分支、狙翎分支
    """点击魔羽职业"""
    Skill.Prof1_zhiye()  # Prof1- 转职为弓箭手分支、箭神分支、狙翎分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


def test_Prof1_8():  # Prof2-转职为弓箭手分支、猎人分支、银色猎人分支
    """
       Prof2-转职为弓箭手分支、猎人分支、银色猎人分支
    :return:
    """
    print("Prof2-转职为弓箭手分支、箭神分支、银色猎人分支")
    Skill.Skill_Switchroles(2)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail3").click()  # 点击选择猎人职业
    Skill.Prof1_zhiye()  # 转职为弓箭手分支、猎人分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # 转职为弓箭手分支、猎人分支、银色猎人分支
    """点击银色猎人职业"""
    Skill.Prof1_zhiye()  # Prof1- 转职为弓箭手分支、猎人分支、银色猎人分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


def test_Prof1_9():  # Prof2-转职为弓箭手分支、游侠分支、风行者分支
    """
       Prof2-转职为弓箭手分支、游侠分支、风行者分支
    :return:
    """
    print("Prof2-转职为弓箭手分支、游侠分支、风行者分支")
    Skill.Skill_Switchroles(2)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择猎人职业
    Skill.Prof1_zhiye()  # 转职为弓箭手分支、游侠分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof2-转职为弓箭手分支、游侠分支、风行者分支
    """点击风行者分支职业"""
    Skill.Prof1_zhiye()  # Prof2-转职为弓箭手分支、游侠分支、风行者分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块




def test_Prof1_10():  # Prof2-转职为弓箭手分支、游侠分支、影舞者分支
    """
       Prof2-转职为弓箭手分支、游侠分支、影舞者分支
    :return:
    """
    print("Prof2-转职为弓箭手分支、游侠分支、影舞者分支")
    Skill.Skill_Switchroles(2)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择猎人职业
    Skill.Prof1_zhiye()  # 转职为弓箭手分支、游侠分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof2-转职为弓箭手分支、游侠分支、影舞者分支
    """点击、影舞者职业"""
    Skill.Prof1_zhiye()  # Prof2-转职为弓箭手分支、游侠分支、影舞者分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


"""
---------------------------------------------以下为魔法师分支--------------------------------------------
"""


def test_Prof1_11():  # Prof3-转职为魔法师分支、元素分支、冰灵分支
    """
       Prof3-转职为魔法师分支、元素分支、冰灵分支
    :return:
    """
    print("Prof3-转职为魔法师分支、元素分支、冰灵分支")
    Skill.Skill_Switchroles(3)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择元素职业
    Skill.Prof1_zhiye()  # 转职为魔法师分支、元素分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof3-转职为魔法师分支、元素分支、冰灵分支
    """点击冰灵分支职业"""
    Skill.Prof1_zhiye()  # Prof3-转职为魔法师分支、元素分支、冰灵分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块



def test_Prof1_12():  # Prof3-转职为魔法师分支、元素分支、火舞分支
    """
        Prof3-转职为魔法师分支、元素分支、火舞分支
    :return:
    """
    print(" Prof3-转职为魔法师分支、元素分支、火舞分支")
    Skill.Skill_Switchroles(3)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 点击选择元素职业
    Skill.Prof1_zhiye()  # 转职为魔法师分支、元素分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  #  Prof3-转职为魔法师分支、元素分支、火舞分支
    """点击火舞分支职业"""
    Skill.Prof1_zhiye()  #  Prof3-转职为魔法师分支、元素分支、火舞分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块



def test_Prof1_13():  # Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支
    """
       Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支
    :return:
    """
    print(" Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支")
    Skill.Skill_Switchroles(3)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择魔导师分支
    Skill.Prof1_zhiye()  # 转职为魔法师分支、魔导师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  #  Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支
    """点击黑暗女王分职业"""
    Skill.Prof1_zhiye()  #  Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块



def test_Prof1_14():  # Prof3-转职为魔法师分支、魔导师分支、时空领主分支
    """
       Prof3-转职为魔法师分支、魔导师分支、时空领主分支
    :return:
    """
    print("Prof3-转职为魔法师分支、魔导师分支、时空领主分支")
    Skill.Skill_Switchroles(3)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 点击选择魔导师分支
    Skill.Prof1_zhiye()  # 转职为魔法师分支、魔导师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  #  Prof3-转职为魔法师分支、魔导师分支、时空领主分支
    """点击时空领主分支职业"""
    Skill.Prof1_zhiye()  #  Prof3-转职为魔法师分支、魔导师分支、时空领主分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


"""
---------------------------------------------以下为牧师分支---------------------------------------------
"""

def test_Prof1_15():  # Prof4-转职为牧师分支、祭祀分支、雷神分支
    """
        Prof4-转职为牧师分支、祭祀分支、雷神分支
    :return:
    """
    print(" Prof4-转职为牧师分支、祭祀分支、雷神分支")
    Skill.Skill_Switchroles(4)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 转职为牧师分支、祭祀分支
    Skill.Prof1_zhiye()  # 转职为牧师分支、祭祀分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof4-转职为牧师分支、祭祀分支、雷神分支
    """点击雷神分支职业"""
    Skill.Prof1_zhiye()  # Prof4-转职为牧师分支、祭祀分支、雷神分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块



def test_Prof1_16():  # Prof4-转职为牧师分支、祭祀分支、圣徒分支
    """
        Prof4-转职为牧师分支、祭祀分支、圣徒分支
    :return:
    """
    print(" Prof4-转职为牧师分支、祭祀分支、圣徒分支")
    Skill.Skill_Switchroles(4)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # 转职为牧师分支、祭祀分支
    Skill.Prof1_zhiye()  # 转职为牧师分支、祭祀分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof4-转职为牧师分支、祭祀分支、圣徒分支
    """点击圣徒分支职业"""
    Skill.Prof1_zhiye()  # Prof4-转职为牧师分支、祭祀分支、圣徒分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


def test_Prof1_17():  # Prof4-转职为牧师分支、贤者分支、十字军分支
    """
        Prof4-转职为牧师分支、贤者分支、十字军分支
    :return:
    """
    print("Prof4-转职为牧师分支、贤者分支、十字军分支")
    Skill.Skill_Switchroles(4)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 转职为牧师分支、祭祀分支
    Skill.Prof1_zhiye()  # 转职为牧师分支、祭祀分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # PProf4-转职为牧师分支、贤者分支、十字军分支
    """点击十字军分支职业"""
    Skill.Prof1_zhiye()  # Prof4-转职为牧师分支、贤者分支、十字军分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块



def test_Prof1_18():  # Prof4-转职为牧师分支、贤者分支、圣骑士分支
    """
        Prof4-转职为牧师分支、贤者分支、圣骑士分支
    :return:
    """
    print("Prof4-转职为牧师分支、贤者分支、圣骑士分支")
    Skill.Skill_Switchroles(4)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # 转职为牧师分支、祭祀分支
    Skill.Prof1_zhiye()  # 转职为牧师分支、祭祀分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof4-转职为牧师分支、贤者分支、圣骑士分支
    """点击圣骑士分支职业"""
    Skill.Prof1_zhiye()  # Prof4-转职为牧师分支、贤者分支、圣骑士分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


"""
---------------------------------------------以下为学者分支---------------------------------------------
"""



def test_Prof1_19():  # Prof5-转职为学者分支、工程师分支、重炮手分支
    """
        Prof5-转职为学者分支、工程师分支、重炮手分支
    :return:
    """
    print("Prof5-转职为学者分支、工程师分支、重炮手分支")
    Skill.Skill_Switchroles(5)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # Prof5-转职为学者分支、工程师分支
    Skill.Prof1_zhiye()  # Prof5-转职为学者分支、工程师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof5-转职为学者分支、工程师分支、重炮手分支
    """点击重炮手职业"""
    Skill.Prof1_zhiye()  # Prof5-转职为学者分支、工程师分支、重炮手分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块




def test_Prof1_20():  # Prof5-转职为学者分支、工程师分支、机械大师分支
    """
        Prof5-转职为学者分支、工程师分支、机械大师分支
    :return:
    """
    print("Prof5-转职为学者分支、工程师分支、机械大师分支")
    Skill.Skill_Switchroles(5)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # Prof5-转职为学者分支、工程师分支
    Skill.Prof1_zhiye()  # Prof5-转职为学者分支、工程师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof5-转职为学者分支、工程师分支、机械大师分支
    """点击机械大师职业"""
    Skill.Prof1_zhiye()  # Prof5-转职为学者分支、工程师分支、机械大师分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块




def test_Prof1_21():  # Prof5-转职为学者分支、炼金术士分支、炼金圣士分支
    """
        Prof5-转职为学者分支、炼金术士分支、炼金圣士分支
    :return:
    """
    print("Prof5-转职为学者分支、炼金术士分支、炼金圣士分支")
    Skill.Skill_Switchroles(5)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof5-转职为学者分支、炼金术士分支
    Skill.Prof1_zhiye()  # Prof5-转职为学者分支、工程师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof5-转职为学者分支、炼金术士分支、炼金圣士分支
    """点击炼金圣士职业"""
    Skill.Prof1_zhiye()  # Prof5-转职为学者分支、炼金术士分支、炼金圣士分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块




def test_Prof1_22():  # Prof5-转职为学者分支、炼金术士分支、药剂师分支
    """
         Prof5-转职为学者分支、炼金术士分支、药剂师分支
    :return:
    """
    print(" Prof5-转职为学者分支、炼金术士分支、药剂师分支")
    Skill.Skill_Switchroles(5)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof5-转职为学者分支、炼金术士分支
    Skill.Prof1_zhiye()  # Prof5-转职为学者分支、工程师分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  #  Prof5-转职为学者分支、炼金术士分支、药剂师分支
    """点击药剂师分支职业"""
    Skill.Prof1_zhiye()  #  Prof5-转职为学者分支、炼金术士分支、药剂师分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块



"""
---------------------------------------------以下为刺客分支---------------------------------------------
"""




def test_Prof1_23():  # Prof6-转职为刺客分支、暗之使徒分支、烈分支
    """
         Prof6-转职为刺客分支、暗之使徒分支、烈分支
    :return:
    """
    print(" Prof6-转职为刺客分支、暗之使徒分支、烈分支")
    Skill.Skill_Switchroles(6)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # Prof6-转职为刺客分支、暗之使徒分支
    Skill.Prof1_zhiye()  # Prof6-转职为刺客分支、暗之使徒分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof6-转职为刺客分支、暗之使徒分支、烈分支
    """点击烈职业"""
    Skill.Prof1_zhiye()  #  PProf6-转职为刺客分支、暗之使徒分支、烈分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块





def test_Prof1_24():  # Prof6-转职为刺客分支、暗之使徒分支、影分支
    """
         Prof6-转职为刺客分支、暗之使徒分支、影分支
    :return:
    """
    print(" Prof6-转职为刺客分支、暗之使徒分支、烈分支")
    Skill.Skill_Switchroles(6)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # Prof6-转职为刺客分支、暗之使徒分支
    Skill.Prof1_zhiye()  # Prof6-转职为刺客分支、暗之使徒分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof6-转职为刺客分支、暗之使徒分支、影分支
    """点击影职业"""
    Skill.Prof1_zhiye()  # Prof6-转职为刺客分支、暗之使徒分支、影分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块





def test_Prof1_25():  # Prof6-转职为刺客分支、光明之怒分支、耀分支
    """
         Prof6-转职为刺客分支、光明之怒分支、耀分支
    :return:
    """
    print(" Prof6-转职为刺客分支、光明之怒分支、耀分支")
    Skill.Skill_Switchroles(6)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof6-转职为刺客分支、光明之怒分支
    Skill.Prof1_zhiye()  # Prof6-转职为刺客分支、光明之怒分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof6-转职为刺客分支、光明之怒分支、耀分支
    """点击耀职业"""
    Skill.Prof1_zhiye()  # Prof6-转职为刺客分支、光明之怒分支、耀分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块





def test_Prof1_26():  # Prof6-转职为刺客分支、光明之怒分支、暗分支
    """
         Prof6-转职为刺客分支、光明之怒分支、暗分支
    :return:
    """
    print(" Prof6-转职为刺客分支、光明之怒分支、暗分支")
    Skill.Skill_Switchroles(6)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof6-转职为刺客分支、光明之怒分支
    Skill.Prof1_zhiye()  # Prof6-转职为刺客分支、光明之怒分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof6-转职为刺客分支、光明之怒分支、暗分支
    """点击暗职业"""
    Skill.Prof1_zhiye()  # Prof6-转职为刺客分支、光明之怒分支、暗分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


"""
---------------------------------------------以下为舞娘分支---------------------------------------------
"""





def test_Prof1_27():  # Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
    """
         Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
    :return:
    """
    print(" Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支")
    Skill.Skill_Switchroles(7)
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # PProf7-转职为舞娘分支、呐喊者分支
    Skill.Prof1_zhiye()  # Prof7-转职为舞娘分支、呐喊者分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
    """点击噬魂者职业"""
    Skill.Prof1_zhiye()  # Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块






def test_Prof1_28():  # Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支
    """
         Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支
    :return:
    """
    print(" Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支")
    Skill.Skill_Switchroles(7)  # 选择角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail1").click()  # PProf7-转职为舞娘分支、呐喊者分支
    Skill.Prof1_zhiye()  # Prof7-转职为舞娘分支、呐喊者分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支
    """点击黑暗萨满职业"""
    Skill.Prof1_zhiye()  # Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块



def test_Prof1_29():  # Prof7-转职为舞娘分支、舞者分支、灵魂舞者分支
    """
         Prof7-转职为舞娘分支、舞者分支、灵魂舞者分支
    :return:
    """
    print(" Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支")
    Skill.Skill_Switchroles(7)  # 选择角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof7-转职为舞娘分支、舞者分支
    Skill.Prof1_zhiye()  # Prof7-转职为舞娘分支、舞者分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail1").click()  # Prof7-转职为舞娘分支、舞者分支、灵魂舞者分支
    """点击灵魂舞者职业"""
    Skill.Prof1_zhiye()  # Prof7-转职为舞娘分支、舞者分支、灵魂舞者分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块




def test_Prof1_30():  # Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支
    """
         Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支
    :return:
    """
    print("Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支")
    Skill.Skill_Switchroles(7)  # 选择角色职业
    poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()  # 点击15级转职
    poco("ProDetail2").click()  # Prof7-转职为舞娘分支、舞者分支
    Skill.Prof1_zhiye()  # Prof7-转职为舞娘分支、舞者分支
    poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()  # 点击二转职业
    poco("ProDetail2").click()  # Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支
    """点击刀锋舞者职业"""
    Skill.Prof1_zhiye()  # Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支
    print("当前转职为" + poco("SkillTree(Clone)").offspring("item2").child("SelectedTextLabel").get_text())
    Skill.juexing()  # 点击觉醒
    return Skill.Skill()  # 测试技能模块


# test_Prof1_1()
