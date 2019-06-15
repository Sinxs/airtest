# -*- coding: utf-8 -*-
__author__ = "sinwu"

import unittest
from airtest.core.api import *
from Script.smoking import home
from multi_processframe.Tools import initial, screenshot
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def Main(devices):
    class TC_home(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_home(self):
            """
            家园-冒烟测试
            """
            try:
                print("开始测试家园模块")
                self.assertEqual("腊八粥宴", home.home(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "家园-冒烟测试")

        def test_entrancehome(self):
            """
            进入家园-控件判断-钓鱼一次
            """
            try:
                print("开始测试进入家园模块")
                self.assertEqual("社交", home.entrancehome(devices))
            finally:
                if poco("ExitHome").exists():
                    poco("ExitHome").click()  # 返回主界面
                    sleep(15)
                screenshot.get_screen_shot(time.time(), devices, "进入家园-冒烟测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_home)
    return srcSuite
