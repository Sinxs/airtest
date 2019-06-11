# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import setting
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCsetting(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_setting(self):
            """
            设置测试模块--主要检测每个按钮点击是否正常，界面是否可以打开
            """
            try:
                self.assertEqual("Duck", setting.setting(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "设置模块截图")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}当前用例结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCsetting)
    return srcSuite
