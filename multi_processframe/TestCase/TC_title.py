# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.title import title_test
from multi_processframe.Tools import initial, screenshot
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def Main(devices):
    class TChorse(unittest.TestCase):
        u'''测试用例101的集合'''
        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            poco = UnityPoco()
            initial.startgame(devices, poco)

        def  test_test_Horse(self):
            """
            这是测试称号的用例:return: 返回最后一个坐骑的按钮状态
            """

            poco = UnityPoco()
            self.assertEqual("称 号", title_test.test_titletets0(poco))
            screenshot.get_screen_shot(time.time(), devices, "称号功能测试脚本")

        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TChorse)
    return srcSuite
