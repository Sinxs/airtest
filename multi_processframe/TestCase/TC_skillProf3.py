# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.skill import Skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCSkillProf2(unittest.TestCase):
        u'''测试用例以下为魔法师分支的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Prof1_11(self):
            """
            这是测试Prof3-转职为魔法师分支、元素分支、冰灵分支
            return:
            """
            print("测试Prof3-转职为魔法师分支、元素分支、冰灵分支")
            self.assertEqual("冰灵", Skill.test_Prof1_11(devices))
            screenshot.get_screen_shot(time.time(), devices, "魔法师角色技能测试脚本")

        def test_Prof1_12(self):
            """
            这是测试 Prof3-转职为魔法师分支、元素分支、火舞分支
            return:
            """
            print("测试Prof3-转职为魔法师分支、元素分支、火舞分支")
            self.assertEqual("火舞", Skill.test_Prof1_12(devices))
            screenshot.get_screen_shot(time.time(), devices, "魔法师角色技能测试脚本")

        def test_Prof1_13(self):
            """
            这是测试Prof3-转职为魔法师分支、魔导师分支、黑暗女王分支
            return: 返回关卡完成回到主界面
            """
            print("测试Prof3-转职为魔法师分支、元素分支、黑暗女王分支")
            self.assertEqual("黑暗女王", Skill.test_Prof1_13(devices))
            screenshot.get_screen_shot(time.time(), devices, "魔法师角色技能测试脚本")

        def test_Prof1_14(self):
            """
            这是测试Prof3-转职为魔法师分支、魔导师分支、时空领主分支
            return: 返回关卡完成回到主界面
            """
            print("测试Prof3-转职为魔法师分支、元素分支、时空领主分支")
            self.assertEqual("时空领主", Skill.test_Prof1_14(devices))
            screenshot.get_screen_shot(time.time(), devices, "魔法师角色技能测试脚本")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkillProf2)
    return srcSuite
