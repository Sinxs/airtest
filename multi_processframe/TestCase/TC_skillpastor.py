# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.skill import Skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCSkillpastor(unittest.TestCase):
        u'''测试用例以下为牧师分支的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_pastor_1(self):
            """
            技能测试--牧师转职--雷神
            """
            try:
                print("测试Prof4-转职为牧师分支、祭祀分支、雷神分支")
                self.assertEqual("雷神", Skill.test_pastor_1(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "牧师角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)


        def test_pastor_2(self):
            """
            技能测试--牧师转职--圣徒
            """
            try:
                print("测试Prof4-转职为牧师分支、祭祀分支、圣徒分支")
                self.assertEqual("圣徒", Skill.test_pastor_2(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "牧师角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)


        def test_pastor_3(self):
            """
            技能测试--牧师转职--十字军
            """
            try:
                print("测试Prof4-转职为牧师分支、祭祀分支、十字军分支")
                self.assertEqual("十字军", Skill.test_pastor_3(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "牧师角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)


        def test_pastor_4(self):
            """
            技能测试--牧师转职--圣骑士
            """
            try:
                print("测试Prof4-转职为牧师分支、祭祀分支、圣骑士分支")
                self.assertEqual("圣骑士", Skill.test_pastor_4(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "牧师角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)




        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkillpastor)
    return srcSuite
