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

    if poco("SettingDlg(Clone)").exists():
        uiname = poco("SettingDlg(Clone)").offspring("Bg").offspring("Bg1").child("T").get_text()
        printcolor.printgreen(f"{uiname}  界面打开成功")
        if poco("PrerogativeBtn").exists():
            poco("PrerogativeBtn").click()
            if poco("PrerogativeFrame(Clone)").offspring("Bg").child("Bg1").exists():
                uiname = poco("PrerogativeFrame(Clone)").offspring("Bg").offspring("Bg1").child("T").get_text()
                printcolor.printgreen(f"{uiname}  界面打开成功")
            else:
                printcolor.printred("个性展示打开失败")
                screenshot.get_screen_shot(time.time(), devices, "个性战士打开失败")

        else:
            printcolor.printred("个性信息打开失败")
            screenshot.get_screen_shot(time.time(), devices, "个性战士打开失败")






        if poco("OptionTab").exists():
            poco("OptionTab").click()
            printcolor.printgreen("系统设置界面打开成功")
        if poco("PushTab").exists():
            poco("PushTab").click()
            printcolor.printgreen("推送设置界面打开成功")
        if poco("CameraTab").exists():
            poco("CameraTab").click()
            printcolor.printgreen("视角设置界面打开成功")
        if poco("PasswordTab").exists():
            poco("PasswordTab").click()
            printcolor.printgreen("二级密码界面打开成功")
    else:
        printcolor.printred("设置界面打开失败！")



#
#
# devices = "127.0.0.1:62001"
# setting(devices)