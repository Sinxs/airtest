# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import skill
from multi_processframe.Tools import initial, screenshot, printcolor
from poco.utils.simplerpc import simplerpc

def Main(devices):
    class TCskillwarrior(unittest.TestCase):
        u'''测试用例战士的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Prof1_1(self):
            """
            战士转职为月之领主的技能测试
            """
            try:
                print("测试转职为战士分支、剑圣分支、月之领主职业")
                self.assertEqual("月之领主", skill.test_warrior_1(devices))
            except simplerpc.RpcTimeoutError:
                printcolor.printred("————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                initial.startgame(devices)
                self.assertEqual("月之领主", skill.test_warrior_1(devices))
            except Exception as e:
                print(e)
            finally:
                screenshot.get_screen_shot(time.time(), devices, "月之领主-职业技能测试")



        def test_Prof1_2(self):
            """
            战士转职为剑皇的技能测试
            """
            try:
                print("是测试转转职为战士分支、剑圣分支、剑皇职业")
                self.assertEqual("剑皇", skill.test_warrior_2(devices))
            except simplerpc.RpcTimeoutError:
                printcolor.printred("————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                initial.startgame(devices)
                self.assertEqual("剑皇", skill.test_warrior_2(devices))
            except Exception as e:
                print(e)
            finally:
                screenshot.get_screen_shot(time.time(), devices, "剑皇-职业技能测试")


        def test_Prof1_3(self):
            """
            战士转职为黑暗复仇者的技能测试
            """
            try:
                print("测试转职为战士分支、剑圣分支、复仇者、黑暗复仇者职业")
                self.assertEqual("黑暗复仇者", skill.test_warrior_3(devices))
            except simplerpc.RpcTimeoutError:
                printcolor.printred("————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                initial.startgame(devices)
                self.assertEqual("黑暗复仇者", skill.test_warrior_3(devices))
            except Exception as e:
                print(e)
            finally:
                screenshot.get_screen_shot(time.time(), devices, "黑暗复仇者-职业技能测试")


        def test_Prof1_4(self):
            """
            战士转职为狂战士的技能测试
            """
            try:
                print(" Prof1- 转职为战士分支、战神分支、毁灭者者职业")
                self.assertEqual("狂战士", skill.test_warrior_4(devices))
            except simplerpc.RpcTimeoutError:
                printcolor.printred("————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                initial.startgame(devices)
                self.assertEqual("狂战士", skill.test_warrior_4(devices))
            except Exception as e:
                print(e)
            finally:
                screenshot.get_screen_shot(time.time(), devices, "狂战士-职业技能测试")

        def test_Prof1_5(self):
            """
            战士转职为毁灭者的技能测试
            """
            try:
                print(" Prof1- 转职为战士分支、战神分支、毁灭者者职业")
                self.assertEqual("毁灭者", skill.test_warrior_5(devices))
            except simplerpc.RpcTimeoutError:
                printcolor.printred("————————————————————————————————————Rpc重连失败，脚本重新启动————————————————————————————————————")
                initial.startgame(devices)
                self.assertEqual("毁灭者", skill.test_warrior_5(devices))
            except Exception as e:
                print(e)
            finally:
                screenshot.get_screen_shot(time.time(), devices, "毁灭者-职业技能测试")




        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCskillwarrior)
    return srcSuite
