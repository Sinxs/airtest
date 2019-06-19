"""
队伍模块-
脚本环境

"""

from airtest.core.api import *
from multi_processframe.Tools import screenshot, printcolor, adb_connect
devices = "127.0.0.1:62025"
def troops(devices):
    poco = adb_connect.device(devices)
    if poco("Team").exists():  # 队伍按钮
        if poco("Team").get_position()[0]<0:
            poco("TaskSwitchBtn").click()
        poco("BottomLeft").click()  # 点击队伍按钮
    else:
        printcolor.printgreen("主界面没有队伍按钮，请检查")
        screenshot.get_screen_shot(time.time(), devices, "没有钓鱼按钮")
    poco("BtnCreate").click()  # 点击创建队伍
    if poco("Title").exists():
        printcolor.printgreen("进入队伍界面，开始判断队伍界面元素。。。")
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("P (1)").exists() and freeze_poco("BtnRefresh").exists() and freeze_poco("BtnTeamRoom").exists() and \
                freeze_poco("BtnCreate").exists() and freeze_poco("BtnMatch").exists():
            printcolor.printgreen("队伍界面控件显示正确，\n开始点击刷新按钮")
            poco("BtnRefresh").click()  # 点击刷新按钮
            printcolor.printgreen("点击刷新按钮，但是因为没有队伍，所以实际上没有任何作用，点着玩吧。。。\n开始点击大厅按钮")
            poco("BtnTeamRoom").click()  # 点击大厅按钮
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if freeze_poco(texture="l_tip_00").exists() and freeze_poco("Title1").exists() and \
                    freeze_poco("Title2").exists() and freeze_poco("Title3").exists() and \
                    freeze_poco("Title4").exists() and freeze_poco("Title5").exists():
                printcolor.printgreen("进入大厅成功")
                for item in range(1, len(freeze_poco("ScrollView").child())):
                    item1 = "item"+str(item)
                    if freeze_poco("TeamListDlg(Clone)").offspring(item1).exists():
                        printcolor.printgreen("检查点 "+freeze_poco("TeamListDlg(Clone)").offspring(item1).child("Text").get_text()+" 显示正确")
                poco("Close").click()  # 点击返回
                for x in range(4):  # 回到主界面
                    if poco("Close").exists():
                        poco("Close").click()
                    else:
                        break
                printcolor.printgreen("返回主界面\n开始进行")
            else:
                printcolor.printred("进入大厅失败，请检查")
                screenshot.get_screen_shot(time.time(), devices, "进入大厅失败")
    else:
        printcolor.printred("点击队伍按钮后没有进入队伍界面，请检查。。。")
        screenshot.get_screen_shot(time.time(), devices, "点击队伍按钮后没有进入队伍界面")
    if poco("BtnJoin").exists():
        poco("BtnJoin").click()
    else:
        printcolor.printgreen("主界面没有队伍按钮")
