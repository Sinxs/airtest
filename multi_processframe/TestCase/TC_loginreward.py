
# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import loginreward
from multi_processframe.Tools import initial, screenshot

def Main(devices):
    class TC_loginreward(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_loginreward(self):
            """
            登陆奖励-可以领取的奖励全部领取，判断界面元素
            """
            try:
                print("开始测试登陆奖励模块")
                self.assertEqual("Title", loginreward.loginreward(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "登陆奖励-冒烟测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_loginreward)
    return srcSuite
