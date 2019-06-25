# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import skill
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
            技能测试--舞娘转职--噬魂者
            """
            try:
                print("测试Prof7-转职为舞娘分支、呐喊者分支、噬魂者分支")
                self.assertEqual("噬魂者", skill.test_dance_1(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "噬魂者-职业技能测试")

        def test_dance_2(self):
            """
             技能测试--舞娘转职--黑暗萨满
            """
            try:
                print("测试Prof7-转职为舞娘分支、呐喊者分支、黑暗萨满分支")
                self.assertEqual("黑暗萨满", skill.test_dance_2(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "黑暗萨满-职业技能测试")




        def test_dance_3(self):
            """
               技能测试--舞娘转职--灵魂舞者
            """
            try:
                print("测试rof7-转职为舞娘分支、舞者分支、灵魂舞者分支")
                self.assertEqual("灵魂舞者", skill.test_dance_3(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "灵魂舞者-职业技能测试")


        def test_dance_4(self):
            """
            技能测试--舞娘转职--刀锋舞者
            """
            try:
                print("测试Prof7-转职为舞娘分支、舞者分支、刀锋舞者分支")
                self.assertEqual("刀锋舞者", skill.test_dance_4(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "刀锋舞者-职业技能测试")



        def test_dance_5(self):
            """
            技能测试--舞娘转职--银色舞灵
            """
            try:
                print("测试Prof7-转职为舞娘分支、舞灵分支、银色舞灵分支")
                self.assertEqual("银色舞灵", skill.test_dance_5(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "银色舞灵-职业技能测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkilldance)
    return srcSuite
