# -*- coding: utf-8 -*-
__author__ = "sinwu"

import unittest
from airtest.core.api import *
from Script.smoking import longxue
from multi_processframe.Tools import initial, screenshot
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def Main(devices):
    class TC_longxue(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_longxue(self):
            """
            龙穴-判断每个龙穴界面控件元素，进行按钮 and icon 点击
            """
            try:
                print("开始测试龙穴模块")
                self.assertEqual("玛蒙的竞技场-困难", longxue.longxue(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "龙穴-冒烟测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_longxue)
    return srcSuite
