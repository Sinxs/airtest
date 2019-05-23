# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.skill import Skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCSkillArcher(unittest.TestCase):
        u'''测试用例以下为弓箭手分支的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Archer_1(self):
            """
            这是测试Prof2-转职为弓箭手分支、箭神分支、魔羽分支
            """
            try:
                print("测试Prof2-转职为弓箭手分支、箭神分支、魔羽分支")
                self.assertEqual("魔羽", Skill.test_Archer_1(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "弓箭手角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_Archer_2(self):
            """
            这  Prof2-转职为弓箭手分支、箭神分支、魔羽分支
            return:
            """
            try:
                print("测试Prof2-转职为弓箭手分支、箭神分支、魔羽分支")
                self.assertEqual("狙翎", Skill.test_Archer_2(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "弓箭手角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)



        def test_Archer_3(self):
            """
            这是测试Prof2-转职为弓箭手分支、猎人分支、银色猎人分支
            return:
            """
            try:
                print("测试Prof2-转职为弓箭手分支、猎人分支、银色猎人分支")
                self.assertEqual("银色猎人", Skill.test_Archer_3(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "弓箭手角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_Archer_4(self):
            """
            这是测试 Prof2-转职为弓箭手分支、游侠分支、风行者分支
            return:
            """
            try:
                print("测试Prof2-转职为弓箭手分支、猎人分支、风行者分支")
                self.assertEqual("风行者", Skill.test_Archer_4(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "弓箭手角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)



        def test_Archer_5(self):
            """
            这是测试Prof2-转职为弓箭手分支、游侠分支、影舞者分支
            return:
            """
            try:
                print("测试Prof2-转职为弓箭手分支、猎人分支、影舞者分支")
                self.assertEqual("影舞者", Skill.test_Archer_5(devices))

            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "弓箭手角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkillArcher)
    return srcSuite
