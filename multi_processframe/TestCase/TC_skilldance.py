# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.skill import Skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCSkilldance(unittest.TestCase):
        u'''测试用例舞娘的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_dance_1(self):
            """
            这是测试Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支
            return:
            """
            try:
                print("测试Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支")
                self.assertEqual("噬魂者", Skill.test_dance_1(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_dance_2(self):
            """
            这是测试Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支
            return:
            """
            try:
                print("测试Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支")
                self.assertEqual("黑暗萨满", Skill.test_dance_2(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)




        def test_dance_3(self):
            """
            这是测试rof7-转职为舞娘分支、舞者分支、灵魂舞者分支
            return:
            """
            try:
                print("测试rof7-转职为舞娘分支、舞者分支、灵魂舞者分支")
                self.assertEqual("灵魂舞者", Skill.test_dance_3(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "战士角色技能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)


        def test_dance_4(self):
            """
            这是测试Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支
            return:
            """
            try:
                print("测试Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支")
                self.assertEqual("刀锋舞者", Skill.test_dance_4(devices))
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

    srcSuite = unittest.makeSuite(TCSkilldance)
    return srcSuite
