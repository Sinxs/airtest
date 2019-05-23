# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.skill import Skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCSkillProf5(unittest.TestCase):
        u'''测试用例以下为学者分支的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Prof1_19(self):
            """
            这是测试Prof5-转职为学者分支、工程师分支、重炮手分支
            return:
            """
            print("测试Prof5-转职为学者分支、工程师分支、重炮手分支")
            self.assertEqual("重炮手", Skill.test_Prof1_19(devices))
            screenshot.get_screen_shot(time.time(), devices, "学者角色技能测试脚本")

        def test_Prof1_20(self):
            """
            这是测试Prof5-转职为学者分支、工程师分支、机械大师分支
            return:
            """
            print("测试Prof5-转职为学者分支、工程师分支、机械大师分支")
            self.assertEqual("机械大师", Skill.test_Prof1_20(devices))
            screenshot.get_screen_shot(time.time(), devices, "学者角色技能测试脚本")

        def test_Prof1_21(self):
            """
            这是测试Prof5-转职为学者分支、炼金术士分支、炼金圣士分支
            return: 返回关卡完成回到主界面
            """
            print("Prof5-转职为学者分支、炼金术士分支、炼金圣士分支")
            self.assertEqual("炼金圣士", Skill.test_Prof1_21(devices))
            screenshot.get_screen_shot(time.time(), devices, "学者角色技能测试脚本")

        def test_Prof1_22(self):
            """
            这是测试Prof5-转职为学者分支、炼金术士分支、药剂师分支
            return: 返回关卡完成回到主界面
            """
            print("Prof5-转职为学者分支、炼金术士分支、药剂师分支")
            self.assertEqual("药剂师", Skill.test_Prof1_22(devices))
            screenshot.get_screen_shot(time.time(), devices, "学者角色技能测试脚本")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkillProf5)
    return srcSuite
