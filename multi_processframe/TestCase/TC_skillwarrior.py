# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.skill import Skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCSkillwarrior(unittest.TestCase):
        u'''测试用例战士的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Prof1_1(self):
            """
            这是测试转职为战士分支、剑圣分支、月之领主职业:
            return:
            """
            print("测试转职为战士分支、剑圣分支、月之领主职业")
            self.assertEqual("月之领主", Skill.test_Prof1_1(devices))
            screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")

        def test_Prof1_2(self):
            """
            这是测试转转职为战士分支、剑圣分支、剑皇职业
            return: 返回关卡完成回到主界面
            """
            print("是测试转转职为战士分支、剑圣分支、剑皇职业")
            self.assertEqual("剑皇", Skill.test_Prof1_2(devices))
            screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")

        def test_Prof1_3(self):
            """
            这是测试转职为战士分支、剑圣分支、复仇者、黑暗复仇者职业
            return:
            """
            print("测试转职为战士分支、剑圣分支、复仇者、黑暗复仇者职业")
            self.assertEqual("黑暗复仇者", Skill.test_Prof1_3(devices))
            screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")

        def test_Prof1_4(self):
            """
            这是测试 Prof1- 转职为战士分支、战皇分支、狂战士职业
            return:
            """
            self.assertEqual("狂战士", Skill.test_Prof1_4(devices))
            screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")

        def test_Prof1_5(self):
            """
            这是测试  Prof1- 转职为战士分支、战神分支、毁灭者者职业
            return: 返回关卡完成回到主界面
            """
            print(" Prof1- 转职为战士分支、战神分支、毁灭者者职业")
            self.assertEqual("毁灭者", Skill.test_Prof1_5(devices))
            screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkillwarrior)
    return srcSuite
