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
            战士转职为月之领主的技能测试
            """
            try:
                print("测试转职为战士分支、剑圣分支、月之领主职业")
                self.assertEqual("月之领主", Skill.test_warrior_1(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)



        def test_Prof1_2(self):
            """
            战士转职为剑皇的技能测试
            """
            try:
                print("是测试转转职为战士分支、剑圣分支、剑皇职业")
                self.assertEqual("剑皇", Skill.test_warrior_2(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)



        def test_Prof1_3(self):
            """
            战士转职为黑暗复仇者的技能测试
            """
            try:
                print("测试转职为战士分支、剑圣分支、复仇者、黑暗复仇者职业")
                self.assertEqual("黑暗复仇者", Skill.test_warrior_3(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)



        def test_Prof1_4(self):
            """
            战士转职为狂战士的技能测试
            """
            try:
                self.assertEqual("狂战士", Skill.test_warrior_4(devices))
                screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)


        def test_Prof1_5(self):
            """
            战士转职为毁灭者的技能测试
            """
            try:
                print(" Prof1- 转职为战士分支、战神分支、毁灭者者职业")
                self.assertEqual("毁灭者", Skill.test_warrior_5(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)




        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkillwarrior)
    return srcSuite
