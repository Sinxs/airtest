"""
时装模块
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from multi_processframe.ProjectTools import common


def fashion(start, devices):
    poco = common.deviceconnect(devices)
    if poco("SysAItem").get_position()[0] > 1:
        poco(texture="halln_4").click()
    else:
        common.printgreen("当前界面就有角色按钮")
    poco("SysAItem").click()
    if poco("XSys_Fashion").exists():  # 时装界面
        poco("XSys_Fashion").click()
        if poco("ItemNewDlg(Clone)").offspring("Frame").offspring("T").exists():
            common.printgreen("进入时装界面成功...")
    else:
        common.printred("没有找到时装按钮，请检查...")
        common.get_screen_shot(start, time.time(), devices, "没有找到时装按钮")
    if poco("BtnAttrTotal").exists():
        poco("BtnAttrTotal").click()  # 点击时装属性
        if poco("ItemNewDlg(Clone)").offspring("Bg").exists():  # 弹出时装属性弹窗
            poco("BtnAttrTotal").click()  # 任意点击可以取消
    else:
        common.printred("界面没有找到时装属性按钮，请检查")
        common.get_screen_shot(start, time.time(), devices, "界面没有找到时装属性按钮")
    if poco("BtnShop").exists():
        poco("BtnShop").click()  # 点击时装获取
        if poco("ItemAccessDlg(Clone)").offspring("Title").exists():
            poco(texture="l_close_00").click()  # 点击返回
            if poco("ItemAccessDlg(Clone)").offspring("Title").exists():  # 作为容错机制，如果没有返回就重新点击
                poco(texture="l_close_00").click()  # 点击返回
    else:
        common.printred("界面没有找到时装获取按钮，请检查")
        common.get_screen_shot(start, time.time(), devices, "界面没有找到时装获取按钮")
    if poco("UIRoot(Clone)").offspring("Title").exists():
        poco("BtnCompose").click()  # 点击时装合成界面
        fashionlist=["S","A","B"]
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        for i in fashionlist:
            if freeze_poco("UIRoot(Clone)").offspring("FashionCompoundDlg")\
                    .offspring(f"Level_{i}").child("UnSelectLab").exists():
                common.printgreen(f"检查 {i}" + freeze_poco("UIRoot(Clone)").offspring("FashionCompoundDlg")
                                  .offspring(f"Level_{i}").child("UnSelectLab").get_text() + "存在")
        common.printgreen(poco("UIRoot(Clone)").offspring("Title").get_text() + " -- 界面检查完成")
        poco(texture="l_close_00").click()
    else:
        common.printred("没有弹出时装合成界面，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "没有弹出时装合成界面")
    if poco("Btnclothes").exists():
        poco("Btnclothes").click()
        with poco.freeze() as freeze_poco:
            if freeze_poco("OutLook").child("TextLabel").exists() and \
                    freeze_poco("FashionRecord").child("TextLabel").exists() and \
                    freeze_poco("EquipRecord").child("TextLabel").exists():
                common.printgreen("界面检查点   " + freeze_poco("OutLook").child("TextLabel").get_text() + " 存在")
                common.printgreen("界面检查点    " + freeze_poco("FashionRecord").child("TextLabel").get_text() + " 存在")
                common.printgreen("界面检查点    " + freeze_poco("EquipRecord").child("TextLabel").get_text() + " 存在")
                common.printgreen("衣柜换装  界面检查完成")
                poco("OutLook").child("TextLabel").click()  # 外形设置
                with poco.freeze() as freeze_poco:
                    for item in range(len(freeze_poco("ScrollView").child("WrapContent").child())):
                        item1 = "item"+str(item)
                        if freeze_poco("WrapContent").child(item1).child("Bg").exists() and freeze_poco("Bg2").exists():
                            common.printgreen("外形设置检查点 " + freeze_poco(item1).offspring("TextLabel")
                                              .get_text() + "显示正确")
                        else:
                            common.printred("外形设置界面缺少控件，请检查。。。")
                            common.get_screen_shot(start, time.time(), devices, "外形设置界面缺少控件")
                poco("FashionRecord").child("TextLabel").click()  # 时装收集
                with poco.freeze() as freeze_poco:
                    if freeze_poco("Attribute").child("Title").exists() and \
                            freeze_poco("Attribute").exists() and \
                            freeze_poco("Select").offspring("WrapContent").exists():
                        common.printgreen("时装收集界面显示正确")
                    else:
                        common.printred("时装收集界面缺少控件，请检查。。。")
                        common.get_screen_shot(start, time.time(), devices, "时装收集界面缺少控件")
                poco("EquipRecord").child("TextLabel").click()  # 装备收集

                with poco.freeze() as freeze_poco:
                    if freeze_poco(texture="l_frame_09").exists() and \
                            freeze_poco("Select").offspring("WrapContent").exists() and \
                            freeze_poco("Bg2").exists() and \
                            freeze_poco("EditPortrait").exists():
                        for item in range(len(freeze_poco("Select").offspring("WrapContent").child())):
                            item1 = "item"+str(item)
                            if freeze_poco("Select").offspring(item1).offspring("TextLabel").exists():
                                common.printgreen("装备收集界面检查点  " + freeze_poco("Select").offspring(item1)
                                                  .offspring("TextLabel").get_text() + "  显示正确")
                            else:
                                common.printred("装备收集界面缺少控件，请检查。。。")
                                common.get_screen_shot(start, time.time(), devices, "装备收集界面缺少控件")
    else:
        common.printred("当前界面没有衣柜换装控件，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "没有找到衣柜换装控件")
    return poco("Attribute").child("T").get_text()


if __name__ == "__main__":
    start = time.localtime()
    fashion(start, "e37c0280")