# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.mainectype import main_ectype
from multi_processframe.Tools import initial, screenshot
from Script.firstinterface import Firstinterface


def Main(devices):
    class TCuse(unittest.TestCase):
        u'''一级界面测试用例的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_SignInReward(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SignInReward(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略",start_Screenshot)


        def test_SysStrengthen(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysStrengthen(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysAward(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysAward(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysAuction(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysAuction(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysGameMall(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysGameMall(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysLimitDragon(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysLimitDragon(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysSevenActivity(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysSevenActivity(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysLive(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysLive(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysOperatingActivity(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysOperatingActivity(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysFirstRecharge(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysFirstRecharge(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysCarnival(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysCarnival(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysPVP(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysPVP(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysGuild(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysGuild(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysActivity(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysActivity(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)


        def test_SysItem(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysItem(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysSkill(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysSkill(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysSprite(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysSprite(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysEquipCreate(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysEquipCreate(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysHorse(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysHorse(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysFriends(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysFriends(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysHome(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysHome(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysRank(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysRank(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysCardCollect(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysCardCollect(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysNPCFavor(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysNPCFavor(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_ChatContent(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_ChatContent(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysPhoto(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysPhoto(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysLoverDance(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysLoverDance(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysDance(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysDance(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysHorseRide(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysHorseRide(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        def test_SysChange(self):
            """
            这是测试一级界面的用例:
            return: 返回关卡完成回到主界面
            """
            try:
                self.assertEqual("1", Firstinterface.test_SysChange(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)
        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCuse)
    return srcSuite
