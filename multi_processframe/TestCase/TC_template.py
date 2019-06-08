# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCtemplate(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_test_Horse(self):
            """
            这是测试坐骑的用例:return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("Btnhave", "需要测试的模块")
            finally:
                screenshot.get_screen_shot(time.time(), devices, "测试模块的截图名称")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCtemplate)
    return srcSuite
