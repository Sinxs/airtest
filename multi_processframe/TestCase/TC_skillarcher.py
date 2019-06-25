# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCskilldance(unittest.TestCase):
        u'''测试用例舞娘的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Archer_1(self):
            """
            技能测试--弓箭手转职--魔羽
            """
            try:
                print("测试Prof2-转职为弓箭手分支、箭神分支、魔羽分支")
                self.assertEqual("魔羽", skill.test_Archer_1(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "魔羽-职业技能测试")

        def test_Archer_2(self):
            """
            技能测试--弓箭手转职--狙翎
            """
            try:
                print("测试Prof2-转职为弓箭手分支、箭神分支、狙翎分支")
                self.assertEqual("狙翎", skill.test_Archer_2(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "狙翎-职业技能测试")

        def test_Archer_3(self):
            """
            技能测试--弓箭手转职--银色猎人
            """
            try:
                print("测试Prof2-转职为弓箭手分支、猎人分支、银色猎人分支")
                self.assertEqual("银色猎人", skill.test_Archer_3(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "银色猎人-职业技能测试")

        def test_Archer_4(self):
            """
            技能测试--弓箭手转职--风行者
            """
            try:
                print("测试Prof2-转职为弓箭手分支、猎人分支、风行者分支")
                self.assertEqual("风行者", skill.test_Archer_4(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "影舞者-职业技能测试")

        def test_Archer_5(self):
            """
            技能测试--弓箭手转职--影舞者
            """
            try:
                print("测试Prof2-转职为弓箭手分支、猎人分支、影舞者分支")
                self.assertEqual("影舞者", skill.test_Archer_5(devices))

            finally:
                screenshot.get_screen_shot(time.time(), devices, "影舞者-职业技能测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCskilldance)
    return srcSuite
