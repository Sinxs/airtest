# -*- encoding=utf8 -*-
__author__ = "Lee.li"

# 系统设置
# 推送设置
# 视角设置
# 个人信息	个性展示-连击框

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.Tools import screenshot, printcolor, adb_connect
import traceback

def setting(devices):
    poco = adb_connect.device(devices)
    poco("Avatar").click()
    touch([1140, 540], times=2)
    if poco("SettingDlg(Clone)").exists(): # 打开设置
        uiname = poco("SettingDlg(Clone)").offspring("Bg").offspring("Bg1").child("T").get_text()
        printcolor.printgreen(f"{uiname}  界面打开成功")
        if poco("PrerogativeBtn").exists(): # 个人信息
            poco("PrerogativeBtn").click()
            if poco("PrerogativeFrame(Clone)").offspring("Bg").child("Bg1").exists(): # 个性展示
                uiname = poco("PrerogativeFrame(Clone)").offspring("Bg").offspring("Bg1").child("T").get_text()
                printcolor.printgreen(f"{uiname}  界面打开成功")
                if poco("RuleBtn").exists(): # 规则详情
                    poco("RuleBtn").click()
                    if poco("CommonHelpTip(Clone)").exists(): # 个性显示规则
                        uiname = poco("CommonHelpTip(Clone)").child("Title").get_text()
                        printcolor.printgreen(f"{uiname}  界面打开成功")
                        poco("CommonHelpTip(Clone)").child("Btn").click()
                        if not poco("CommonHelpTip(Clone)").exists():
                            printcolor.printgreen("规则详情界面关闭正常")
                        else:
                            printcolor.printred("规则详情界面关闭异常")
                            screenshot.get_screen_shot(time.time(), devices, "规则详情界面关闭异常")
                    else:
                        printcolor.printred("个性显示规则界面打开失败")
                        screenshot.get_screen_shot(time.time(), devices, "个性显示规则界面打开失败")
                else:
                    printcolor.printred("规则详情打开异常")
                    screenshot.get_screen_shot(time.time(), devices, "规则详情打开异常")
                if poco("ShopBtn").exists(): # 个性商店
                    poco("ShopBtn").click()
                    uiname = poco("ShopName").get_text()
                    printcolor.printgreen(f"{uiname}  界面打开成功")
                    poco("Close").click()
                    if poco("PrerogativeFrame(Clone)").offspring("Bg").child("Bg1").exists():
                        printcolor.printgreen("个性商店关闭正常")
                    else:
                        printcolor.printred("个性商店关闭异常")
                        screenshot.get_screen_shot(time.time(), devices, "个性商店关闭异常")
                else:
                    printcolor.printred("个性商店打开失败")
                    screenshot.get_screen_shot(time.time(), devices, "个性商店打开失败")
                for i in range(6):
                    if i == 4:
                        swipe((335, 567), (335, 260))
                        for a in range(20):
                            if poco("PrerogativeFrame(Clone)").offspring("PreList").offspring("item4").get_position()[1] > 0.9:
                                swipe((335, 567), (335, 260))
                            else:
                                break
                    item = f"item{i}"
                    if poco("PrerogativeFrame(Clone)").offspring("PreList").offspring(item).exists():
                        poco("PrerogativeFrame(Clone)").offspring("PreList").offspring(item).click()
                        uiname = poco("PrerogativeFrame(Clone)").offspring("PreList").offspring(item).child("Text").get_text()
                        childuiname = poco("TLabel").get_text()
                        childnumber = poco("PrerogativeFrame(Clone)").offspring("WrapContent").child()
                        if len(childnumber) <1:
                            printcolor.printred(f"{uiname}的物品数量异常，请查看具体情况")
                        else:
                            printcolor.printgreen(f"按钮{uiname}打开正常，table页签{childuiname}打开正常，子页签一共有{len(childnumber)}个物品")
                    else:
                        printcolor.printred(f"{uiname}按钮不存在")
                    if i == 5:
                        poco("Close").click()
                        printcolor.printgreen("个性展示功能测试正常")
            else:
                printcolor.printred("个性展示打开失败")
                screenshot.get_screen_shot(time.time(), devices, "个性展示打开失败")
            poco("Avatar").click()
            touch([1140, 540], times=2)
            if  poco("PersonalCareerBtn").exists():
                poco("PersonalCareerBtn").click()
                time.sleep(3)
                if len(poco("PersonalCareer(Clone)").offspring("Tabs").child()) == 3:
                    printcolor.printgreen("个人生涯界面存在3个按钮")
                    poco("Tabs").child("item0").click()
                    printcolor.printgreen("角色名称是"+poco("Username").get_text())
                    poco("Tabs").child("item1").click()
                    time.sleep(3)
                    poco("PKDetail").click()
                    if poco(text="挑战记录").exists():
                        printcolor.printgreen("挑战记录界面打开成功")
                        poco(texture="l_close_00").click()
                    else:
                        printcolor.printred("挑战记录界面打开失败")
                        screenshot.get_screen_shot(time.time(), devices, "挑战记录界面打开失败")
                    poco("All").click() # 打开PVP信息全部比赛
                    if poco("Score").exists():
                        score = poco("Score").child("Value").get_text()
                        printcolor.printgreen(f"全部比赛按钮点击正常，获取的当前评分是：{score}")
                    else:
                        printcolor.printred("PVP信息全部比赛打开失败")
                        screenshot.get_screen_shot(time.time(), devices, "PVP信息全部比赛打开失败")
                    time.sleep(3)
                    poco("Tabs").child("item2").click()
                    if poco("Season").exists():
                        uiname = poco("Level").get_text()
                        printcolor.printgreen(f"当前的荣誉等级是{uiname}")
                        poco("Reward").click()
                        childnumber = poco("ScrollView").child()
                        if len(childnumber) >5:
                            printcolor.printgreen("荣誉等级奖励的条目大于5个")
                            poco(texture="l_close_00")
                        else:
                            printcolor.printred("荣誉等级奖励的条目小于5个")
                            screenshot.get_screen_shot(time.time(), devices, "荣誉等级奖励的条目小于5个")
                            poco(texture="l_close_00")
                    else:
                        printcolor.printred("荣誉奖杯界面打开失败")
                        screenshot.get_screen_shot(time.time(), devices, "荣誉奖杯界面打开失败")
                else:
                    printcolor.printred("个人生涯界面缺少按钮，具体见详图")
                    screenshot.get_screen_shot(time.time(), devices, "个人生涯界面缺少按钮")
            else:
                printcolor.printred("个人生涯按钮不存在")
                screenshot.get_screen_shot(time.time(), devices, "个人生涯按钮不存在")
        else:
            printcolor.printred("个人信息打开失败")
            screenshot.get_screen_shot(time.time(), devices, "个人信息打开失败")
        # if poco("OptionTab").exists():
        #     poco("OptionTab").click()
        #     printcolor.printgreen("系统设置界面打开成功")
        # if poco("PushTab").exists():
        #     poco("PushTab").click()
        #     printcolor.printgreen("推送设置界面打开成功")
        # if poco("CameraTab").exists():
        #     poco("CameraTab").click()
        #     printcolor.printgreen("视角设置界面打开成功")
        # if poco("PasswordTab").exists():
        #     poco("PasswordTab").click()
        #     printcolor.printgreen("二级密码界面打开成功")

    else:
        printcolor.printred("设置界面打开失败！")





# devices = "127.0.0.1:62001"
# setting(devices)