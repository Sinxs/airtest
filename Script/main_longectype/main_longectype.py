from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

devices = "127.0.0.1:62001"

def addlongectype(poco):
    """
    :return: GM add 远征次数
    """
    if poco("Open").exists():  # 判断有没有GM按钮，如果有直接点击输入增加次数
        poco("Open").click()
        poco("DebugDlg(Clone)").offspring("P").click()
        text("resetcount 3001")
        poco(texture="switch").click()
        poco("Open").click()
    else:  # 否则先打开GM框，在点击输入增加次数
        poco("Avatar").click()
        text("resetcount 3001")
        poco(texture="switch").click()
        poco("SettingDlg(Clone)").offspring("Close").click()
        poco("Open").click()

def longectype(poco):
    if poco("P").exists():
        poco("P").click()
    else:
        print("当前界面没有日常按钮，请检查。。。")
    item = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item50").offspring("Label")
    if poco(f"{item}").exists():
        for ii in range(10):
            pos = poco(f"{item}").get_position()
            if pos[1] < 0.14:
                swipe([1060, 723], [1060, 450], 5)
            else:
                break
        for ii in range(10):
            pos = poco(f"{item}").get_position()
            if pos[1] > 0.78:
                swipe([1060, 450], [1060, 723], 5)
                break
        poco(f"{item}").click()

def start(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)  # 链接设备，并且重置 poco
    # addlongectype(poco)  # 增加副本次数
    longectype(poco)

start(devices)


