from multi_processframe.Tools import printcolor,adb_connect,screenshot
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
Androidpoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

devices = "127.0.0.1:62025"

def honor(devices):
    poco = adb_connect.device(devices)
    if poco("SysAItem").exists():
        if poco("SysAItem").get_position()[1] > 1:  # 界面有角色按钮
            poco(texture="halln_4").click()
        poco("SysAItem").click()  # 点击角色按钮
    else:
        printcolor.printgreen("主界面没有角色按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    if poco("XSys_Item_Equip").exists():
        poco("XSys_Item_Equip").click()  # 点装备按钮
        if poco("ShowTitle").exists():
            poco("ShowTitle").click()  # 点击头衔按钮
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if freeze_poco("TitleDlg(Clone)").offspring("Title").exists():
                printcolor.printgreen("进入头衔晋升界面")
                printcolor.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Title").get_text() + " 显示正确")
                printcolor.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current").offspring("FightLabel").get_text() + " 显示正确")
                printcolor.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current").offspring("item0").child("Label").get_text() + " 显示正确")
                printcolor.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current").offspring("item1").child("Label").get_text() + " 显示正确")
                if poco("TitleDlg(Clone)").offspring("RedPoint").exists():  # 如果有可以晋升的头衔，就点击晋升，但是只点击一次
                    printcolor.printgreen("有可以晋升的选项，点击晋升....")
                    poco("Promote").click()  # 点击晋升
                    sleep(6)
                    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                    printcolor.printgreen("进入头衔晋升界面")
                    printcolor.printgreen("检查点 " + freeze_poco("TitleShareDlg(Clone)").child("Bg").child("Title").get_text() + " 显示正确")
                    printcolor.printgreen("检查点 " + freeze_poco("Message").get_text() + " 显示正确")
                    if poco("KeepOn").exists():
                        printcolor.printgreen("点击屏幕继续...")
                        poco("KeepOn").click()  # 点击屏幕继续
                        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                        if freeze_poco("TitleDlg(Clone)").offspring("Title").exists():
                            printcolor.printgreen("进入头衔晋升界面")
                            printcolor.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Title").get_text() + " 显示正确")
                            printcolor.printgreen( "检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current").offspring("FightLabel"))
                            printcolor.printgreen("检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current").offspring("item0").child("Label").get_text() + " 显示正确")
                            printcolor.printgreen( "检查点 " + freeze_poco("TitleDlg(Clone)").offspring("Current").offspring("item1").child("Label").get_text() + " 显示正确")
                        else:
                            printcolor.printred("没有返回晋升界面，请检查...")
                            screenshot.get_screen_shot(time.time(), devices, "没有返回晋升界面")
                else:
                    printcolor.printgreen("没有可以晋升的选项，无法晋升")
                # todo：接下来判断没有晋升选项的状态，如果没有晋升，就给出提示直接跳过，进入下一个状态的判断，剩下是的合成勋章的判断


        else:
            printcolor.printred("没有进入装备界面，请检查...")
            screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    else:
        printcolor.printred("没有进入装备界面，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
