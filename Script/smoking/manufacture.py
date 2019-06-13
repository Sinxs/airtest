from multi_processframe.Tools import printcolor,adb_connect,screenshot
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco


def manufacture(devices):
    poco = adb_connect.device(devices)
    if poco("SysDEquipCreate").get_position()[1] > 0.93:
        poco(texture="halln_4").click()
        sleep(2)
    else:
        printcolor.printgreen("当前界面就有制作按钮")
    poco("SysDEquipCreate").click()
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("XSys_EquipCreate_EquipSet").exists() and \
            freeze_poco("XSys_EquipCreate_EmblemSet").exists() and \
            freeze_poco("XSys_EquipCreate_Upgrade").exists() and \
            freeze_poco("XSys_EquipCreate_ArtifactSet").exists():
        printcolor.printgreen("界面检查点 装备制作-文章制作-龙器制作-装备制作-继承  控件显示正确")
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("EquipCreateDlg(Clone)").offspring("4").offspring("SelectLab").exists() and \
                freeze_poco("EquipCreateDlg(Clone)").offspring("95023").child("Selected").child("P").exists() and \
                freeze_poco("EquipCreateDlg(Clone)").offspring("95223").child("Selected").child("P").exists() and \
                freeze_poco("0").exists() and \
                freeze_poco("1").exists() and \
                freeze_poco("2").exists():
            printcolor.printgreen("装备制作-魔化符文龙套·首饰 各个检查点 显示正确")
        else:
            printcolor.printred("装备制作-魔化符文龙套·首饰 界面 缺少控件，请检查")
            screenshot.get_screen_shot(time.time(), devices, "装备制作-魔化符文龙套·首饰  缺少控件")
        poco("EquipCreateDlg(Clone)").offspring("95023").child("Selected").child("P").click()  # 魔化符文龙套
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("0").exists() and \
                freeze_poco("1").exists() and \
                freeze_poco("2").exists() and \
                freeze_poco("3").exists() and \
                freeze_poco("4").exists():
            printcolor.printgreen("装备制作-魔化付文龙套各个检查点 显示正确")
        else:
            printcolor.printred("装备制作-魔化付文龙套装界面 缺少控件，请检查")
            screenshot.get_screen_shot(time.time(), devices, "装备制作-魔化付文龙套装界面 缺少控件")
        poco("XSys_EquipCreate_EmblemSet").click()  # 点击纹章制作
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("WrapContent").exists() and \
                freeze_poco(texture="Mall_add_2").exists() and \
                freeze_poco("ItemNameLabel").exists() and \
                freeze_poco("Create").exists():
            printcolor.printgreen("纹章制作各个检查点 显示正确")
        else:
            printcolor.printred("纹章制作界面 缺少控件，请检查")
            screenshot.get_screen_shot(time.time(), devices, "纹章制作界面 缺少控件")
        poco("XSys_EquipCreate_ArtifactSet").click()  # 点击龙器制作
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        for item in range(len(freeze_poco("TypeList").offspring("Table").child())):
            if freeze_poco("EquipCreateDlg(Clone)").offspring(str(item)).offspring("SelectLab").exists():
                printcolor.printgreen("检查点 " + freeze_poco("EquipCreateDlg(Clone)").offspring(str(item)).offspring(
                    "SelectLab").get_text() + " 存在")
            elif freeze_poco("EquipCreateDlg(Clone)").offspring(str(item)).offspring("UnSelectLab").exists():
                printcolor.printgreen("检查点 " + freeze_poco("EquipCreateDlg(Clone)").offspring(str(item)).offspring(
                    "UnSelectLab").get_text() + " 存在")
            else:
                printcolor.printred("龙器制作界面缺少控件，请检查")
                screenshot.get_screen_shot(time.time(), devices, "龙器制作界面缺少控件")
        poco("XSys_EquipCreate_Upgrade").click()  # 装备升级界面
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if poco("WrapContent").exists() and \
                freeze_poco(text="装备套装").exists() and \
                freeze_poco("红龙套装").exists() and \
                freeze_poco("冰龙套装").exists() and \
                freeze_poco("符文龙套装").exists():
            printcolor.printgreen("检查点  装备升级界面显示正确")
            poco("红龙套装").click()
            if poco(texture="l_frame_01_0").exists():
                printcolor.printgreen("检查点  红龙套装界面显示正确")
            else:
                printcolor.printred("红龙套装界面缺少控件，请检查")
                screenshot.get_screen_shot(time.time(), devices, "红龙套装界面缺少控件")
            poco("冰龙套装").click()
            if poco(texture="l_frame_01_0").exists():
                printcolor.printgreen("检查点  冰龙套装界面显示正确")
            else:
                printcolor.printred("冰龙套装界面缺少控件，请检查")
                screenshot.get_screen_shot(time.time(), devices, "冰龙套装界面缺少控件")
            poco("符文龙套装").click()
            if poco(texture="l_frame_01_0").exists():
                printcolor.printgreen("检查点  符文龙套装界面显示正确")
            else:
                printcolor.printred("符文龙套装界面缺少控件，请检查")
                screenshot.get_screen_shot(time.time(), devices, "符文龙套装界面缺少控件")
        poco("XSys_Equip_Inherit").click()  # 继承按钮
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("0").exists() and \
                freeze_poco("Table").child("1").exists() and \
                freeze_poco(texture="l_framew_01").exists():
            printcolor.printgreen("检查点--继承界面--显示正确")
            poco("0").offspring("1").child("Selected").click()  # 点击传说装备
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for item in range(len(poco("WrapContent").child())):
                item1 = "item" + str(item)
                if freeze_poco(item1).offspring("Name").exists():
                    printcolor.printgreen("检查点 " + freeze_poco(item1).offspring("Name").get_text() + " 存在")
                else:
                    printcolor.printred("传说装备缺少控件，请检查")
                    screenshot.get_screen_shot(time.time(), devices, "传说装备缺少控件")
            poco("0").offspring("2").child("Selected").click()  # 点击远古装备
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for item in range(len(poco("WrapContent").child())):
                item1 = "item" + str(item)
                if freeze_poco(item1).offspring("Name").exists():
                    printcolor.printgreen("检查点 " + freeze_poco(item1).offspring("Name").get_text() + " 存在")
                else:
                    printcolor.printred("远古装备缺少控件，请检查")
                    screenshot.get_screen_shot(time.time(), devices, "远古装备缺少控件")
            poco("Table").child("1").child("ChildList").offspring("Selected").click()  # 点击 135龙器
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for item in range(len(poco("WrapContent").child())):
                item1 = "item" + str(item)
                if freeze_poco(item1).offspring("Name").exists():
                    printcolor.printgreen("检查点 " + freeze_poco(item1).offspring("Name").get_text() + " 存在")
                else:
                    printcolor.printred("135龙器装备缺少控件，请检查")
                    screenshot.get_screen_shot(time.time(), devices, "135龙器装备缺少控件")
        else:
            printcolor.printred("继承界面缺少控件，请检查")
            screenshot.get_screen_shot(time.time(), devices, "继承界面缺少控件")
        poco("L_ring_03").click()  # 点击继承介绍

    else:
        printcolor.printred("物品制作页面 缺少控件，请检查")
        screenshot.get_screen_shot(time.time(), devices, "物品制作页面缺少控件")

    return poco("CommonHelpTip(Clone)").child("Title").get_text()