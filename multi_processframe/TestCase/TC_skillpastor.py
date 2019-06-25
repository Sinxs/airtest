# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCskillpastor(unittest.TestCase):
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
                self.assertEqual("雷神", skill.test_pastor_1(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "雷神-职业技能测试")



        def test_pastor_2(self):
            """
            技能测试--牧师转职--圣徒
            """
            try:
                print("测试Prof4-转职为牧师分支、祭祀分支、圣徒分支")
                self.assertEqual("圣徒", skill.test_pastor_2(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "圣徒-职业技能测试")



        def test_pastor_3(self):
            """
            技能测试--牧师转职--十字军
            """
            try:
                print("测试Prof4-转职为牧师分支、祭祀分支、十字军分支")
                self.assertEqual("十字军", skill.test_pastor_3(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "十字军-职业技能测试")



        def test_pastor_4(self):
            """
            技能测试--牧师转职--圣骑士
            """
            try:
                print("测试Prof4-转职为牧师分支、祭祀分支、圣骑士分支")
                self.assertEqual("圣骑士", skill.test_pastor_4(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "圣骑士-职业技能测试")


        def test_pastor_5(self):
            """
            技能测试--牧师转职--黑暗教主
            """
            try:
                print("测试Prof4-转职为牧师分支、教主分支、黑暗教主分支")
                self.assertEqual("黑暗教主", skill.test_pastor_5(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "黑暗教主-职业技能测试")



        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCskillpastor)
    return srcSuite
