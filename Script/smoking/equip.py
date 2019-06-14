from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
Androidpoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from multi_processframe.Tools import printcolor,adb_connect


def addequip(poco):
    if not poco("Open").exists():
        poco("AvatarBG").child("P").click()
        Androidpoco("android.widget.Button").click()
        poco("SettingDlg(Clone)").offspring("Close").click()
        poco(text=">").click()
        text("item 11395600 1")
        Androidpoco("android.widget.Button").click()

        poco("AvatarBG").child("P").click()
        poco("Close").click()
        poco("Close").click()
        if poco("SysAItem").get_position()[1] > 1:  # 界面有角色按钮
            poco(texture="halln_4").click()
            poco("SysAItem").click()
            poco("equip11395600").click()
            poco("EquipToolTipDlg(Clone)").child("Bg").offspring("Button1").child("Label").click()  # 装备-装备
            poco("Close").click()
            poco("SysAItem").click()
        else:
            poco("SysAItem").click()
            poco("equip11395600").click()
            poco("EquipToolTipDlg(Clone)").child("Bg").offspring("Button1").child("Label").click()  # 装备-装备
            poco("Close").click()
    else:
        poco("Open").click()
        poco(text=">").click()
        text("item 11395600 1")
        Androidpoco("android.widget.Button").click()
        poco("AvatarBG").child("P").click()
        poco("Close").click()
        poco("Close").click()
        if poco("SysAItem").get_position()[1] > 1:  # 界面有角色按钮
            poco(texture="halln_4").click()
            poco("SysAItem").click()
            poco("equip11395600").click()
            poco("EquipToolTipDlg(Clone)").child("Bg").offspring("Button1").child("Label").click()  # 装备-装备
            poco("Close").click()
            poco("SysAItem").click()
        else:
            poco("SysAItem").click()
            poco("equip11395600").click()
            poco("EquipToolTipDlg(Clone)").child("Bg").offspring("Button1").child("Label").click()  # 装备-装备
            poco("Close").click()


def equip(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("SysAItem").exists():  # 角色按钮存在
        if poco("SysAItem").get_position()[0] > 1:  # 界面有角色按钮
            poco(texture="halln_4").click()
            poco("SysAItem").click()
        else:
            poco("SysAItem").click()
        if poco("ItemNewDlg(Clone)").offspring("item0").child("Quality").exists():  # 已经穿戴时装
            printcolor.printgreen("已经穿戴了装备")
            # todo:直接操作
        else:  # 先获取时装在穿戴后
            poco("Close").click()
            addequip(poco)
            if poco("SysAItem").get_position()[1] > 1:  # 界面有角色按钮
                poco(texture="halln_4").click()
                poco("SysAItem").click()
            else:
                poco("SysAItem").click()

        Buttonlist = [2, 3, 4, 5, 6, 8, 10, 11]  # 装备的各种操作
        for item in Buttonlist:  # 点击装备，进入装备的各种操作界面
            item1 = "Button"+str(item)
            item2 = poco(item1).child("Label")
            poco("ItemNewDlg(Clone)").offspring("item0").child("Quality").click()  # 点击装备
            printcolor.printgreen("进入  " + item2.get_text() + "  界面")
            poco(item1).click()  # 点击需要的装备操作选项
            if poco("ItemNewDlg(Clone)").offspring("Frame").child("p").child("p").exists():
                # printcolor.printgreen("进入界面测试完成")
                poco(texture="l_close_00").click()
            else:
                printcolor.printred("没有显示"+item2.get_text()+"界面，请检查---")



    else:  # 如果没有角色按钮
        printcolor.printred("当前界面没有找到角色按钮，请检查。。。")
    return poco("Title").get_text()

