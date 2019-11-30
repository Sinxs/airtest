"""
头衔模块-判断头衔晋升各个界面元素和勋章的合成
if 如果没有可以晋升的模块就不晋升
if 如果没有可以合成的勋章就不合成
环境准备：1、可以晋升头衔的账号，准备勋章 item 301 20、item 302 20
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from multi_processframe.ProjectTools import common
from airtest.core.api import *

def honor(start, devices):
    poco = common.deviceconnect(devices)
    if poco("SysAItem").exists():
        if poco("SysAItem").get_position()[0] > 1:  # 界面有角色按钮
            poco(texture="halln_4").click()
        poco("SysAItem").click()  # 点击角色按钮
    else:
        common.printgreen("主界面没有角色按钮，请检查...")
        common.get_screen_shot(start, time.time(), devices, "主界面没有角色按钮")
    if poco("XSys_Item_Equip").exists():
        poco("XSys_Item_Equip").click()  # 点装备按钮
        if poco("ShowTitle").exists():
            poco("ShowTitle").click()  # 点击头衔按钮
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if freeze_poco("TitleDlg(Clone)").offspring("Title").exists():
                common.printgreen("进入头衔晋升界面")
                common.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Title").get_text() + " 显示正确")
                common.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current").offspring("FightLabel")
                                  .get_text() + " 显示正确")
                common.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current").offspring("item0")
                                  .child("Label").get_text() + " 显示正确")
                common.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current").offspring("item1")
                                  .child("Label").get_text() + " 显示正确")
                common.printgreen("点击晋升....")
                poco("Promote").click()  # 点击晋升
                if poco("KeepOn").wait(6).exists():  # 如果有可以晋升的头衔，就点击晋升，但是只点击一次
                    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                    common.printgreen("进入头衔晋升界面")
                    common.printgreen("检查点 " + freeze_poco("TitleShareDlg(Clone)").child("Bg").child("Title")
                                      .get_text() + " 显示正确")
                    common.printgreen("检查点 " + freeze_poco("Message").get_text() + " 显示正确")
                    if poco("KeepOn").exists():
                        common.printgreen("点击屏幕继续...")
                        poco("KeepOn").wait(6).click()  # 点击屏幕继续
                        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                        if freeze_poco("TitleDlg(Clone)").offspring("Title").exists():
                            common.printgreen("进入头衔晋升界面")
                            common.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Title").get_text()
                                              + " 显示正确")
                            common.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current")
                                              .offspring("FightLabel").get_text() + " 显示正确")
                            common.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current")
                                              .offspring("item0").child("Label").get_text() + " 显示正确")
                            common.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current")
                                              .offspring("item1").child("Label").get_text() + " 显示正确")
                            poco(texture="l_close_00").click()
                            poco("XSys_Bag_Item").click()  # 点击背包按钮
                            common.printgreen("点击返回到角色界面，并且点击背包按钮，下面开始测试勋章合成功能")
                        else:
                            common.printred("没有返回晋升界面，请检查...")
                            common.get_screen_shot(start, time.time(), devices, "没有返回晋升界面")
                else:
                    common.printgreen("没有可以晋升的选项，无法晋升")
                    poco(texture="l_close_00").click()
                    poco("XSys_Bag_Item").click()  # 点击背包按钮
                    common.printgreen("点击返回到角色界面，并且点击背包按钮，下面开始测试勋章合成功能")
                if poco("ItemNewDlg(Clone)").offspring("item301").child("Num").exists():  # 判断背包中勋章的数量，如果数量不足以合成就跳过
                    common.printgreen("背包存在战斗勋章，开始检查勋章数量")
                    if int(poco("ItemNewDlg(Clone)").offspring("item301").child("Num").get_text()) > 3:
                        common.printgreen("战斗勋章数量>3，开始进行合成操作...")
                        poco("ItemNewDlg(Clone)").offspring("item301").click()
                        freeze_poco = poco.freeze()  # TODO：定义冻结poco
                        if freeze_poco("TopFrame").offspring("Name").exists():
                            common.printgreen("检查点 " + freeze_poco("Text0").offspring("T").get_text() + "     "
                                              + freeze_poco("Text0").get_text() + "      显示正确")
                            common.printgreen("检查点 " + freeze_poco("Text1").offspring("T").get_text() + "     "
                                              + freeze_poco("Text1").get_text() + "      显示正确")
                            common.printgreen("检查点 " + freeze_poco("Text2").offspring("T").get_text() + "     "
                                              + freeze_poco("Text2").get_text() + "      显示正确")
                            common.printgreen("检查点 " + freeze_poco("Binding").offspring("T").get_text() + "     "
                                              + freeze_poco("Binding").offspring("Yes").get_text() + "        显示正确")
                            common.printgreen("检查点 " + freeze_poco("Description").offspring("Title").get_text() +
                                              "     " + freeze_poco("Text").get_text() + "        显示正确")
                            if poco("Button1").exists():
                                common.printgreen("点击晋升按钮")
                                poco("Button1").click()  # 点击晋升
                                if poco("Title").exists():
                                    common.printgreen("进入晋升界面成功")
                                    poco(texture="l_close_00").click()  # 点击返回
                                    poco("ItemNewDlg(Clone)").offspring("item301").click()  # 再次点击勋章
                                else:
                                    common.printred("晋升界面元素控件缺失，请检查...")
                                    common.get_screen_shot(start, time.time(), devices, "没有弹出晋升弹窗")
                            else:
                                common.printred("没有弹出晋升弹窗，请检查...")
                                common.get_screen_shot(start, time.time(), devices, "没有弹出晋升弹窗")
                            if poco("Button5").exists():  # 点击勋章升级按钮
                                poco("Button5").click()
                                if poco("GreyModalDlg(Clone)").child("Bg").child("Label").exists():
                                    common.printgreen("检查点 " + poco("GreyModalDlg(Clone)").child("Bg").child("Label")
                                                      .get_text() + "显示正确")
                                    poco("OK").click()  # 点击确定按钮，进行合成
                                    common.printgreen("合成成功")
                            else:
                                common.printred("没有弹出合成弹窗，请检查...")
                                common.get_screen_shot(start, time.time(), devices, "没有弹出合成弹窗")
                    else:
                        common.printred("背包没有勋章，不做合成操作", "blue")
                        common.get_screen_shot(start, time.time(), devices, "勋章不足")
                else:
                    common.printred("背包没有勋章，不做合成操作", "blue")
                    common.get_screen_shot(start, time.time(), devices, "背包没有勋章")
                if poco("ItemNewDlg(Clone)").offspring("item302").child("Num").exists():  # 判断背包中勋章的数量，如果数量不足以合成就跳过
                    common.printgreen("背包存在宫廷勋章，开始检查勋章数量")
                    if int(poco("ItemNewDlg(Clone)").offspring("item302").child("Num").get_text()) > 3:
                        common.printgreen("宫廷勋章数量>3，开始进行合成操作...")
                        poco("ItemNewDlg(Clone)").offspring("item302").click()
                        freeze_poco = poco.freeze()  # TODO：定义冻结poco
                        if freeze_poco("TopFrame").offspring("Name").exists():
                            common.printgreen("检查点 " + freeze_poco("Text0").offspring("T").get_text() + "     "
                                              + freeze_poco("Text0").get_text() + "      显示正确")
                            common.printgreen("检查点 " + freeze_poco("Text1").offspring("T").get_text() + "     "
                                              + freeze_poco("Text1").get_text() + "      显示正确")
                            common.printgreen("检查点 " + freeze_poco("Text2").offspring("T").get_text() + "     "
                                              + freeze_poco("Text2").get_text() + "      显示正确")
                            common.printgreen("检查点 " + freeze_poco("Binding").offspring("T").get_text() + "     "
                                              + freeze_poco("Binding").offspring("Yes").get_text() + "        显示正确")
                            common.printgreen("检查点 " + freeze_poco("Description").offspring("Title").get_text()
                                              + "     " + freeze_poco("Text").get_text() + "        显示正确")
                            if poco("Button1").exists():
                                common.printgreen("点击晋升按钮")
                                poco("Button1").click()  # 点击晋升
                                if poco("Title").exists():
                                    common.printgreen("进入晋升界面成功")
                                    poco(texture="l_close_00").click()  # 点击返回
                                    poco("ItemNewDlg(Clone)").offspring("item302").click()  # 再次点击勋章
                                else:
                                    common.printred("晋升界面元素控件缺失，请检查...")
                                    common.get_screen_shot(start, time.time(), devices, "没有弹出晋升弹窗")
                            else:
                                common.printred("没有弹出晋升弹窗，请检查...")
                                common.get_screen_shot(start, time.time(), devices, "没有弹出晋升弹窗")
                            if poco("Button5").exists():  # 点击勋章升级按钮
                                poco("Button5").click()
                                if poco("GreyModalDlg(Clone)").child("Bg").child("Label").exists():
                                    common.printgreen("检查点 " + poco("GreyModalDlg(Clone)").child("Bg").child("Label")
                                                      .get_text() + "显示正确")
                                    poco("OK").click()  # 点击确定按钮，进行合成
                                    common.printgreen("合成成功")
                            else:
                                common.printred("没有弹出合成弹窗，请检查...")
                                common.get_screen_shot(start, time.time(), devices, "没有弹出合成弹窗")
                    else:
                        common.printgreen("宫廷勋章不足，不做合成操作")
                        common.get_screen_shot(start, time.time(), devices, "勋章不足")
                else:
                    common.printred("背包没有勋章，不做合成操作", "blue")
                    common.get_screen_shot(start, time.time(), devices, "背包没有勋章")
        else:
            common.printred("没有进入装备界面，请检查...")
            common.get_screen_shot(start, time.time(), devices, "主界面缺少日常按钮")
    else:
        common.printred("没有进入装备界面，请检查...")
        common.get_screen_shot(start, time.time(), devices, "主界面缺少日常按钮")
    return poco("ItemNewDlg(Clone)").offspring("Frame").offspring("T").get_text()


if __name__ == "__main__":
    start = time.localtime()
    honor(start, "e37c0280")
