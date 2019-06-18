"""
聊天 -- 每个聊天选项都进行聊天和发送表情，表情随机发送
聊天限制不做判断，反正一次跑不完，除非重复跑
"""

from multi_processframe.Tools import printcolor,adb_connect,screenshot
from airtest.core.api import *
import random
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
Androidpoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def chat(devices):
    poco = adb_connect.device(devices)
    poco("Back").click()  # 点击聊天功能
    sleep(1)
    chatlist = [1,2,3,4,10,14]
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    for tab in chatlist:
        tab1 = "tab" + str(tab)
        printcolor.printgreen("检查点 "+freeze_poco("ChatNewDlg_ani").offspring(tab1).offspring("Bg").child("name").get_text()+" 聊天选项 显示正确")
        poco("ChatNewDlg_ani").offspring(tab1).offspring("Bg").child("name").click()
        if poco("chattext").exists():
            printcolor.printgreen("点击输入框")
            poco("chattext").click()  # 点击输入框
            text("聊五毛钱的天。。。")
            Androidpoco("android.widget.Button").click()
            poco("sendchat").click()  # 点击发送
            if poco("addBtn").exists():
                poco("addBtn").click()  # 表情
                sleep(1)
                item1 = "item" + str(random.randint(0, 23))
                poco(item1).child("template").click()
                poco("sendchat").click()  # 点击发送
                sleep(2)
        else:
            printcolor.printgreen("当前聊天选项没有输入选项")
    return poco("ChatNewDlg_ani").offspring("tab4").offspring("Selected").child("name").get_text()
