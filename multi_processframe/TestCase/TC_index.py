# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.mainectype import main_ectype
from multi_processframe.Tools import initial, screenshot
from Script.firstinterface import index


def Main(devices):
    class TCindex(unittest.TestCase):
        u'''一级界面测试用例的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        # def test_SignInReward(self):
        #     """
        #     一级界面--签到模块判断
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SignInReward(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略",start_Screenshot)
        #
        #
        # def test_SysStrengthen(self):
        #     """
        #     一级界面--变强模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysStrengthen(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysAward(self):
        #     """
        #     一级界面--奖励模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysAward(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysAuction(self):
        #     """
        #     一级界面--交易所模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysAuction(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        def test_SysGameMall(self):
            """
            一级界面--商城模块打开是否正常
            """
            try:
                self.assertEqual("CustomerService", index.test_SysGameMall(devices))
            except:
                start_Screenshot = "这里是启动报错场景截图的功能"
                screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
                self.assertEqual("此条的信息请忽略", start_Screenshot)

        # def test_SysLimitDragon(self):
        #     """
        #     一级界面--极限龙本模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysLimitDragon(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysSevenActivity(self):
        #     """
        #     一级界面--登陆奖励模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysSevenActivity(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysLive(self):
        #     """
        #     一级界面--观看模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysLive(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysOperatingActivity(self):
        #     """
        #     一级界面--精彩活动模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysOperatingActivity(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysFirstRecharge(self):
        #     """
        #     一级界面--首冲模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysFirstRecharge(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysCarnival(self):
        #     """
        #     一级界面--模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysCarnival(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysPVP(self):
        #     """
        #     一级界面--竞技场模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysPVP(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysGuild(self):
        #     """
        #     一级界面--公会模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysGuild(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysActivity(self):
        #     """
        #     一级界面--日常模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysActivity(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        #
        # def test_SysItem(self):
        #     """
        #      一级界面--角色模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysItem(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysSkill(self):
        #     """
        #      一级界面--技能模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysSkill(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysSprite(self):
        #     """
        #      一级界面--精灵模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysSprite(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysEquipCreate(self):
        #     """
        #      一级界面--制作模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysEquipCreate(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysHorse(self):
        #     """
        #      一级界面--坐骑模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysHorse(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysFriends(self):
        #     """
        #      一级界面--好友模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysFriends(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysHome(self):
        #     """
        #      一级界面--家园模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysHome(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysRank(self):
        #     """
        #     一级界面--排行榜模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysRank(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysCardCollect(self):
        #     """
        #     一级界面--图鉴模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysCardCollect(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysNPCFavor(self):
        #     """
        #     一级界面--头衔模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysNPCFavor(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_ChatContent(self):
        #     """
        #     一级界面--聊天模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_ChatContent(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysPhoto(self):
        #     """
        #     一级界面--拍照模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysPhoto(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysLoverDance(self):
        #     """
        #     一级界面--双人动作模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysLoverDance(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysDance(self):
        #     """
        #     一级界面--跳舞模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysDance(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysHorseRide(self):
        #     """
        #     一级界面--坐骑骑乘模块打开是否正常
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysHorseRide(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        #
        # def test_SysChange(self):
        #     """
        #     一级界面--变强模块打开是否正常
        #
        #     """
        #     try:
        #         self.assertEqual("1", Firstinterface.test_SysChange(devices))
        #     except:
        #         start_Screenshot = "这里是启动报错场景截图的功能"
        #         screenshot.get_screen_shot(time.time(), devices, "通用测试截图名称")
        #         self.assertEqual("此条的信息请忽略", start_Screenshot)
        # def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCindex)
    return srcSuite
