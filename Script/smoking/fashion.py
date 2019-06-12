# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import printcolor,adb_connect,screenshot

devices = "127.0.0.1:62025"
def fashion(devices):
    poco = adb_connect.device(devices)
    if poco("SysAItem").get_position()[1] > 1:
        poco(texture="halln_4").click()
    else:
        printcolor.printgreen("当前界面就有角色按钮")
    poco("SysAItem").click()
    if poco("XSys_Fashion").exists():  # 时装界面
        poco("XSys_Fashion").click()
        if poco("ItemNewDlg(Clone)").offspring("Frame").offspring("T").exists():
            printcolor.printgreen("进入时装界面成功...")
    else:
        printcolor.printred("没有找到时装按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "没有找到时装按钮")
    if poco("UIRoot(Clone)").offspring("Title").exists():
        poco("BtnCompose").click()  # 点击时装合成界面
        fashionlist=["S","A","B"]
        for i in fashionlist:
            if poco("UIRoot(Clone)").offspring("FashionCompoundDlg").offspring(f"Level_{i}").child("UnSelectLab").exists():
                printcolor.printgreen(f"检查 {i}"+poco("UIRoot(Clone)").offspring("FashionCompoundDlg").offspring(f"Level_{i}").child("UnSelectLab").get_text()+"存在")
        printcolor.printgreen(+poco("UIRoot(Clone)").offspring("Title").get_text()+"界面检查完成")
        poco(texture="l_close_00").click()
    else:
        printcolor.printred("没有弹出时装合成界面，请检查。。。")
        screenshot.get_screen_shot(time.time(), devices, "没有弹出时装合成界面")
    if poco("Btnclothes").exists():
        poco("Btnclothes").click()
        with poco.freeze() as freeze_poco:
            if freeze_poco("OutLook").child("TextLabel").exists() and \
                    freeze_poco("FashionRecord").child("TextLabel").exists() and \
                    freeze_poco("EquipRecord").child("TextLabel").exists():
                printcolor.printgreen("界面存在 "+freeze_poco("OutLook").child("TextLabel").get_text()+" 控件")
                printcolor.printgreen("界面存在 " + freeze_poco("FashionRecord").child("TextLabel").get_text() + " 控件")
                printcolor.printgreen("界面存在 " + freeze_poco("EquipRecord").child("TextLabel").get_text() + " 控件")
                printcolor.printgreen("时装收集界面检查完成")
                poco("OutLook").child("TextLabel").click()  # 外形设置
                with poco.freeze() as freeze_poco:
                    for item in range(len(freeze_poco("WrapContent").child())):
                        item1 = "item"+str(item)
                        if freeze_poco("WrapContent").child(item1).exists():
                            pass
                        else:
                            printcolor.printred("外形设置界面缺少控件，请检查。。。")
                            screenshot.get_screen_shot(time.time(), devices, "外形设置界面缺少控件")
                poco("FashionRecord").child("TextLabel")  # 时装收集
                with poco.freeze() as freeze_poco:
                    if freeze_poco("Attribute").child("Title").exists() and \
                            freeze_poco("Attribute").exists() and \
                            freeze_poco("Select").offspring("WrapContent").exists():
                        printcolor.printgreen("时装收集界面显示正确")
                    else:
                        printcolor.printred("时装收集界面缺少控件，请检查。。。")
                        screenshot.get_screen_shot(time.time(), devices, "时装收集界面缺少控件")
                poco("EquipRecord").child("TextLabel").click()
                with poco.freeze() as freeze_poco:
                    if poco(texture="l_frame_09").exists() and \
                        poco("Select").offspring("WrapContent").exists() and \
                        poco("Bg2").exists() and \
                        poco("EditPortrait").exists():
                        printcolor.printgreen("装备收集界面显示正确")
                    else:
                        printcolor.printred("装备收集界面缺少控件，请检查。。。")
                        screenshot.get_screen_shot(time.time(), devices, "装备收集界面缺少控件")


    else:
        printcolor.printred("当前界面没有衣柜换装控件，请检查。。。")
        screenshot.get_screen_shot(time.time(), devices, "没有找到衣柜换装控件")

fashion(devices)
