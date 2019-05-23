# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.skill import Skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCSkillProf6(unittest.TestCase):
        u'''测试用例以下为刺客分支的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Prof1_23(self):
            """
            这是测试Prof6-转职为刺客分支、暗之使徒分支、烈分支
            return: 返回关卡完成回到主界面
            """
            print("测试Prof6-转职为刺客分支、暗之使徒分支、烈分支")
            self.assertEqual("烈", Skill.test_Prof1_23(devices))
            screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")

        def test_Prof1_24(self):
            """
            这是测试Prof6-转职为刺客分支、暗之使徒分支、影分支
            return: 返回关卡完成回到主界面
            """
            print("测试Prof6-转职为刺客分支、暗之使徒分支、影分支")
            self.assertEqual("影", Skill.test_Prof1_24(devices))
            screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")

        def test_Prof1_25(self):
            """
            这是测试Prof6-转职为刺客分支、光明之怒分支、耀分支
            return: 返回关卡完成回到主界面
            """
            print("测试Prof6-转职为刺客分支、光明之怒分支、耀分支")
            self.assertEqual("耀", Skill.test_Prof1_25(devices))
            screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")

        def test_Prof1_26(self):
            """
            这是测试Prof6-转职为刺客分支、光明之怒分支、暗分支
            return: 返回关卡完成回到主界面
            """
            print("测试Prof6-转职为刺客分支、光明之怒分支、暗分支")
            self.assertEqual("暗", Skill.test_Prof1_26(devices))
            screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkillProf6)
    return srcSuite
