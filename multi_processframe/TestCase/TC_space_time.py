# -*- coding: utf-8 -*-
__author__ = "sinwu"

import unittest
from airtest.core.api import *
from Script.smoking import spacetime
from multi_processframe.Tools import initial, screenshot
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def Main(devices):
    class TC_space_time(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_task(self):
            """
            时空裂缝--界面元素判断，按钮点击
            """
            try:
                print("开始测试时空裂缝模块")
                self.assertEqual("排名奖励", spacetime.space_time(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "时空裂缝-冒烟测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_space_time)
    return srcSuite
