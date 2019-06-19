# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from airtest.core.api import *
from multi_processframe.Tools import screenshot, printcolor, adb_connect

def card_collect(devices):
    """
    精灵测试脚本
    :param devices:
    :return:
    """
    poco = adb_connect.device(devices)
    check_menu("SysCSprite", poco)  # 进入精灵
    if poco("SpriteSystemDlg(Clone)").exists():  # 判断精灵界面是否存在
        try:
            poco("XSys_SpriteSystem_Shop").click() # 先抽精灵
            poco("SpriteSystemDlg(Clone)").offspring("SpriteShopHandler").offspring("SpecialLottery").offspring("Ten").click()
            poco("XSys_SpriteSystem_Lottery").click()
            if poco("SpriteSystemDlg(Clone)").offspring("SpriteShopHandler").offspring("SpecialLottery").offspring("Button").child("Free").exists():
                poco("SpriteSystemDlg(Clone)").offspring("SpriteShopHandler").offspring("SpecialLottery").child("Button").click()
                if poco("SpriteShowDlg(Clone)").offspring("Bg").offspring("Close").child("Label").exists():
                    poco("SpriteShowDlg(Clone)").offspring("Bg").offspring("Close").child("Label").click()
                    if poco("ShareBtn").exists():
                        poco("Close").click()
                    poco("OkButton").click()
            poco("SpriteSystemDlg(Clone)").offspring("SpriteLotteryHandler").offspring("SpecialLottery").offspring("Ten").click()
            time.sleep(1)
            poco("OkButton").click()
            time.sleep(2)
            if poco("SpriteShowDlg(Clone)").offspring("Bg").offspring("Close").child("Label").exists():
                poco("SpriteShowDlg(Clone)").offspring("Bg").offspring("Close").child("Label").click()
                if poco("ShareBtn").exists():
                    poco("Close").click()
                poco("OkButton").click()
            else:
                poco("OkButton").click()
            printcolor.printgreen("购买精灵蛋，抽精灵流程正常")
        except Exception as e:
            printcolor.printred("购买精灵蛋，抽精灵流程异常")
            printcolor.printred(e)
            # screenshot.get_screen_shot(time.time(), devices, "购买精灵蛋，抽精灵流程正常异常")
        with poco.freeze() as freeze_poco:
            if freeze_poco("Help").exists() and \
                    freeze_poco("XSys_SpriteSystem_Main").exists() and \
                    freeze_poco("XSys_SpriteSystem_Fight").exists() and \
                    freeze_poco("XSys_SpriteSystem_Shop").exists() and \
                    freeze_poco("XSys_SpriteSystem_Lottery").exists() and \
                    freeze_poco("XSys_SpriteSystem_Resolve").exists() and \
                    freeze_poco("XSys_SpriteSystem_EquipMade").exists() and \
                    freeze_poco("Illustration").exists() and \
                    poco("MainSkill").exists() and \
                    freeze_poco("P1").exists() and \
                    freeze_poco("FeedBtn").exists() and \
                    freeze_poco("AwakeBtn").exists() and \
                    freeze_poco("StarUpBtn").exists() and \
                    freeze_poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring("item0").exists() and \
                    freeze_poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring("item1").exists():
                    printcolor.printgreen("精灵技能，上阵，商店，召唤，分解，打造，精灵属性，精灵装备，精灵进阶，喂食，觉醒，升星UI元素显示正常")
            else:
                printcolor.printred("精灵界面UI元素显示异常，详情见截图")
                # screenshot.get_screen_shot(time.time(), devices, "精灵界面UI元素显示异常")










    else:
        printcolor.printred("精灵界面报错，详情见截图")
        # screenshot.get_screen_shot(time.time(), devices, "精灵界面报错")
    poco("Close").click()
    return poco("Duck").get_name()   # 返回值poco("Duck").get_name()

def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 0.98:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco("MenuSwitchBtn").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()


devices = "127.0.0.1:62001"
card_collect(devices)