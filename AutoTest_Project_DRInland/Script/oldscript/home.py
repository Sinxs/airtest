"""
家园模块
"""
from multi_processframe.ProjectTools import common,common,common
from airtest.core.api import *


def home(start, devices):
    poco = common.deviceconnect(devices)
    if poco("SysB_Home").get_position()[0] > 1:
        poco(texture="halln_4").click()
        sleep(2)
    else:
        common.printgreen("当前界面就有家园按钮")
    poco("SysB_Home").click()  # 点击家园按钮
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    homelist = ["XSys_Home_MyHome","XSys_Home_HomeFriends","XSys_Home_Cooking","XSys_Home_Feast"]
    for item in homelist:
        if freeze_poco("HomeMainView(Clone)").offspring(item).offspring("TextLabel").exists():
            common.printgreen("界面检查点 " + freeze_poco("HomeMainView(Clone)").offspring(item).offspring("TextLabel").get_text() + " 存在")
        else:
            common.printred("家园界面 缺少控件，请检查")
            common.get_screen_shot(start, time.time(), devices, "家园界面缺少控件")
    poco("HomeMainView(Clone)").offspring("XSys_Home_MyHome").click()  # 点击我的家园
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("HomeMainView(Clone)").offspring("HomeLog").child("Tittle").child("NameLab").exists() and \
            freeze_poco("HomeMainView(Clone)").offspring("FriendsRank").child("Tittle").child("NameLab").exists():
        common.printgreen("检查点 " + freeze_poco("HomeMainView(Clone)").offspring("HomeLog").child("Tittle").child("NameLab").get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco("HomeMainView(Clone)").offspring("FriendsRank").child("Tittle").child("NameLab").get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco("VisitedTimes").child("Tittle").get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco("BaitNum").child("Tittle").get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco("PlantNum").child("Tittle").get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco("HarvestTime").child("Tittle").get_text() + " 显示正确")
        common.printgreen("检查点 " + freeze_poco("HomeStatus").child("Tittle").get_text() + " 显示正确")
    else:
        common.printred("我的家园界面 缺少控件，请检查")
        common.get_screen_shot(start, time.time(), devices, "我的家园界面缺少控件")
    poco("HomeMainView(Clone)").offspring("XSys_Home_HomeFriends").click()  # 点击好友
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("ailin").exists() and freeze_poco("tip").exists():
        common.printgreen("检查点" + freeze_poco("tip").get_text() + "显示完成")
    else:
        common.printred("好友界面 缺少控件，请检查")
        common.get_screen_shot(start, time.time(), devices, "好友界面缺少控件")
    poco("HomeMainView(Clone)").offspring("XSys_Home_Cooking").click()  # 点击烹饪
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("ToggleSprite").exists():
        A = poco("ToggleSprite").get_position()[1]
        B = (poco("HomeMainView(Clone)").offspring("UITable").child("item0")
            .child("Children").child("item0").get_position()[1])
        if B - A < 0.05:
            poco("ToggleSprite").click()  # 点击一级料理
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        for item in range(len(freeze_poco("HomeMainView(Clone)").offspring("UITable").child("item0").
                                      child("Children").child())):
            item1 = "item" + str(item)
            common.printgreen("检查点 " + freeze_poco("HomeMainView(Clone)").offspring("UITable").child("item0")
                              .child("Children").child(item1).child("UnSelectLab").get_text() + "显示正确")
        poco("ToggleSprite").click()  # 缩回一级料理
        A = poco("NameLab").get_position()[1]
        B = (poco("HomeMainView(Clone)").offspring("UITable").child("item1").offspring("item10")
            .child("UnSelectLab").get_position()[1])
        if B - A < 0.05:
            poco("NameLab").click()  # 点击二级料理
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        for item in range(len(freeze_poco("HomeMainView(Clone)").offspring("UITable").child("item1").
                                      child("Children").child())):
            item1 = "item" + str(item)
            common.printgreen("检查点 " + freeze_poco("HomeMainView(Clone)").offspring("UITable").child("item0").
                              child("Children").child(item1).child("UnSelectLab").get_text() + "显示正确")
    else:
        common.printred("烹饪界面 缺少控件，请检查")
        common.get_screen_shot(start, time.time(), devices, "烹饪界面缺少控件")
    poco("HomeMainView(Clone)").offspring("XSys_Home_Feast").click()  # 点击宴会
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item0").child("Tittle").exists() and \
            freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item1").child("Tittle").exists() and \
            freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item2").child("Tittle").exists() and \
            freeze_poco(texture="l_frame_01_00").exists() and \
            freeze_poco(texture="l_frame_01_0").exists():
        common.printgreen("宴会界面检查点" + freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item2").
                          child("Tittle").get_text() + "显示正确")
        common.printgreen("宴会界面检查点" + freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item1").
                          child("Tittle").get_text() + "显示正确")
        common.printgreen("宴会界面检查点" + freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item0").
                          child("Tittle").get_text() + "显示正确")
    else:
        common.printred("宴会界面 缺少控件，请检查")
        common.get_screen_shot(start, time.time(), devices, "宴会界面缺少控件")
    poco("HomeMainView(Clone)").offspring("Tabs").child("item0").child("Tittle").click()  # 点击全鱼宴
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if poco("HomeMainView(Clone)").offspring("Content").offspring("Name").exists() and poco("ContentLab").exists():
        common.printgreen("界面检查点 " + freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item0").
                          child("Tittle").get_text() + " 显示正确")
        common.printgreen("界面检查点 " + freeze_poco("ContentLab").get_text() + " 显示正确")
    else:
        common.printred("全鱼宴界面 缺少控件，请检查")
        common.get_screen_shot(start, time.time(), devices, "全鱼宴界面缺少控件")
    poco("HomeMainView(Clone)").offspring("Tabs").child("item1").child("Tittle").click()  # 点击海鲜宴
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if poco("HomeMainView(Clone)").offspring("Content").offspring("Name").exists() and poco("ContentLab").exists():
        common.printgreen(
            "界面检查点 " + freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item0").
            child("Tittle").get_text() + " 显示正确")
        common.printgreen("界面检查点 " + freeze_poco("ContentLab").get_text() + " 显示正确")
    else:
        common.printred("海鲜宴界面 缺少控件，请检查")
        common.get_screen_shot(start, time.time(), devices, "海鲜宴界面缺少控件")
    poco("HomeMainView(Clone)").offspring("Tabs").child("item2").child("Tittle").click()  # 点击腊八粥宴
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if poco("HomeMainView(Clone)").offspring("Content").offspring("Name").exists() and poco("ContentLab").exists():
        common.printgreen("界面检查点 " + freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item0").
                          child("Tittle").get_text() + " 显示正确")
        common.printgreen("界面检查点 " + freeze_poco("ContentLab").get_text() + " 显示正确")

    else:
        common.printred("腊八粥宴界面 缺少控件，请检查")
        common.get_screen_shot(start, time.time(), devices, "腊八粥宴界面缺少控件")
    return poco("HomeMainView(Clone)").offspring("Tabs").child("item2").child("Tittle").get_text()


def entrancehome(start, devices):
    poco = common.deviceconnect(devices)
    poco = common.deviceconnect(devices)
    if poco("SysB_Home").get_position()[0] > 1:
        poco(texture="halln_4").click()
        sleep(2)
    else:
        common.printgreen("当前界面就有家园按钮")
    poco("SysB_Home").click()  # 点击家园按钮
    if poco("HomeMainView(Clone)").offspring("XSys_Home_MyHome").exists():
        poco("HomeMainView(Clone)").offspring("XSys_Home_MyHome").click()  # 点击我的家园
        if poco("Background").exists():
            poco("Background").click()  # 点击前往家园
            sleep(7)
            if poco("Planting").child("T").exists() and \
                    poco("Fishing").child("T").exists() and \
                    poco("HomeHandler").child("Name").exists():
                common.printgreen("检查点" + poco("Planting").child("T").get_text() + "  显示正确")
                common.printgreen("检查点" + poco("Fishing").child("T").get_text() + "  显示正确")
                common.printgreen("检查点" + poco("HomeHandler").child("Name").get_text() + "  显示正确")
                common.printgreen("进入我的家园测试成功")
            else:
                common.printgreen("没有进入我的家园，请检查..")
                common.get_screen_shot(start, time.time(), devices, "没有进入我的家园")
            poco("Fishing").child("T").click()  # 点击钓鱼
            sleep(10)
            if poco("StartFishingBtn").exists() and poco("SweepBtn").exists():
                poco("StartFishingBtn").click()  # 点击单次钓鱼
                if poco(texture="l_frame_02").child("T").exists():
                    common.printgreen("检查点 " + poco(texture="l_frame_02").child("T").get_text() + "  显示正确")
                    common.printgreen("进入钓鱼成功")
                    sleep(10)
                    poco("Close").click()
                    if poco(texture="title_public").exists():
                        poco("OK").click()
                        common.printgreen("钓鱼操作测试完成")
                    else:
                        common.printgreen("没有钓到鱼........")
            else:
                common.printgreen("没有钓鱼按钮，请检查..")
                common.get_screen_shot(start, time.time(), devices, "没有钓鱼按钮")
        else:
            common.printgreen("我的家园界面缺少前家园按钮，请检查..")
            common.get_screen_shot(start, time.time(), devices, "我的家园界面缺少前家园按钮")
    else:
        common.printgreen("家园界面缺少控件。请检查..")
        common.get_screen_shot(start, time.time(), devices, "家园界面缺少控件")
    if poco("SysC_HomeCooking").exists():
        poco("SysC_HomeCooking").click()  # 点击烹饪按钮
        poco("HomeMainView(Clone)").offspring("XSys_Home_MyHome").click()  # 点击我的家园
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("HomeMainView(Clone)").offspring("HomeLog").child("Tittle").child("NameLab").exists() and \
                freeze_poco("HomeMainView(Clone)").offspring("FriendsRank").child("Tittle").child("NameLab").exists():
            common.printgreen(
                "检查点 " + freeze_poco("HomeMainView(Clone)").offspring("HomeLog").child("Tittle").child(
                    "NameLab").get_text() + " 显示正确")
            common.printgreen(
                "检查点 " + freeze_poco("HomeMainView(Clone)").offspring("FriendsRank").child("Tittle").child(
                    "NameLab").get_text() + " 显示正确")
            common.printgreen("检查点 " + freeze_poco("VisitedTimes").child("Tittle").get_text() + " 显示正确")
            common.printgreen("检查点 " + freeze_poco("BaitNum").child("Tittle").get_text() + " 显示正确")
            common.printgreen("检查点 " + freeze_poco("PlantNum").child("Tittle").get_text() + " 显示正确")
            common.printgreen("检查点 " + freeze_poco("HarvestTime").child("Tittle").get_text() + " 显示正确")
            common.printgreen("检查点 " + freeze_poco("HomeStatus").child("Tittle").get_text() + " 显示正确")
        else:
            common.printred("我的家园界面 缺少控件，请检查")
            common.get_screen_shot(start, time.time(), devices, "我的家园界面缺少控件")
        poco("HomeMainView(Clone)").offspring("XSys_Home_HomeFriends").click()  # 点击好友
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("ailin").exists() and freeze_poco("tip").exists():
            common.printgreen("检查点" + freeze_poco("tip").get_text() + "显示完成")
        else:
            common.printred("好友界面 缺少控件，请检查")
            common.get_screen_shot(start, time.time(), devices, "好友界面缺少控件")
        poco("HomeMainView(Clone)").offspring("XSys_Home_Cooking").click()  # 点击烹饪
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("ToggleSprite").exists():
            A = poco("ToggleSprite").get_position()[1]
            B = poco("HomeMainView(Clone)").offspring("UITable").child("item0").child("Children").child(
                "item0").get_position()[1]
            if B - A < 0.05:
                poco("ToggleSprite").click()  # 点击一级料理
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for item in range(len(
                    freeze_poco("HomeMainView(Clone)").offspring("UITable").child("item0").child("Children").child())):
                item1 = "item" + str(item)
                common.printgreen(
                    "检查点 " + freeze_poco("HomeMainView(Clone)").offspring("UITable").child("item0").child(
                        "Children").child(item1).child("UnSelectLab").get_text() + "显示正确")
            poco("ToggleSprite").click()  # 缩回一级料理
            A = poco("NameLab").get_position()[1]
            B = poco("HomeMainView(Clone)").offspring("UITable").child("item1").offspring("item9").child(
                "UnSelectLab").get_position()[1]
            if B - A < 0.05:
                poco("NameLab").click()  # 点击二级料理
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for item in range(len(
                    freeze_poco("HomeMainView(Clone)").offspring("UITable").child("item1").child("Children").child())):
                item1 = "item" + str(item)
                common.printgreen(
                    "检查点 " + freeze_poco("HomeMainView(Clone)").offspring("UITable").child("item0").child(
                        "Children").child(
                        item1).child("UnSelectLab").get_text() + "显示正确")
        else:
            common.printred("烹饪界面 缺少控件，请检查")
            common.get_screen_shot(start, time.time(), devices, "烹饪界面缺少控件")
        poco("HomeMainView(Clone)").offspring("XSys_Home_Feast").click()  # 点击宴会
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item0").child("Tittle").exists() and \
                freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item1").child("Tittle").exists() and \
                freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item2").child("Tittle").exists() and \
                freeze_poco(texture="l_frame_01_00").exists() and \
                freeze_poco(texture="l_frame_01_0").exists():
            common.printgreen("宴会界面检查点" + freeze_poco("HomeMainView(Clone)").offspring("Tabs").
                              child("item2").child("Tittle").get_text() + "显示正确")
            common.printgreen("宴会界面检查点" + freeze_poco("HomeMainView(Clone)").offspring("Tabs").
                              child("item1").child("Tittle").get_text() + "显示正确")
            common.printgreen("宴会界面检查点" + freeze_poco("HomeMainView(Clone)").offspring("Tabs").
                              child("item0").child("Tittle").get_text() + "显示正确")
        else:
            common.printred("宴会界面 缺少控件，请检查")
            common.get_screen_shot(start, time.time(), devices, "宴会界面缺少控件")
        poco("HomeMainView(Clone)").offspring("Tabs").child("item0").child("Tittle").click()  # 点击全鱼宴
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if poco("HomeMainView(Clone)").offspring("Content").offspring("Name").exists() and \
                poco("ContentLab").exists():
            common.printgreen("界面检查点 " + freeze_poco("HomeMainView(Clone)").offspring("Tabs").
                              child("item0").child("Tittle").get_text() + " 显示正确")
            common.printgreen("界面检查点 " + freeze_poco("ContentLab").get_text() + " 显示正确")
        else:
            common.printred("全鱼宴界面 缺少控件，请检查")
            common.get_screen_shot(start, time.time(), devices, "全鱼宴界面缺少控件")
        poco("HomeMainView(Clone)").offspring("Tabs").child("item1").child("Tittle").click()  # 点击海鲜宴
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if poco("HomeMainView(Clone)").offspring("Content").offspring("Name").exists() and poco("ContentLab").exists():
            common.printgreen(
                "界面检查点 " + freeze_poco("HomeMainView(Clone)").offspring("Tabs").child("item0").child(
                    "Tittle").get_text() + " 显示正确")
            common.printgreen("界面检查点 " + freeze_poco("ContentLab").get_text() + " 显示正确")
        else:
            common.printred("海鲜宴界面 缺少控件，请检查")
            common.get_screen_shot(start, time.time(), devices, "海鲜宴界面缺少控件")
        poco("HomeMainView(Clone)").offspring("Tabs").child("item2").child("Tittle").click()  # 点击腊八粥宴
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("HomeMainView(Clone)").offspring("Content").offspring("Name").exists() and \
                freeze_poco("ContentLab").exists():
            common.printgreen("界面检查点 " + freeze_poco("HomeMainView(Clone)").offspring("Tabs").
                              child("item0").child("Tittle").get_text() + " 显示正确")
            common.printgreen("界面检查点 " + freeze_poco("ContentLab").get_text() + " 显示正确")
            poco("Close").click()  # TODO:点击返回
            if poco("SysB_HomeShop").exists():
                poco("SysB_HomeShop").click()  # 点击家园商店
                freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                for item in range(len(poco("Panel").child())):
                    item1 = "item" + str(item)
                    if freeze_poco("MallDlg(Clone)").offspring(item1).child("Item").child("Name").exists():
                        common.printgreen("界面检查点 " + freeze_poco("MallDlg(Clone)").offspring(item1).
                                          child("Item").child("Name").get_text() + " 显示正确")
                    else:
                        common.printred("家园商店界面 缺少控件，请检查")
                        common.get_screen_shot(start, time.time(), devices, "家园商店界面缺少控件")
            poco("Close").click()  # TODO:点击返回

            if poco("SysA_HomeMain").exists():
                poco("SysA_HomeMain").click()  # 点击家园总览
                common.printgreen("进入家园总览成功，因为已经测试过当前界面，故不再测试...")
                if poco(texture="l_frame_00").exists():
                    poco("Close").click()  # TODO:点击返回
                    if poco("ExitHome").exists():
                        poco("ExitHome").click()  # 返回主界面
                        sleep(15)
                        if poco("H2").exists():
                            common.printgreen("回到游戏主界面")
            else:
                common.printred("家园界面缺少 家园总览 控件，请检查")
                common.get_screen_shot(start, time.time(), devices, "家园界面缺少家园总览缺少控件")
        else:
            common.printred("腊八粥宴界面 缺少控件，请检查")
            common.get_screen_shot(start, time.time(), devices, "腊八粥宴界面缺少控件")
    else:
        common.printgreen("家园界面缺少烹饪控件。请检查..")
        common.get_screen_shot(start, time.time(), devices, "我的家园界面缺少前家园按钮")
    return poco("Alphaboard").offspring("SysA_Friends").child("Name").get_text()  # 返回  社交  社交


