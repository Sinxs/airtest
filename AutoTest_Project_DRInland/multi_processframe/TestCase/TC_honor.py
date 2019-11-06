# -*- coding: utf-8 -*-
__author__ = "sinwu"

from multi_processframe.ProjectTools.common import *
import unittest
from airtest.core.api import *
from Script.smoking import honor
from multi_processframe.ProjectTools import initial
from poco.utils.simplerpc import simplerpc


def Main(start, devices):
    class TC_honor(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            try:
                initial.startgame(devices)
            except simplerpc.RpcTimeoutError:
                for i in range(initial.RpcTimeoutime()):  # rpc超时问题重置次数
                    try:
                        printred(
                            "————————————————————————————————————"
                            "Rpc重连失败，脚本重新启动"
                            "————————————————————————————————————")
                        initial.startgame(devices)
                        get_screen_shot(start, time.time(), devices, "重置脚本环境")
                        break
                    except simplerpc.RpcTimeoutError:
                        printred(
                            "————————————————————————————————————"
                            "Rpc重连失败，脚本重新启动"
                            "————————————————————————————————————")
                        initial.startgame(devices)
                        get_screen_shot(start, time.time(), devices, "重置脚本环境")

        def test_honor(self):
            """
            头衔模块-头衔晋升and界面判断-勋章合成and界面判断
            """
            try:
                print("开始测试头衔模块")
                self.assertEqual("背 包", honor.honor(start, devices))
            except simplerpc.RpcTimeoutError:
                for i in range(initial.RpcTimeoutime()):  # rpc超时问题重置次数
                    try:
                        printred(
                            "————————————————————————————————————"
                            "Rpc重连失败，脚本重新启动"
                            "————————————————————————————————————")
                        initial.startgame(devices)
                        self.assertEqual("背 包", honor.honor(start, devices))
                        break
                    except simplerpc.RpcTimeoutError:
                        printred(
                            "————————————————————————————————————"
                            "Rpc重连失败，脚本重新启动"
                            "————————————————————————————————————")
                        initial.startgame(devices)
                        self.assertEqual("背 包", honor.honor(start, devices))

            finally:
                get_screen_shot(start, time.time(), devices, "头衔-冒烟测试")



        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            set_config("honor")
            goback(devices)
            pass

    srcSuite = unittest.makeSuite(TC_honor)
    return srcSuite
