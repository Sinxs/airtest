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
    else:
        printcolor.printred("设置界面打开失败！")
    poco("OptionTab")
    poco("PushTab")
    poco("CameraTab")
    poco("PasswordTab")

devices = "127.0.0.1:62001"
setting(devices)