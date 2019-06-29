# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import main_ectype
from multi_processframe.Tools import initial, screenshot, printcolor
from poco.utils.simplerpc import simplerpc


def Main(devices):
    class TC_chapter_9(unittest.TestCase):
        u'''测试用例TCmainectype_chapter_one的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Chapter_9(self):
            """
            主线关卡第九章战斗流程测试--测试自动通关副本，检测地图卡点，对于没有自动战斗的关卡进入副本后退出
            """
            try:
                self.assertEqual("Duck", main_ectype.chapter_nine(devices))
            except simplerpc.RpcTimeoutError:
                printcolor.printred(
                    "————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                initial.startgame(devices)
                self.assertEqual("Duck", main_ectype.chapter_nine(devices))
            except Exception as e:
                print(e)

            finally:
                screenshot.get_screen_shot(time.time(), devices, "主线关卡测试脚本")

        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_chapter_9)
    return srcSuite
