# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.title import title_test
from multi_processframe.Tools import initial, screenshot
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def Main(devices):
    class test_titletets(unittest.TestCase):
        u'''测试用例101的集合'''
        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''

            initial.startgame(devices)

        def  test_titletets0(self):
            """
             测试--普通称号
            """
            try:
                print("普通称号测试")
                self.assertEqual("称 号", title_test.test_titletets0(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "称号功能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)



        def  test_titletets1(self):
            """
            测试--副本称号
            """
            try:
                print("副本称号测试")
                self.assertEqual("称 号", title_test.test_titletets1(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "称号功能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)



        def  test_titletets2(self):
            """
            测试--巢穴称号
            """
            try:
                print("巢穴称号测试")
                self.assertEqual("称 号", title_test.test_titletets2(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "称号功能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)



        def test_titletets3(self):
            """
            测试--限时称号
            """
            try:
                print("限时称号测试")
                self.assertEqual("称 号", title_test.test_titletets3(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "称号功能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)


        def test_titletets4(self):
            """
            测试--活动称号
            """
            try:
                print("活动称号测试")
                self.assertEqual("称 号", title_test.test_titletets4(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "称号功能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)


        def test_titletets5(self):
            """
            测试--限时称号
            """
            try:
                print("限时称号测试")
                self.assertEqual("称 号", title_test.test_titletets5(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "称号功能测试脚本")
                self.assertEqual("此条的信息请忽略", start_Screenshot)


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(test_titletets)
    return srcSuite
