# -*- encoding=utf8 -*-
__author__ = "Lee.li"

# 系统设置
# 推送设置
# 视角设置
# 个人信息	个性展示-连击框

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.ProjectTools import common, common, common
import traceback
from multi_processframe.ProjectTools import common


def setting(start, devices):
    poco = common.deviceconnect(devices)
    poco("Avatar").click()
    common.settouch(1, 1140, 540, devices, times=2)
    if poco("SettingDlg(Clone)").exists(): # 打开设置
        uiname = poco("SettingDlg(Clone)").offspring("Bg").offspring("Bg1").child("T").get_text()
        common.printgreen(f"{uiname}  界面打开成功")

        if poco("InfoTab").exists(): # 个人信息
            poco("InfoTab").click()
            poco("PrerogativeBtn").click()
            if poco("PrerogativeFrame(Clone)").offspring("Bg").child("Bg1").exists(): # 个性展示
                if poco("DebugDlg(Clone)").offspring("Close").exists():
                    poco("DebugDlg(Clone)").offspring("Close").click()
                common.setswipe(1, (335, 260), (335, 576), devices)
                uiname = poco("PrerogativeFrame(Clone)").offspring("Bg").offspring("Bg1").child("T").get_text()
                common.printgreen(f"{uiname}  界面打开成功")
                if poco("RuleBtn").exists(): # 规则详情
                    poco("RuleBtn").click()
                    if poco("CommonHelpTip(Clone)").exists(): # 个性显示规则
                        uiname = poco("CommonHelpTip(Clone)").child("Title").get_text()
                        common.printgreen(f"{uiname}  界面打开成功")
                        poco("CommonHelpTip(Clone)").child("Btn").click()
                        if not poco("CommonHelpTip(Clone)").exists():
                            common.printgreen("规则详情界面关闭正常")
                        else:
                            common.printred("规则详情界面关闭异常")
                            common.get_screen_shot(start, time.time(), devices, "规则详情界面关闭异常")
                    else:
                        common.printred("个性显示规则界面打开失败")
                        common.get_screen_shot(start, time.time(), devices, "个性显示规则界面打开失败")
                else:
                    common.printred("规则详情打开异常")
                    common.get_screen_shot(start, time.time(), devices, "规则详情打开异常")
                if poco("ShopBtn").exists(): # 个性商店
                    poco("ShopBtn").click()
                    uiname = poco("ShopName").get_text()
                    common.printgreen(f"{uiname}  界面打开成功")
                    poco("Close").click()
                    if poco("PrerogativeFrame(Clone)").offspring("Bg").child("Bg1").exists():
                        common.printgreen("个性商店关闭正常")
                    else:
                        common.printred("个性商店关闭异常")
                        common.get_screen_shot(start, time.time(), devices, "个性商店关闭异常")
                else:
                    common.printred("个性商店打开失败")
                    common.get_screen_shot(start, time.time(), devices, "个性商店打开失败")
                for i in range(6):
                    if i == 4:
                        common.setswipe(1, (335, 567), (335, 260), devices)
                        for a in range(20):
                            if poco("PrerogativeFrame(Clone)").offspring("PreList").offspring("item4").get_position()[1] > 0.9:
                                common.setswipe(1, (335, 567), (335, 260), devices)
                            else:
                                break
                    item = f"item{i}"
                    if poco("PrerogativeFrame(Clone)").offspring("PreList").offspring(item).exists():
                        poco("PrerogativeFrame(Clone)").offspring("PreList").offspring(item).click()
                        uiname = poco("PrerogativeFrame(Clone)").offspring("PreList").offspring(item).child("Text").get_text()
                        childuiname = poco("TLabel").get_text()
                        childnumber = poco("PrerogativeFrame(Clone)").offspring("WrapContent").child()
                        if len(childnumber) <1:
                            common.printred(f"{uiname}的物品数量异常，请查看具体情况")
                        else:
                            common.printgreen(f"按钮{uiname}打开正常，table页签{childuiname}打开正常，子页签一共有{len(childnumber)}个物品")
                    else:
                        common.printred(f"{uiname}按钮不存在")
                    if i == 5:
                        poco("Close").click()
                        common.printgreen("个性展示功能测试正常")
            else:
                common.printred("个性展示打开失败")
                common.get_screen_shot(start, time.time(), devices, "个性展示打开失败")
            poco("Avatar").click()
            touch([1140, 540], times=2)
            if  poco("PersonalCareerBtn").exists(): # 个人生涯
                poco("PersonalCareerBtn").click()
                if poco("DebugDlg(Clone)").offspring("Close").exists():
                    poco("DebugDlg(Clone)").offspring("Close").click()
                time.sleep(3)
                if len(poco("PersonalCareer(Clone)").offspring("Tabs").child()) == 3:
                    common.printgreen("个人生涯界面存在3个按钮")
                    poco("Tabs").child("item0").click()
                    common.printgreen("角色名称是" + poco("Username").get_text())
                    poco("Tabs").child("item1").click()
                    time.sleep(3)
                    poco("Season").click()
                    poco("PKDetail").click()
                    if poco(text="挑战记录").exists():
                        common.printgreen("挑战记录界面打开成功")
                        poco(texture="l_close_00").click()
                    else:
                        common.printred("挑战记录界面打开失败")
                        common.get_screen_shot(start, time.time(), devices, "挑战记录界面打开失败")
                    poco("All").click() # 打开PVP信息全部比赛
                    if poco("Score").exists():
                        score = poco("Score").child("Value").get_text()
                        common.printgreen(f"全部比赛按钮点击正常，获取的当前评分是：{score}")
                    else:
                        common.printred("PVP信息全部比赛打开失败")
                        common.get_screen_shot(start, time.time(), devices, "PVP信息全部比赛打开失败")
                    time.sleep(3)
                    poco("Tabs").child("item2").click()
                    if poco("Season").exists():
                        uiname = poco("Level").get_text()
                        common.printgreen(f"当前的荣誉等级是{uiname}")
                        poco("Reward").click()
                        childnumber = poco("ScrollView").child()
                        if len(childnumber) >5:
                            common.printgreen("荣誉等级奖励的条目大于5个")
                            poco(texture="l_close_00").click()
                            poco("Close").click()
                        else:
                            common.printred("荣誉等级奖励的条目小于5个")
                            common.get_screen_shot(start, time.time(), devices, "荣誉等级奖励的条目小于5个")
                            poco(texture="l_close_00").click()
                            poco("Close").click()
                    else:
                        common.printred("荣誉奖杯界面打开失败")
                        common.get_screen_shot(start, time.time(), devices, "荣誉奖杯界面打开失败")
                else:
                    common.printred("个人生涯界面缺少按钮，具体见详图")
                    common.get_screen_shot(start, time.time(), devices, "个人生涯界面缺少按钮")
            else:
                common.printred("个人生涯按钮不存在")
                common.get_screen_shot(start, time.time(), devices, "个人生涯按钮不存在")
        else:
            common.printred("个人信息打开失败")
            common.get_screen_shot(start, time.time(), devices, "个人信息打开失败")
        poco("Avatar").click()
        common.settouch(1, 1140, 540, devices, times=2)
        if poco("SettingDlg(Clone)").exists():  # 判断设置界面是否打开
            if poco("OptionTab").exists():  # 系统设置
                poco("OptionTab").click()
                if poco("SettingPanel").exists():
                    poco("SettingDlg(Clone)").offspring("BtnMid").click()
                    common.printgreen("系统设置界面打开正常，设置画质未中")
                else:
                    common.printred("系统设置界面异常")
                    common.get_screen_shot(start, time.time(), devices, "系统设置界面异常")
            if poco("PushTab").exists():
                poco("PushTab").click()
                if poco("PushPanel").exists():
                    poco("SettingDlg(Clone)").offspring("Scroll1").offspring("item0").offspring("Checked").click()
                    common.printgreen("推送设置界面打开成功，操作每日领取体力的提醒")
            else:
                common.printred("推送设置界面异常")
                common.get_screen_shot(start, time.time(), devices, "推送设置界面异常")
            if poco("CameraTab").exists():
                poco("CameraTab").click()
                if poco("BattlePanel").exists():
                    poco("SettingDlg(Clone)").offspring("3DFree").child("Normal").click()
                    common.printgreen("视角设置界面打开成功，切换视角未3D自由视角")
            else:
                common.printred("视角设置界面异常")
                common.get_screen_shot(start, time.time(), devices, "视角设置界面异常")
            if poco("PasswordTab").exists():
                poco("PasswordTab").click()
                if poco("PasswordPanel").exists():
                    poco("SettingDlg(Clone)").offspring("Open").child("Selected").click()
                    if poco("SettingPanel").exists():
                        poco("TwoLevelPassword(Clone)").offspring("Close").click()
                        common.printgreen("二级密码界面打开成功,操作回收保护功能，界面打开关闭正常")
                        poco("SettingDlg(Clone)").child("Bg").child("Close").click()
            else:
                common.printred("二级密码界面异常")
                common.get_screen_shot(start, time.time(), devices, "二级密码界面异常")
                poco("SettingDlg(Clone)").child("Bg").child("Close").click()
    else:
        common.printred("设置界面打开失败！")
    if poco("Open").exists():  # GM小按钮存在
        poco("Avatar").click()
        poco("Close").click()
    return poco("Duck").get_name()  # 返回值


# devises = "127.0.0.1:62001"
# setting(devises)