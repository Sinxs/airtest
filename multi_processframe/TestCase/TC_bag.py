# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import bag
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TC_bag(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_bag(self):
            """
            背包功能测试模块--背包分类，背包扩展的操作
            """
            try:
                self.assertEqual("Duck", bag.bag_item(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "龙器功能测试模块")

        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_bag)
    return srcSuite
