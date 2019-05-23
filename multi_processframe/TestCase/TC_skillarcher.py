# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.skill import Skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCSkillProf3(unittest.TestCase):
        u'''测试用例以下为弓箭手分支的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Prof1_6(self):
            """
            这是测试Prof2-转职为弓箭手分支、箭神分支、魔羽分支
            """
            print("测试Prof2-转职为弓箭手分支、箭神分支、魔羽分支")
            self.assertEqual("魔羽", Skill.test_Prof1_6(devices))
            screenshot.get_screen_shot(time.time(), devices, "弓箭手角色技能测试脚本")

        def test_Prof1_7(self):
            """
            这  Prof2-转职为弓箭手分支、箭神分支、魔羽分支
            return:
            """
            print("测试Prof2-转职为弓箭手分支、箭神分支、魔羽分支")
            self.assertEqual("狙翎", Skill.test_Prof1_7(devices))
            screenshot.get_screen_shot(time.time(), devices, "弓箭手角色技能测试脚本")

        def test_Prof1_8(self):
            """
            这是测试Prof2-转职为弓箭手分支、猎人分支、银色猎人分支
            return:
            """
            print("测试Prof2-转职为弓箭手分支、猎人分支、银色猎人分支")
            self.assertEqual("银色猎人", Skill.test_Prof1_8(devices))
            screenshot.get_screen_shot(time.time(), devices, "弓箭手角色技能测试脚本")

        def test_Prof1_9(self):
            """
            这是测试 Prof2-转职为弓箭手分支、游侠分支、风行者分支
            return:
            """
            print("测试Prof2-转职为弓箭手分支、猎人分支、风行者分支")
            self.assertEqual("风行者", Skill.test_Prof1_9(devices))
            screenshot.get_screen_shot(time.time(), devices, "弓箭手角色技能测试脚本")

        def test_Prof1_10(self):
            """
            这是测试Prof2-转职为弓箭手分支、游侠分支、影舞者分支
            return:
            """
            print("测试Prof2-转职为弓箭手分支、猎人分支、影舞者分支")
            self.assertEqual("影舞者", Skill.test_Prof1_10(devices))
            screenshot.get_screen_shot(time.time(), devices, "弓箭手角色技能测试脚本")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkillProf3)
    return srcSuite
