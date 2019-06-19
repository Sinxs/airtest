# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from airtest.core.api import *
from multi_processframe.Tools import screenshot, printcolor, adb_connect

def Artifact(devices):
    poco = adb_connect.device(devices)
    check_menu("SysAItem", poco) # 进入角色
    if poco("XSys_Artifact").exists(): # 进入龙器页签
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
                printcolor.printgreen("龙器界面，四个槽位，图册，帮助，数量，龙器页，龙器加成，龙器神炉UI元素显示正常")
            else:
                printcolor.printred("龙器界面UI元素显示异常，详情见截图")
                # screenshot.get_screen_shot(time.time(), devices, "龙器界面UI元素显示异常")
            try:
                freeze_poco("Prof").click() # 操作龙器页
                poco("ItemNewDlg(Clone)").offspring("item1").child("BtnUse").click()
                poco(texture="l_close_00")
                printcolor.printgreen("龙器页打开使用正常")
            except Exception as e:
                printcolor.printred("龙器页打开使用异常")
                printcolor.printred(e)
                screenshot.get_screen_shot(time.time(), devices, "龙器页打开使用异常")
                if poco(texture="l_close_00").exists():
                    poco(texture="l_close_00").click()
            try: # 操作 龙器加成，图册，规则
                freeze_poco("AttriBtn").click()
                freeze_poco("AttriBtn").click()
                freeze_poco("BtnShop").click()
                poco(texture="l_close_00").click()
                freeze_poco("ItemNewDlg(Clone)").offspring("Bg").offspring("RightPanel").offspring("ArtifactListPanel").child("Help").click()
                poco("Btn").click()
                printcolor.printgreen("操作 龙器加成，图册，规则点击正常")
            except Exception as e:
                printcolor.printred("帮助界面，龙器加成，图鉴点击异常")
                printcolor.printred(e)
                screenshot.get_screen_shot(time.time(), devices, "点击异常")
            try: # 操作龙器神炉
                poco("ComposeBtn").click()
                with poco.freeze() as freeze_poco:
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").child("Bg").offspring("XSys_Artifact_Comepose").child("Bg").click()
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").offspring("BtnCompose").click()
                    poco("BtnOneKeyCompose").click()
                    poco("ArtifactDeityStoveDlg(Clone)").offspring("ArtifactOneKeyFrame").offspring("Close").click()
                    freeze_poco("Get").click()
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").child("Bg").offspring("XSys_Artifact_Recast").child("Bg").click()  # 重铸
                    freeze_poco("Get").click()
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").child("Bg").offspring("XSys_Artifact_Fuse").child("Bg").click()  # 融合
                    freeze_poco("Get").click()
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").child("Bg").offspring("XSys_Artifact_Inscription").child("Bg").click()
                    poco("MoneyCost").click()
                    freeze_poco("ArtifactDeityStoveDlg(Clone)").child("Bg").offspring("XSys_Artifact_Refined").child("Bg").click()
                    freeze_poco("Get").click()
                    poco("ArtifactDeityStoveDlg(Clone)").offspring("Bg").child("Help").click()  # 帮助
                    poco("Btn").click()
                    freeze_poco(texture="l_close_00").click()
                    printcolor.printgreen("龙器神炉点击正常")
            except Exception as e:
                printcolor.printred("龙器神炉点击异常")
                printcolor.printred(e)
                screenshot.get_screen_shot(time.time(), devices, "龙器神炉点击异常")
        if poco("empty0").exists() and (not poco("ItemNewDlg(Clone)").offspring("item0").child("Icon").exists()):
            poco("Artifact0").click()  # 点击槽位
            poco("ListPanel").click()  # 点击跳转龙魂
            if poco("item0").child("value").get_text() == "0":
                poco("EnterBtn").click()  # 点击进入副本
                poco("access212").click()  # 点击进入
                poco("OK").click()
                poco("Close").click()
                poco("EnterBtn").click()  # 点击进入副本
            else:
                poco("EnterBtn").click()
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
        with poco.freeze() as freeze_poco:
            equipchild = freeze_poco("WrapContent").child()
            for i in equipchild:
                name = i.get_name()
                if name[:5] != "empty":
                    equipname = name
                    break
        poco(equipname).click() # 点击装备
        poco("Button1").click() # 穿戴装备
        for i in range(4):
            item = "item" + str(i)
            if poco("ItemNewDlg(Clone)").offspring(item).child("Icon").exists():
                printcolor.printgreen("龙器穿戴成功")
                break
            if i == 3:
                printcolor.printred("龙器穿戴失败")
    else:
        printcolor.printred("龙器功能暂未开放，请提升等级角色")
        # screenshot.get_screen_shot(time.time(), devices, "龙器功能暂未开放")
    poco("Close").click()
    return poco("Duck").get_name()   # 返回值poco("Duck").get_name()

def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 1:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco("MenuSwitchBtn").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()


# devices = "127.0.0.1:62001"
# Artifact(devices)