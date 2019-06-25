# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCSkillscholar(unittest.TestCase):
        u'''测试用例以下为学者分支的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_scholar_1(self):
            """
              技能测试--学者转职--重炮手
            """
            try:
                print("测试Prof5-转职为学者分支、工程师分支、重炮手分支")
                self.assertEqual("重炮手", skill.test_scholar_1(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "重炮手-职业技能测试")



        def test_scholar_2(self):
            """
            技能测试--学者转职--机械大师
            """
            try:
                print("测试Prof5-转职为学者分支、工程师分支、机械大师分支")
                self.assertEqual("机械大师", skill.test_scholar_2(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "机械大师-职业技能测试")



        def test_scholar_3(self):
            """
            技能测试--学者转职--炼金圣士
            """
            try:
                print("Prof5-转职为学者分支、炼金术士分支、炼金圣士分支")
                self.assertEqual("炼金圣士", skill.test_scholar_3(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "炼金圣士-职业技能测试")



        def test_scholar_4(self):
            """
             技能测试--学者转职--药剂师
            """
            try:
                print("Prof5-转职为学者分支、炼金术士分支、药剂师分支")
                self.assertEqual("药剂师", skill.test_scholar_4(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "药剂师-职业技能测试")




        def test_pastor_5(self):
            """
            技能测试--学者转职--银色机甲师
            """
            try:
                print("Prof5-转职为学者分支、机甲师分支、银色机甲师分支")
                self.assertEqual("圣骑士", skill.test_scholar_5(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "圣骑士-职业技能测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkillscholar)
    return srcSuite
