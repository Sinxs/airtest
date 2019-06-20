# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from airtest.core.api import *
from multi_processframe.Tools import screenshot, printcolor, adb_connect

def sprite(devices):
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
            if poco("SpriteSystemDlg(Clone)").offspring("SpriteShopHandler").offspring("SpecialLottery").child("Button").child("Free").exists():
                poco("SpriteSystemDlg(Clone)").offspring("SpriteShopHandler").offspring("SpecialLottery").child("Button").child("Free").click()
                if poco("SpriteShowDlg(Clone)").offspring("Bg").offspring("Close").child("Label").exists():
                    poco("SpriteShowDlg(Clone)").offspring("Bg").offspring("Close").child("Label").click()
                    if poco("ShareBtn").exists():
                        poco("Close").click()
                    poco("OkButton").click()
            poco("SpriteSystemDlg(Clone)").offspring("SpriteLotteryHandler").offspring("SpecialLottery").offspring("Ten").click()
            time.sleep(5)
            count = 0
            with poco.freeze() as freezez_poco:
                for i in range(10):
                    item = "item" + str(i)
                    if not freezez_poco("SpriteSystemDlg(Clone)").offspring("SpriteLotteryHandler").offspring(
                            item).child("ItemTpl").exists():
                        count += 1
            printcolor.printgreen(f"抽到了{count}个A级以上的坐骑")
            if count == 0:
                poco("OkButton").click()
            else:
                poco("OkButton").click()
                for i in range(count):
                        time.sleep(3)
                        if poco("SpriteShowDlg(Clone)").offspring("Bg").offspring("Close").child("Label").exists(): # 判断A级以上的精灵是否抽到
                            poco("SpriteShowDlg(Clone)").offspring("Bg").offspring("Close").child("Label").click() # 抽到点击跳过
                            if poco("ShareBtn").exists(): # 判断有没有分享图
                                poco("Close").click() # 有分享图点掉
                poco("OkButton").click()
            printcolor.printgreen("购买精灵蛋，抽精灵流程正常")
        except Exception as e:
            printcolor.printred("购买精灵蛋，抽精灵流程异常")
            printcolor.printred(e)
            screenshot.get_screen_shot(time.time(), devices, "购买精灵蛋，抽精灵流程正常异常")
        poco("XSys_SpriteSystem_Main").click()
        poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring("TabsFrame").child("item0").click()
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
                    freeze_poco("FeedBtn").exists() and \
                    freeze_poco("AwakeBtn").exists() and \
                    freeze_poco("StarUpBtn").exists() and \
                    freeze_poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring("item0").exists() and \
                    freeze_poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring("item1").exists():
                    if freeze_poco("P1").exists():
                        printcolor.printgreen("进阶",end=",")
                    else:
                        print("没有S级以上的精灵，进阶按钮不显示")
                    printcolor.printgreen("精灵技能，上阵，商店，召唤，分解，打造，精灵属性，精灵装备，喂食，觉醒，升星UI元素显示正常")
            else:
                printcolor.printred("精灵界面UI元素显示异常，详情见截图")
                screenshot.get_screen_shot(time.time(), devices, "精灵界面UI元素显示异常")
            try:
                if not poco("FoodList").exists():
                    poco("FeedBtn").click()
                for i in range(3):
                    item = "item" + str(i)
                    num = poco("SpriteSystemDlg(Clone)").offspring(item).child("Num").get_text()
                    if int(num) > 0:
                        break
                poco("SpriteSystemDlg(Clone)").offspring(item).child("Quality").click()
                printcolor.printgreen("精灵升级正常")
                poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring("TabsFrame").child("item0").click()
                poco("AwakeBtn").click()
                poco("OK").click()
                poco("SpriteSystemDlg(Clone)").offspring("KeepOrig").child("Background").click()
                poco(text="升星").click()
                poco("SpriteSystemDlg(Clone)").offspring("StarUpBtn").click()
                poco(texture="l_close_00").click()
                poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring("TabsFrame").child("item1").click()
                poco("AccessBtn").click()
                poco("SpriteSystemDlg(Clone)").offspring("SpriteElves").offspring("item0").child("Icon").click()
                poco("Free").click()
                try:
                    poco("XSys_SpriteSystem_Main").click()
                    with poco.freeze() as freeze_poco:  # 获取装备中的第一件，进行穿戴操作
                        equipchild = freeze_poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring(
                            "Items").offspring("WrapContent").child()
                        for i in equipchild:
                            name = i.get_name()
                            if name[:5] != "empty":
                                equipname = name
                                break
                    poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring(equipname)[0].click()
                    poco("FuncFrame").child("Button1").click() # 卸下穿戴的装备
                    poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").child("Bg").child("Spriteequip").child("Spriteequip").child(equipname).click()
                    poco("Button1").click()
                    printcolor.printgreen("精灵装备打造穿戴正常")
                except Exception as e:
                    printcolor.printred("精灵装备打造穿戴异常")
                    printcolor.printred(e)
                    screenshot.get_screen_shot(time.time(), devices, "精灵准备打造穿戴异常")
                try:
                    poco("XSys_SpriteSystem_Fight").click()
                    count = 0 # 计数出去队长之外一共有多少个精灵在阵上
                    with poco.freeze() as preeze_poco: # 冻结计算不是队长位置一共有几个精灵
                        if preeze_poco("SpriteFightFrame").offspring("CBtn").exists():
                            for i in preeze_poco("SpriteFightFrame").offspring("CBtn"):
                                uiname = i.parent().parent().get_name()
                                if preeze_poco(uiname).exists():
                                    count += 1
                        if preeze_poco("SpriteSystemDlg(Clone)").offspring("Avatar0").offspring("Name").get_text() == "":
                            print("上阵的精灵中没有队长", end=",")
                        else:
                            count += 1
                        printcolor.printgreen(f"一共有{count}个精灵在阵上")
                        if preeze_poco("SpriteSystemDlg(Clone)").offspring("Avatar0").offspring("Name").get_text() == "" and count == 0:
                            for i in range(3):
                                item = "item" + str(i)
                                preeze_poco("SpriteSystemDlg(Clone)").offspring(item).click()
                            poco("SpriteSystemDlg(Clone)").offspring("Avatar2").offspring("CBtn").click()
                    printcolor.printgreen("精灵上阵操作正常")
                except Exception as e:
                    printcolor.printred("精灵上阵操作异常")
                    printcolor.printred(e)
                    screenshot.get_screen_shot(time.time(), devices, "精灵上阵操作异常")
                try:
                # 分解
                    poco("XSys_SpriteSystem_Resolve").click()
                    with poco.freeze() as freeze_poco:
                        freeze_poco("SpriteSystemDlg(Clone)").offspring("item0").click()
                        freeze_poco("SpriteSystemDlg(Clone)").offspring("item1").click()
                        freeze_poco("FilterBtn").click()
                        if len(poco("SpriteSystemDlg(Clone)").offspring("SpriteResolveFrame").child("ScrollView").child()) < 3:
                            freeze_poco("SpriteSystemDlg(Clone)").offspring("ItemOperateFrame").offspring("C").child("Checked").click()
                            freeze_poco("SpriteSystemDlg(Clone)").offspring("ItemOperateFrame").offspring("S").child("Checked").click()
                            poco("FilterBtn").click()
                        freeze_poco("ResolveBtn").click()
                        if poco("GreyModalDlg(Clone)").offspring("OK").exists():
                            poco("GreyModalDlg(Clone)").offspring("OK").click()
                        printcolor.printgreen("精灵分解成功")
                        freeze_poco("Illustration").click()
                        poco(texture="l_close_00").click()
                    printcolor.printgreen("精灵分解操作正常")
                except Exception as e:
                    printcolor.printred("精灵分解操作异常")
                    printcolor.printred(e)
                    screenshot.get_screen_shot(time.time(), devices, "精灵分解操作异常")
            except  Exception as e:
                printcolor.printred("精灵操作流程异常")
                printcolor.printred(e)
                screenshot.get_screen_shot(time.time(), devices, "精灵操作流程异常")
    else:
        printcolor.printred("精灵界面报错，详情见截图")
        screenshot.get_screen_shot(time.time(), devices, "精灵界面报错")
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


# devices = "127.0.0.1:62001"
# sprite(devices)