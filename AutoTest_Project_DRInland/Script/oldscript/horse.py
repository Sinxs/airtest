# -*- encoding=utf8 -*-
__author__ = "Lee.li"

from airtest.core.api import *
from multi_processframe.ProjectTools import common, common, common
from multi_processframe.ProjectTools import common

def horse_befor(start, devices):
    """
    1.进入主界面
    2.点击坐骑按钮
    3.依次点击坐骑图标，查看坐骑模型是否正常
    """
    horselist = [1, ]
    poco = common.deviceconnect(devices)
    check_menu("SysEHorse", poco) # 调用函数查看主界面坐骑按钮是否可点击
    poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
    with poco.freeze() as freeze_poco:
        petgrid = freeze_poco("Grid").child()  # 获取目前所有坐骑数量
    for x in range(20):
        if poco("Grid").child("item0").get_position()[1] < 0.145:
            common.setswipe(1, (486, 170), (486, 889), devices)
        else:
            break
    for i in range(len(petgrid)//2):
        item = "item" + str(i)
        if i >= 25:
            for i in range(20):
                if poco("Grid").child(item).get_position()[1] > 0.9:
                    common.setswipe(1, (200, 560), (200, 180), devices)
                elif poco("Grid").child(item).get_position()[1] < 0.12:
                    common.setswipe(1, (200, 180), (200, 560), devices)
                else:
                    break
        poco("Grid").offspring(item).click()  # 点击坐骑icon
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("Btnhave").exists() or freeze_poco("BtnMount").exists(): #判断坐骑打开是否正常是否存在
            petname = freeze_poco("PetName").offspring("Name").get_text() # 获得当前坐骑的名称
            common.printgreen(f"{petname}坐骑查看正常", end=",")
            try:
                snapshotnumber = freeze_poco("PetMainDlg(Clone)").child("Bg").child("Snapshot").child().get_name()
                if snapshotnumber.isnumeric() == True:
                    if any(snapshotnumber != s for s in horselist):  # 判断snapshotnumber是否在horselist中出现过,如果没有
                        common.printgreen(f"坐骑模型配置存在", end=",")
                        horselist.append(snapshotnumber)
                    else:
                        common.printred(f"{petname}模型与之前的重复", end=",")
                        common.get_screen_shot(start, time.time(), devices, "坐骑模型不显示")
                else:
                    common.printred("坐骑模型配置不存在，请详细查看", end=",")
                    common.get_screen_shot(start, time.time(), devices, "坐骑模型不显示")
            except Exception as e:
                print(e)
                common.printred("坐骑模型配置不存在，请详细查看", end=",")
                common.get_screen_shot(start, time.time(), devices, "坐骑模型不显示")

            if freeze_poco("Btnhave").exists():
                poco("Btnhave").click()
                if poco("ItemToolTipDlg(Clone)").child("Bg").offspring("TopFrame").child("Name").exists():
                    common.printgreen("获取界面打开正常")
                    common.settouch(1, 1140, 540, devices, times=2)
                else:
                    common.printgreen("没有相关坐骑信息，请查具体查看该坐骑！")
                    common.get_screen_shot(start, time.time(), devices, "没有获取到该坐骑相关信息")
                    common.settouch(1, 1140, 540, devices, times=2)
            else:
                if freeze_poco("BtnMount").exists():
                    print("坐骑已经获得，没有获取途径")
                else:
                    common.printred("没有相关坐骑信息，请查具体查看该坐骑！")
                    common.get_screen_shot(start, time.time(), devices, "没有获取到该坐骑相关信息")
        else:
            common.printred("没有获取到该坐骑相关信息")
            common.get_screen_shot(start, time.time(), devices, "没有获取到该坐骑相关信息")
        poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
        time.sleep(1)
    return poco("Btnhave").get_name() # 返回值

def horse_after(start, devices):
    """
    1.进入主界面
    2.点击坐骑按钮
    3.依次点击坐骑图标，查看坐骑模型是否正常
    """
    horselist = [1, ]
    poco = common.deviceconnect(devices)
    check_menu("SysEHorse", poco) # 调用函数查看主界面坐骑按钮是否可点击
    poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
    with poco.freeze() as freeze_poco:
        petgrid = freeze_poco("Grid").child()  # 获取目前所有坐骑数量
    for i in range(len(petgrid)//2,len(petgrid)):
        item = "item" + str(i)
        for i in range(20):
            if poco("Grid").child(item).get_position()[1] > 0.9:
                common.setswipe(1, (200, 560), (200, 180), devices)
            elif poco("Grid").child(item).get_position()[1] < 0.12:
                common.setswipe(1, (200, 180), (200, 560), devices)
            else:
                break
        poco("Grid").offspring(item).click()  # 点击坐骑icon
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("Btnhave").exists() or freeze_poco("BtnMount").exists(): #判断坐骑打开是否正常是否存在
            petname = freeze_poco("PetName").offspring("Name").get_text() # 获得当前坐骑的名称
            common.printgreen(f"{petname}坐骑查看正常", end=",")
            try:
                snapshotnumber = freeze_poco("PetMainDlg(Clone)").child("Bg").child("Snapshot").child().get_name()
                if snapshotnumber.isnumeric() == True:
                    if any(snapshotnumber != s for s in horselist):  # 判断snapshotnumber是否在horselist中出现过,如果没有
                        common.printgreen(f"坐骑模型配置存在", end=",")
                        horselist.append(snapshotnumber)
                    else:
                        common.printred(f"{petname}模型与之前的重复", end=",")
                        common.get_screen_shot(start, time.time(), devices, "坐骑模型不显示")
                else:
                    common.printred("坐骑模型配置不存在，请详细查看", end=",")
                    common.get_screen_shot(start, time.time(), devices, "坐骑模型不显示")
            except Exception as e:
                print(e)
                common.printred("坐骑模型配置不存在，请详细查看", end=",")
                common.get_screen_shot(start, time.time(), devices, "坐骑模型不显示")

            if freeze_poco("Btnhave").exists():
                poco("Btnhave").click()
                if poco("ItemToolTipDlg(Clone)").child("Bg").offspring("TopFrame").child("Name").exists():
                    common.printgreen("获取界面打开正常")
                    common.settouch(1, 1140, 540, devices, times=2)
                else:
                    common.printgreen("没有相关坐骑信息，请查具体查看该坐骑！")
                    common.get_screen_shot(start, time.time(), devices, "没有获取到该坐骑相关信息")
                    common.settouch(1, 1140, 540, devices, times=2)
            else:
                if freeze_poco("BtnMount").exists():
                    print("坐骑已经获得，没有获取途径")
                else:
                    common.printred("没有相关坐骑信息，请查具体查看该坐骑！")
                    common.get_screen_shot(start, time.time(), devices, "没有获取到该坐骑相关信息")
        else:
            common.printred("没有获取到该坐骑相关信息")
            common.get_screen_shot(start, time.time(), devices, "没有获取到该坐骑相关信息")
        poco("NewBtn").child("BtnBg").click() # 打开坐骑列表
        time.sleep(1)

    return poco("Btnhave").get_name() # 返回值






def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 0.82:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco(texture="switch").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()

# devices = "127.0.0.1:62001"
# horse_befor(devices)