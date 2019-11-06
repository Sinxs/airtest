# -*- encoding=utf8 -*-
__author__ = "Lee.li"
import random
from multi_processframe.ProjectTools.common import *
from airtest.core.api import *


def Artifact(start, devices):
    poco = deviceconnect(devices)
    check_menu("SysAItem", poco)  # 进入角色
    if poco("XSys_Artifact").exists():  # 进入龙器页签
        poco("XSys_Artifact").click()
        with poco.freeze() as freeze_poco:
            if freeze_poco("Artifact0").child("t").exists() and \
                    freeze_poco("Artifact1").child("t").exists() and \
                    freeze_poco("Artifact2").child("t").exists() and \
                    freeze_poco("Artifact3").child("t").exists() and \
                    freeze_poco("BtnShop").exists() and \
                    freeze_poco("BagNum").exists() and \
                    freeze_poco("ItemNewDlg(Clone)").offspring("Help").exists() and \
                    freeze_poco("Prof").exists() and \
                    freeze_poco("AttriBtn").exists() and \
                    freeze_poco("ComposeBtn").exists():
                printgreen("龙器界面，四个槽位，图册，帮助，数量，龙器页，龙器加成，龙器神炉UI元素显示正常")
            else:
                printred("龙器界面UI元素显示异常，详情见截图")
                get_screen_shot(start, time.time(), devices, "龙器界面UI元素显示异常")
            try:
                freeze_poco("Prof").click()  # 操作龙器页
                item = "item" + str(random.randint(1, 10))  # 产生一个随机数，随机点击使用标签页
                poco("ScrollView").child(item).child("BtnUse").click()  # 点击使用标签页
                if poco(texture="l_close_00").exists():
                    poco(texture="l_close_00").click()
                printgreen("龙器页打开使用正常")
            except Exception as e:
                printred("龙器页打开使用异常")
                printred(e)
                get_screen_shot(start, time.time(), devices, "龙器页打开使用异常")
                if poco(texture="l_close_00").exists():
                    poco(texture="l_close_00").click()
            try:  # 操作 龙器加成，图册，规则
                freeze_poco("AttriBtn").click()
                if poco("ItemNewDlg(Clone)").offspring("ArtifactFrame").offspring("Panel").exists():
                    printgreen("龙器加成页打开正常")
                    touch([0.5, 0.5])
                else:
                    printred("龙器加成页打开失败")
                    get_screen_shot(start, time.time(), devices, "龙器加成页打开失败")
                freeze_poco("BtnShop").click()
                poco(texture="l_close_00").click()
                printgreen("操作 龙器加成，图册点击正常")
            except Exception as e:
                printred("帮助界面，龙器加成，图鉴点击异常")
                printred(e)
                get_screen_shot(start, time.time(), devices, "点击异常")
            try:  # 操作龙器神炉
                poco("ComposeBtn").click()
                with poco.freeze() as freeze_poco:
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").child("Bg").offspring("XSys_Artifact_Comepose").child(
                        "Bg").click()
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").offspring("BtnCompose").click()
                    poco("BtnOneKeyCompose").click()
                    poco("ArtifactDeityStoveDlg(Clone)").offspring("ArtifactOneKeyFrame").offspring("Close").click()
                    freeze_poco("Get").click()
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").child("Bg").offspring("XSys_Artifact_Recast").child(
                        "Bg").click()  # 重铸
                    freeze_poco("Get").click()
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").child("Bg").offspring("XSys_Artifact_Fuse").child(
                        "Bg").click()  # 融合
                    freeze_poco("Get").click()
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").child("Bg").offspring(
                        "XSys_Artifact_Inscription").child("Bg").click()
                    poco("MoneyCost").click()
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").child("Bg").offspring("XSys_Artifact_Refined").child(
                        "Bg").click()
                    freeze_poco("Get").click()
                    poco("ArtifactDeityStoveDlg(Clone)").offspring("Bg").child("Help").click()  # 帮助
                    poco("Btn").click()
                    freeze_poco(texture="l_close_00").click()
                    printgreen("龙器神炉点击正常")
            except Exception as e:
                printred("龙器神炉点击异常")
                printred(e)
                get_screen_shot(start, time.time(), devices, "龙器神炉点击异常")
        if poco("empty0").exists() and (not poco("ItemNewDlg(Clone)").offspring("item0").child("Icon").exists()):
            poco("Artifact0").click()  # 点击槽位
            poco("ListPanel").click()  # 点击跳转龙魂
            if poco("item0").child("value").get_text() == "0":
                poco("EnterBtn").click()  # 点击进入副本
                poco("access212").click()  # 点击进入
                poco("OK").click()
                poco("Close").click()
                poco("EnterBtn").click()  # 点击进入副本
                printgreen("龙魂禁地门票购买成功")
                print("进入龙魂禁地副本大龙器")
            else:
                poco("EnterBtn").click()
                print("进入龙魂禁地副本大龙器")
            time.sleep(10)
            if poco("AutoPlayCancel").exists():
                pass
            else:
                poco("AutoPlay").click()
            time.sleep(90)
            if poco("ItemIconListBattleDlg(Clone)").offspring("Bg").child("Close").exists():
                poco("ItemIconListBattleDlg(Clone)").offspring("Bg").child("Close").click()
                poco("Close").click()
                check_menu("SysAItem", poco)
                poco("XSys_Artifact").click()
            else:
                printred("没有穿戴装备，龙魂禁地打不过去，请穿戴装备后再次执行脚本")
                get_screen_shot(start, time.time(), devices, "没有穿戴装备，龙魂禁地打不过去，请穿戴装备后再次执行脚本")
                poco("Pause").click()
                poco("Leave").click()
                time.sleep(8)
                poco("Close").click()
        if poco("XSys_Artifact").exists():
            poco("XSys_Artifact").click()
            with poco.freeze() as freeze_poco:
                equipchild = freeze_poco("WrapContent").child()
                for i in equipchild:
                    name = i.get_name()
                    if name[:5] != "empty":
                        equipname = name
                        break
            poco(equipname).click()  # 点击装备
            poco("Button1").click()  # 穿戴装备
            for i in range(4):
                item = "item" + str(i)
                if poco("ItemNewDlg(Clone)").offspring(item).child("Icon").exists():
                    printgreen("龙器穿戴成功")
                    with poco.freeze() as freeze_poco:
                        for x in freeze_poco("ArtifactFrame").child("Panel").child("Artifacts").offspring("Quality"):
                            uiname = x.parent().get_name()
                            freeze_poco(uiname).click()
                            poco("Button1").click()  # 穿戴装备
                    printgreen("龙器卸下成功")
                    break
                if i == 3:
                    printred("龙器穿戴失败")
    else:
        printred("龙器功能暂未开放，请提升等级角色")
        get_screen_shot(start, time.time(), devices, "龙器功能暂未开放")
    return poco("AttriBtn").get_name()  # 返回值poco("Duck").get_name()


def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 1:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco("MenuSwitchBtn").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()


if __name__ == "__main__":
    # start = time.localtime()
    # Artifact(start, "9b57691d")
    del_progress()

