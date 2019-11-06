# -*- coding: utf-8 -*-
__author__ = "sinwu"

from multi_processframe.ProjectTools.common import *
import unittest
from airtest.core.api import *
from Script.smoking import home
from multi_processframe.ProjectTools import initial
from poco.utils.simplerpc import simplerpc


def Main(start, devices):
    class TC_home(unittest.TestCase):
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

        def test_home(self):
            """
            家园-家园界面控件判断、按钮点击
            """
            try:
                print("开始测试家园模块")
                self.assertEqual("腊八粥宴", home.home(start, devices))
            except simplerpc.RpcTimeoutError:
                for i in range(initial.RpcTimeoutime()):  # rpc超时问题重置次数
                    try:
                        printred(
                            "————————————————————————————————————"
                            "Rpc重连失败，脚本重新启动"
                            "————————————————————————————————————")
                        initial.startgame(devices)
                        self.assertEqual("腊八粥宴", home.home(start, devices))
                        break
                    except simplerpc.RpcTimeoutError:
                        printred(
                            "————————————————————————————————————"
                            "Rpc重连失败，脚本重新启动"
                            "————————————————————————————————————")
                        initial.startgame(devices)
                        self.assertEqual("腊八粥宴", home.home(start, devices))

            finally:
                get_screen_shot(start, time.time(), devices, "家园-冒烟测试")
        # todo: 以下是进入家园的脚本，因为涉及到场景切换，所以暂时屏蔽
        # def test_entrancehome(self):
        #     """
        #     进入家园-控件判断-钓鱼一次
        #     """
        #     try:
        #         print("开始测试进入家园模块")
        #         self.assertEqual("社交", home.entrancehome(start, devices))
        #     except simplerpc.RpcTimeoutError:
        #         for i in range(initial.RpcTimeoutime()):  # rpc超时问题重置次数
        #             try:
        #                 printred(
        #                                                 
        #                     "————————————————————————————————————"
        #                     "Rpc重连失败，脚本重新启动"
        #                     "————————————————————————————————————")
        #                 initial.startgame(devices)
        #                 self.assertEqual("社交", home.entrancehome(start, devices))
        #                 break
        #             except simplerpc.RpcTimeoutError:
        #                 printred(
        #                                                 
        #                     "————————————————————————————————————"
        #                     "Rpc重连失败，脚本重新启动"
        #                     "————————————————————————————————————")
        #                 initial.startgame(devices)
        #                 self.assertEqual("社交", home.entrancehome(start, devices))
        #
        #     except Exception as e:
        #         print(e)
        #     finally:
        #         poco = UnityPoco()
        #         if poco("ExitHome").exists():
        #             poco("ExitHome").click()  # 返回主界面
        #             sleep(15)
        #         get_screen_shot(start, time.time(), devices, "进入家园-冒烟测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            set_config("home")
            goback(devices)
            pass

    srcSuite = unittest.makeSuite(TC_home)
    return srcSuite
