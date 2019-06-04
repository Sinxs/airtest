from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
Androidpoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
devicces = "127.0.0.1:62001"
"""
使用方式
0、把以上 devices 后面的设备名改成自己的，没错，就是离介绍上面最近的哪一行代码
1、手动创建一个账号
2、进入角色选择界面
3、运行当前脚本 establish_account 模块
4、如果中途报错，就把游戏放到初始界面，运行establish_account2 模块
"""

def establish_account1(poco):
    if poco("Overlay").exists():
        poco("Overlay").click()
        sleep(3)
        poco("Skip").click()

    else:
        print("没找到跳过直接跑吧....")
    if poco(text="点击屏幕继续").exists():
        poco(text="点击屏幕继续").click()
    if poco("Pause").child("p")[1].exists():
        poco("Pause").child("p")[1].click()
        poco(text="退出副本").click()
        sleep(30)
    if poco("Avatar").exists():
        poco("Avatar").click()
        text("god")
        Androidpoco("android.widget.Button").click()
        sleep(9)
        poco("SettingDlg(Clone)").offspring("Close").click()
        for i in range(5):
            if poco("Close").exists():
                poco("Close").click()
            else:
                break
        poco("Open").click()

        sleep(3)

        poco(text=">").click()
        text("level 130")
        Androidpoco("android.widget.Button").click()
        sleep(8)

        poco(text=">").click()
        text("item 42 1000")
        Androidpoco("android.widget.Button").click()
        sleep(3)

        poco(text=">").click()
        text("item 9999 1")
        Androidpoco("android.widget.Button").click()

        poco(text=">").click()
        text("item 9998 1")
        Androidpoco("android.widget.Button").click()
        poco("Close").click()  # GM指令搞定
        #  装在GM装备
    poco("SysAItem").click()
    if poco("equip9999").exists():
        poco("equip9999").click()
        poco("EquipToolTipDlg(Clone)").child("Bg").offspring("Button1").child("Label").click()
    if poco("equip9998").exists():
        poco("equip9998").click()
        poco("EquipToolTipDlg(Clone)").child("Bg").offspring("Button1").child("Label").click()

    poco("Close").click()
    poco("Avatar").click()
    poco(text="切换角色").click()
    sleep(20)


def establish_account(devicces):
    dev = connect_device("android:///" + devicces)
    poco = UnityPoco(device=dev)
    for i in range(4, 8):
        poco(f"Prof{i}").click()
        sleep(2)
        if poco("EnterGame").exists():
            poco("EnterGame").click()
            if poco(text="[fece00]角色名字长度不合法，或含有非法字符").exists():
                poco("Random").click()
                if poco("EnterGame").exists():
                    poco("EnterGame").click()
            sleep(45)
            establish_account1(poco)


# establish_account(devicces)


def establish_account2(devicces):
    dev = connect_device("android:///" + devicces)
    poco = UnityPoco(device=dev)
    if poco("Overlay").exists():
        poco("Overlay").click()
        sleep(3)
        poco("Skip").click()

    else:
        print("没找到跳过直接跑吧....")
    if poco(text="点击屏幕继续").exists():
        poco(text="点击屏幕继续").click()
    if poco("Pause").child("p")[1].exists():
        poco("Pause").child("p")[1].click()
        poco(text="退出副本").click()
        sleep(30)
    if poco("Avatar").exists():
        poco("Avatar").click()
        text("god")
        Androidpoco("android.widget.Button").click()
        sleep(9)
        poco("SettingDlg(Clone)").offspring("Close").click()
        for i in range(5):
            if poco("Close").exists():
                poco("Close").click()
            else:
                break
        poco("Open").click()

        sleep(3)

        poco(text=">").click()
        text("level 130")
        Androidpoco("android.widget.Button").click()
        sleep(8)

        poco(text=">").click()
        text("item 42 1000")
        Androidpoco("android.widget.Button").click()
        sleep(3)

        poco(text=">").click()
        text("item 9999 1")
        Androidpoco("android.widget.Button").click()

        poco(text=">").click()
        text("item 9998 1")
        Androidpoco("android.widget.Button").click()
        poco("Close").click()  # GM指令搞定
        #  装在GM装备
    poco("SysAItem").click()
    if poco("equip9999").exists():
        poco("equip9999").click()
        poco("EquipToolTipDlg(Clone)").child("Bg").offspring("Button1").child("Label").click()
    if poco("equip9998").exists():
        poco("equip9998").click()
        poco("EquipToolTipDlg(Clone)").child("Bg").offspring("Button1").child("Label").click()

    poco("Close").click()
    poco("Avatar").click()
    poco(text="切换角色").click()


establish_account2(devicces)


