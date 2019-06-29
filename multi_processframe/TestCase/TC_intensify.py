
# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import intensify
from multi_processframe.Tools import initial, screenshot, printcolor
from poco.utils.simplerpc import simplerpc


def Main(devices):
    class TC_intensify(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_intensify(self):
            """
            变强模块-一级界面控件控件判断
            """
            try:
                print("开始测试变强模块")
                self.assertEqual("对应的活跃度宝箱打开随机获得水晶", intensify.Intensify(devices))
            except simplerpc.RpcTimeoutError:
                printcolor.printred("————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                initial.startgame(devices)
                self.assertEqual("对应的活跃度宝箱打开随机获得水晶", intensify.Intensify(devices))
            except Exception as e:
                print(e)
            finally:
                screenshot.get_screen_shot(time.time(), devices, "变强模块-冒烟测试")

        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_intensify)
    return srcSuite
