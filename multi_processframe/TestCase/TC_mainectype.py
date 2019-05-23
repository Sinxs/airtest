# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.mainectype import main_ectype
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCmainectype(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Chapter_One(self):
            """
            返回关卡完成回到主界面
            """
            try:
                self.assertEqual("Duck", main_ectype.test_Chapter_One(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "主线关卡测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCmainectype)
    return srcSuite
