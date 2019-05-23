# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.horse import horse
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TChorse(unittest.TestCase):
        u'''测试用例101的集合'''
        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def  test_test_Horse(self):
            """
            这是测试坐骑的用例:return: 返回最后一个坐骑的按钮状态
            """
            try:
                self.assertEqual("Btnhave", horse.test_Horse(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "坐骑功能测试脚本")
                self.assertEqual("此条的信息请忽略",start_Screenshot)

        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TChorse)
    return srcSuite
