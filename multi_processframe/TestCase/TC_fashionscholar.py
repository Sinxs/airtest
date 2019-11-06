# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.selected_fashion import fashion
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TC_fashionscholar(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_fashionscholar(self):
            """
            测试--学者--时装
            """
            try:
                print(" Prof2-转职为学者时装模块测试")
                self.assertEqual("衣柜换装", fashion.test_fashionscholar(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "时装测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_fashionscholar)
    return srcSuite
