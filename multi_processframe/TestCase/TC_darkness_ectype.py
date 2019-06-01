# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.darkness_ectype import darkness_ectype
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TC_darkness_ectype(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            try:
                initial.startgame(devices)
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "时装测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_fashionarcher(self):
            """
            测试--交易所功能

            """
            # ps: 因为测试环境中没有可以交易的
            try:
                print("黑暗神殿功能测试")
                self.assertEqual("黑暗神殿[-]", darkness_ectype.darkness_ectype(devices))
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

    srcSuite = unittest.makeSuite(TC_darkness_ectype)
    return srcSuite
