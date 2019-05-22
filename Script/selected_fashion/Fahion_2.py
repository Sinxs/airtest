# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from poco.drivers.unity3d import *
poco = UnityPoco()
from Selected_fashion import fashion_1


def test_Prof1fashion_1():  # Prof1-转职为战士分支、剑圣分支、月之领主职业
    fashion_1.Switchroles_1()
    fashion_1.Switchroles_2(1)
    fashion_1.Fashion_text1()
    return poco("title_back").child("Title").get_text()



def test_Prof1fashion_2():  # Prof2-转职为弓箭手分支、箭神分支、魔羽分支
    # fashion_1.Switchroles_1()
    # fashion_1.Switchroles_2(2)
    # fashion_1.Fashion_text1()
    return poco("title_back").child("Title").get_text()



def test_Prof1fashion_3():  # Prof3-转职为魔法师分支、元素分支、冰灵分支
    fashion_1.Switchroles_1()
    fashion_1.Switchroles_2(3)
    fashion_1.Fashion_text1()
    return poco("title_back").child("Title").get_text()

def test_Prof1fashion_4(): # Prof4-转职为牧师分支、祭祀分支、雷神分支
    fashion_1.Switchroles_1()
    fashion_1.Switchroles_2(4)
    fashion_1.Fashion_text1()
    return poco("title_back").child("Title").get_text()

def test_Prof1fashion_5():  # Prof5-转职为学者分支、工程师分支、重炮手分支
    fashion_1.Switchroles_1()
    fashion_1.Switchroles_2(5)
    fashion_1.Fashion_text1()
    return poco("title_back").child("Title").get_text()

def test_Prof1fashion_6():  # Prof6-转职为刺客分支、暗之使徒分支、烈分支
    fashion_1.Switchroles_1()
    fashion_1.Switchroles_2(6)
    fashion_1.Fashion_text1()
    return poco("title_back").child("Title").get_text()

def test_Prof1fashion_7():  # Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
    fashion_1.Switchroles_1()
    fashion_1.Switchroles_2(7)
    fashion_1.Fashion_text1()
    return poco("title_back").child("Title").get_text()
