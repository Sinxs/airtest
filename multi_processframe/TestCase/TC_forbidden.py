# -*- coding: utf-8 -*-
__author__ = "sinwu"

import unittest
from airtest.core.api import *
from Script.smoking import longhunforbidden
from multi_processframe.Tools import initial, screenshot
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def Main(devices):
    class TC_longhunforbidden(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_longhunforbidden(self):
            """
            龙魂禁地-判断龙魂禁地界面的控件元素，掉落图鉴的物品道具，没有进入副本
            """
            try:
                print("开始测试龙魂禁地模块")
                self.assertEqual("奖励预览", longhunforbidden.longhunforbidden(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "龙魂禁地-冒烟测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_longhunforbidden)
    return srcSuite
