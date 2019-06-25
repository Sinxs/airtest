# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCskillthug(unittest.TestCase):
        u'''测试用例以下为刺客分支的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_thug_1(self):
            """
            技能测试--刺客转职--烈
            """
            try:
                print("测试Prof6-转职为刺客分支、暗之使徒分支、烈分支")
                self.assertEqual("烈", skill.test_thug_1(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "烈-职业技能测试")



        def test_thug_2(self):
            """
            技能测试--刺客转职--影
            """
            try:
                print("测试Prof6-转职为刺客分支、暗之使徒分支、影分支")
                self.assertEqual("影", skill.test_thug_2(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "影-职业技能测试")



        def test_thug_3(self):
            """
             技能测试--刺客转职--耀
            """
            try:
                print("测试Prof6-转职为刺客分支、光明之怒分支、耀分支")
                self.assertEqual("耀", skill.test_thug_3(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "耀-职业技能测试")



        def test_thug_4(self):
            """
               技能测试--刺客转职--暗
            """
            try:
                print("测试Prof6-转职为刺客分支、光明之怒分支、暗分支")
                self.assertEqual("暗", skill.test_thug_4(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "暗-职业技能测试")




        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCskillthug)
    return srcSuite
