"""
装备模块-
脚本环境
1、角色需要有一套显示所有功能的装备（高级装备），需要手动添加，如果没有装备就略过去
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.ProjectTools import common


def equip(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("SysAItem").exists():  # 角色按钮存在
        if poco("SysAItem").get_position()[0] > 1:  # 界面有角色按钮
            poco(texture="halln_4").click()
            poco("SysAItem").click()
            poco("XSys_Item_Equip").click()
        else:
            poco("SysAItem").click()
            poco("XSys_Item_Equip").click()
        for item in range(len(poco("EquipFrame").child())-2):
            item3 = "item" + str(item)
            if poco("ItemNewDlg(Clone)").offspring(item3).child("Quality").exists():  # 已经穿戴时装
                equip = poco("ItemNewDlg(Clone)").offspring(item3).child("Quality")
                common.printgreen("已经穿戴了装备")
                # todo:直接操作
                Buttonlist = [2, 3, 4, 5, 6, 8]  # 装备的各种操作
                for item in Buttonlist:  # 点击装备，进入装备的各种操作界面
                    item1 = "Button" + str(item)
                    item2 = poco(item1).child("Label")
                    equip.click()  # 点击装备
                    if item2.exists():
                        common.printgreen("进入  " + item2.get_text() + "  界面")
                        poco(item1).click()  # 点击需要的装备操作选项
                        if poco("ItemNewDlg(Clone)").offspring("Frame").child("p").child("p").exists():
                            # printcolor.printgreen("进入界面测试完成")
                            poco(texture="l_close_00").click()
                        else:
                            common.printred("没有显示" + item2.get_text() + "界面，请检查---")
                    else:
                        common.printgreen("当前装备缺少 <装备相关> 选项,请更换更高级的装备")
                return poco("Title").get_text()
        else:  # 先获取时装在穿戴后
            common.printred("角色没有穿装备，请准备好测试环境在跑当前脚本，测试环境准备条件在当前脚本的最上方..")
    else:  # 如果没有角色按钮
        common.printred("当前界面没有找到角色按钮，请检查。。。")


if __name__ == "__main__":
    start = time.localtime()
    equip("e37c0280")
