from multi_processframe.Tools import printcolor,adb_connect,screenshot
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

devices = "127.0.0.1:62025"
def butpos(butpos,pos1=0.4,pos2=0.81,high=1330,low=930,lows=482):
    """
把不在屏幕内部的控件滑动到屏幕内，使之可被操作
:param butpos: 控件的坐标值
:param pos1: 希望控件所在屏幕上的最低限
:param pos2: 希望控件所在屏幕上的最上限
:param high: 固定坐标
:param low: 滑动起始或终点位置
:param lows: 滑动起始或终点位置
:return:
    """
    for i in range(20):
        but = butpos.get_position()
        if but[1] < pos1:
            swipe([high, lows], [high, low], 5)
        elif but[1] > pos2:
            swipe([high, low], [high, lows], 5)
        else:
            break

def manufacture():
    poco = adb_connect.device(devices)
    if poco("SysDEquipCreate").get_position()[0] > 1:
        poco(texture="halln_4").click()
    else:
        printcolor.printgreen("当前界面就有角色按钮")
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
                poco(text="装备套装").exists() and \
                poco("红龙套装").exists() and \
                poco("冰龙套装").exists() and \
                poco("符文龙套装").exists():
            printcolor.printgreen("检查点  装备升级界面显示正确")
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            poco("红龙套装").click()
            if 

    else:
        printcolor.printred("物品制作页面 缺少控件，请检查")
        screenshot.get_screen_shot(time.time(), devices, "物品制作页面缺少控件")
    poco("XSys_EquipCreate_EquipSet").click()  # 点击装备制作







