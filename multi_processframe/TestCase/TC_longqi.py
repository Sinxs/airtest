# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import longqi
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TClongqi(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_longyu(self):
            """
            龙器功能测试模块--主要检测龙器界面按钮，龙器穿戴，龙器获取，龙器神炉个按钮点击操作
            """
            try:
                self.assertEqual("Duck", longqi.Artifact(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "龙器功能测试模块")

        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TClongqi)
    return srcSuite