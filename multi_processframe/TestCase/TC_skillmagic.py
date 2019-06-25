# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCskillmagic(unittest.TestCase):
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
            技能测试--魔法师转职--冰灵
            """
            try:
                print("测试Prof3-转职为魔法师分支、元素分支、冰灵分支")
                self.assertEqual("冰灵", skill.test_magic_1(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "冰灵-职业技能测试")



        def test_Prof1_12(self):
            """
              技能测试--魔法师转职--火舞
            """
            try:
                print("测试Prof3-转职为魔法师分支、元素分支、火舞分支")
                self.assertEqual("火舞", skill.test_magic_2(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "火舞-职业技能测试")



        def test_Prof1_13(self):
            """
            技能测试--魔法师转职--黑暗女王
            """
            try:
                print("测试Prof3-转职为魔法师分支、元素分支、黑暗女王分支")
                self.assertEqual("黑暗女王", skill.test_magic_3(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "黑暗女王-职业技能测试")



        def test_Prof1_14(self):
            """
            技能测试--魔法师转职--时空领主
            """
            try:
                print("测试Prof3-转职为魔法师分支、元素分支、时空领主分支")
                self.assertEqual("时空领主", skill.test_magic_4(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "时空领主-职业技能测试")




        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCskillmagic)
    return srcSuite