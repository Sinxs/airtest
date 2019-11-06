
# -*- coding: utf-8 -*-
__author__ = "Lee.li"
from multi_processframe.ProjectTools.common import *
import unittest
from airtest.core.api import *
from Script.smoking import bossrush
from multi_processframe.ProjectTools import initial, common
from poco.utils.simplerpc import simplerpc

def Main(start, devices):
    class TC_bossrush(unittest.TestCase):
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
                        common.printred(
                            "————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                        initial.startgame(devices)
                        common.get_screen_shot(start, time.time(), devices, "重置脚本环境")
                        break
                    except simplerpc.RpcTimeoutError:
                        common.printred(
                            "————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                        initial.startgame(devices)
                        common.get_screen_shot(start, time.time(), devices, "重置脚本环境")

        def test_bossrush(self):
            """
            bossrush -- bossrush界面判断
            """
            try:
                print("开始测试bossrush模块")
                self.assertEqual("本次挑战增益", bossrush.bossrush(start, devices))
            except simplerpc.RpcTimeoutError:
                for i in range(initial.RpcTimeoutime()):  # rpc超时问题重置次数
                    try:
                        common.printred(
                            "————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                        initial.startgame(devices)
                        self.assertEqual("本次挑战增益", bossrush.bossrush(start, devices))
                        break
                    except simplerpc.RpcTimeoutError:
                        common.printred(
                            "————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                        initial.startgame(devices)
                        self.assertEqual("本次挑战增益", bossrush.bossrush(start, devices))


            finally:
                common.get_screen_shot(start, time.time(), devices, "bossrush-冒烟测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            common.set_config("bossrush")
            goback(devices)
            pass

    srcSuite = unittest.makeSuite(TC_bossrush)
    return srcSuite
