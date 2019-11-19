"""
精灵测试脚本
"""
# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from multi_processframe.ProjectTools.common import *
from airtest.core.api import *


def sprite(start, devices):
    """
    精灵测试脚本
    :param devices:
    :return:
    """
    poco = deviceconnect(devices)
    check_menu("SysCSprite", poco)  # 进入精灵
    if poco("SpriteSystemDlg(Clone)").exists():  # 判断精灵界面是否存在
        try:
            poco("XSys_SpriteSystem_Shop").click()  # 先买精灵蛋
            if poco(texture="l_button_Act_1").exists():  # 判断免费次数存不存在
                poco(texture="l_button_Act_1").click()
                for i in range(5):
                    poco("SpecialLottery").offspring("Ten").click()
            else:
                for i in range(5):
                    poco("SpecialLottery").offspring("Ten").click()
            poco("XSys_SpriteSystem_Lottery").click()  # 进入召唤界面抽精灵
            for i in range(4):
                poco("SpecialLottery").offspring("Ten").click()
                if poco("GreyModalDlg(Clone)").child("Bg").child("OK").exists():
                    poco("OK").click()
                    print("您的精灵已达到上限80只，请先分解部分精灵 ")
                    break
                else:
                    time.sleep(5)
                    count = 0
                    with poco.freeze() as freezez_poco:
                        for i in range(10):
                            item = "item" + str(i)
                            if not freezez_poco("SpriteSystemDlg(Clone)").offspring("SpriteLotteryHandler").offspring(
                                    item).child("ItemTpl").exists():
                                count += 1
                    printgreen(f"抽到了{count}个S级以上的坐骑")
                    if count == 0:
                        poco("OkButton").click()
                    else:
                        poco("OkButton").click()
                        for i in range(count):
                            time.sleep(3)
                            if poco("SpriteShowDlg(Clone)").offspring("Bg").offspring("Close").child(
                                    "Label").exists():  # 判断A级以上的精灵是否抽到
                                poco("SpriteShowDlg(Clone)").offspring("Bg").offspring("Close").child(
                                    "Label").click()  # 抽到点击跳过
                                if poco("ShareBtn").exists():  # 判断有没有分享图
                                    poco("Close").click()  # 有分享图点掉
                        poco("OkButton").click()
                        printgreen("此次抽精灵操作正常")
        except Exception as e:
            printred("购买精灵蛋，抽精灵流程异常")
            printred(e)
            get_screen_shot(start, time.time(), devices, "购买精灵蛋，抽精灵流程正常异常")
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
                    poco("P1").click()
                    poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring("BtnObtain").child("T").click()
                    poco(texture="l_close_00").click()
                    print("进阶按钮点击正常，界面显示正常")
                else:
                    print("没有S级以上的精灵，进阶按钮不显示")
                printgreen("精灵技能，上阵，商店，召唤，分解，打造，精灵属性，精灵装备，喂食，觉醒，升星UI元素显示正常")
            else:
                printred("精灵界面UI元素显示异常，详情见截图")
                get_screen_shot(start, time.time(), devices, "精灵界面UI元素显示异常")
            try:
                if not poco("FoodList").exists():
                    poco("FeedBtn").click()
                for i in range(3):
                    item = "item" + str(i)
                    num = poco("SpriteSystemDlg(Clone)").offspring(item).child("Num").get_text()
                    if int(num) > 0:
                        break
                poco("SpriteSystemDlg(Clone)").offspring(item).child("Quality").click()
                printgreen("精灵升级正常")
                poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring("TabsFrame").child("item0").click()
                poco("AwakeBtn").click()
                poco("OK").click()
                poco("SpriteSystemDlg(Clone)").offspring("KeepOrig").child("Background").click()
                poco("StarUpBtn").click()
                poco("SpriteSystemDlg(Clone)").offspring("StarUpBtn").click()
                poco("RebornBtn").click()
                poco("Select1").click()
                poco(texture="l_close_00").click()
                printgreen("精灵升星，重生正常")
                poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").offspring("TabsFrame").child("item1").click()
                poco("AccessBtn").click()
                poco("SpriteSystemDlg(Clone)").offspring("SpriteElves").offspring("item0").child("Icon").click()
                if poco("SpriteSystemDlg(Clone)").offspring("SpriteElves").offspring("item0").child("Item").exists():
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
                        poco("FuncFrame").child("Button1").click()  # 卸下穿戴的装备
                        poco("SpriteSystemDlg(Clone)").offspring("SpriteMainFrame").child("Bg").child(
                            "Spriteequip").child("Spriteequip").child(equipname).click()
                        poco("Button1").click()
                        printgreen("精灵装备打造穿戴正常")
                    except Exception as e:
                        printred("精灵装备打造穿戴异常")
                        printred(e)
                        get_screen_shot(start, time.time(), devices, "精灵准备打造穿戴异常")
                else:
                    printred("精灵装备界面异常")
                    get_screen_shot(start, time.time(), devices, "精灵装备界面异常")
                try:
                    poco("XSys_SpriteSystem_Fight").click()
                    count = 0  # 计数出去队长之外一共有多少个精灵在阵上
                    with poco.freeze() as preeze_poco:  # 冻结计算不是队长位置一共有几个精灵
                        if preeze_poco("SpriteFightFrame").offspring("CBtn").exists():
                            for i in preeze_poco("SpriteFightFrame").offspring("CBtn"):
                                uiname = i.parent().parent().get_name()
                                if preeze_poco(uiname).exists():
                                    count += 1
                        if preeze_poco("SpriteSystemDlg(Clone)").offspring("Avatar0").offspring(
                                "Name").get_text() == "":
                            print("上阵的精灵中没有队长", end=",")
                        else:
                            count += 1
                        printgreen(f"一共有{count}个精灵在阵上")
                        if preeze_poco("SpriteSystemDlg(Clone)").offspring("Avatar0").offspring(
                                "Name").get_text() == "" and count == 0:
                            for i in range(3):
                                item = "item" + str(i)
                                preeze_poco("SpriteSystemDlg(Clone)").offspring(item).click()
                            poco("SpriteSystemDlg(Clone)").offspring("Avatar2").offspring("CBtn").click()
                    printgreen("精灵上阵操作正常")
                except Exception as e:
                    printred("精灵上阵操作异常")
                    printred(e)
                    get_screen_shot(start, time.time(), devices, "精灵上阵操作异常")
                try:
                    # 分解
                    poco("XSys_SpriteSystem_Resolve").click()
                    poco("XSys_SpriteSystem_Resolve").click()
                    with poco.freeze() as freeze_poco:
                        freeze_poco("SpriteSystemDlg(Clone)").offspring("item0").click()
                        freeze_poco("SpriteSystemDlg(Clone)").offspring("item1").click()
                        freeze_poco("ResolveBtn").click()
                        if poco("GreyModalDlg(Clone)").offspring("OK").exists():
                            poco("GreyModalDlg(Clone)").offspring("OK").click()
                        freeze_poco("FilterBtn").click()
                        if len(poco("SpriteSystemDlg(Clone)").offspring("SpriteResolveFrame").child(
                                "ScrollView").child()) < 3:
                            freeze_poco("SpriteSystemDlg(Clone)").offspring("ItemOperateFrame").offspring("C").child(
                                "Checked").click()
                            freeze_poco("SpriteSystemDlg(Clone)").offspring("ItemOperateFrame").offspring("B").child(
                                "Checked").click()
                            freeze_poco("SpriteSystemDlg(Clone)").offspring("ItemOperateFrame").offspring("A").child(
                                "Checked").click()
                        freeze_poco("FilterBtn").click()
                        freeze_poco("ResolveBtn").click()
                        if poco("GreyModalDlg(Clone)").offspring("OK").exists():
                            poco("GreyModalDlg(Clone)").offspring("OK").click()
                        if poco("GreyModalDlg(Clone)").offspring("OK").exists():
                            poco("GreyModalDlg(Clone)").offspring("OK").click()
                        printgreen("精灵分解成功")
                        freeze_poco("Illustration").click()
                        poco(texture="l_close_00").click()
                    printgreen("精灵分解操作正常")
                except Exception as e:
                    printred("精灵分解操作异常")
                    printred(e)
                    get_screen_shot(start, time.time(), devices, "精灵分解操作异常")
            except  Exception as e:
                printred("精灵操作流程异常")
                printred(e)
                get_screen_shot(start, time.time(), devices, "精灵操作流程异常")
    else:
        printred("精灵界面报错，详情见截图")
        get_screen_shot(start, time.time(), devices, "精灵界面报错")
    return poco("FilterBtn").get_name()  # 返回值poco("Duck").get_name()


def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 0.98:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco("MenuSwitchBtn").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()


if __name__ == "__main__":
    start = time.localtime()
    sprite(start, "f4eebcd6")
