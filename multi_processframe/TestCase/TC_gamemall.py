# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import gamemall
from multi_processframe.Tools import initial, screenshot

def Main(devices):
    class TC_gamemall(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_gamemall(self):
            """
            商城-界面控件判断-售卖商品判断
            """
            try:
                print("开始测试商店模块")
                self.assertEqual("充 值", gamemall.gamemall(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "商城-冒烟测试")

        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_gamemall)
    return srcSuite
