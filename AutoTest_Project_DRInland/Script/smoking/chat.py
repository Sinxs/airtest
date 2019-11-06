"""
聊天 -- 每个聊天选项都进行聊天和发送表情，表情随机发送
聊天限制不做判断，反正一次跑不完，除非重复跑
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from multi_processframe.ProjectTools import common
from airtest.core.api import *
import random


def chat(start, devices):
    poco = common.deviceconnect(devices)
    poco("Back").click()  # 点击聊天功能
    sleep(1)
    # todo：每次都全部测试
    # chatlist = [1, 2, 3, 4, 10, 14]
    # todo：测试全部
    chatlist = [1, 2, 3]
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    for tab in chatlist:
        tab1 = "tab" + str(tab)
        if not freeze_poco("ChatNewDlg_ani").offspring(tab1).offspring("Bg").child("name").exists():
            common.printred("tab2  不存在，大概率是没有加入公会，所以没有公会聊天选项，请加入工会后再次运行本脚本")
            continue
        if freeze_poco("ChatNewDlg_ani").offspring(tab1).offspring("Bg").child("name").exists():
            common.printgreen("检查点 " + freeze_poco("ChatNewDlg_ani").offspring(tab1).offspring("Bg")
                              .child("name").get_text() + " 聊天选项 显示正确")
            # 重置表情框
            if poco("ChatEmotion").exists():
                poco("addBtn").click()
                sleep(1.5)
            # 点击大选项
            poco("ChatNewDlg_ani").offspring(tab1).offspring("Bg").child("name").click()
            if poco("chattext").exists():
                poco("textinput").wait().set_text("聊五毛钱的天。。。")
                poco("sendchat").click()  # 点击发送
                if poco("Cancel").exists():  # 没有聊天次数了，聊天功能到此为止
                    common.printred("没有聊天次数了，系统聊天功能今天测试不了，除非买次数")
                    poco("Cancel").click()  # 点击不在补充蓝鸟道具
                    continue
                if poco("addBtn").exists():
                    poco("addBtn").click()  # 表情
                    if not poco("ChatEmotion").exists():
                        poco("addBtn").click()
                    sleep(1)
                    item1 = "item" + str(random.randint(0, 23))
                    if poco(item1).exists():
                        poco(item1).click()
                        poco("sendchat").click()  # 点击发送
                        sleep(2)
                        if poco("Cancel").exists():  # 没有聊天次数了，聊天功能到此为止
                            common.printred("没有聊天次数了，系统聊天功能今天测试不了，除非买次数")
                            poco("Cancel").click()  # 点击不在补充蓝鸟道具
                            continue
                    else:
                        common.printred("表情界面没有出现，请检查...")
                        common.get_screen_shot(start, time.time(), devices, "表情界面没有出现")
            else:
                common.printgreen(freeze_poco("ChatNewDlg_ani").offspring(tab1).offspring("Bg")
                                  .child("name").get_text() + "  选项没有输入选项")
                common.get_screen_shot(start, time.time(), devices, "选项没有输入选项")
        else:
            common.printred(f"检查点  聊天选项 {tab1} 不存在，检查一下.一个大选项,大概率是因为没有加工会造成")
            common.get_screen_shot(start, time.time(), devices, "聊天选项控件缺失")
    return poco("ChatNewDlg_ani").offspring("tab4").offspring("Selected").child("name").get_text()  # 系 统


if __name__ == "__main__":
    start = time.localtime()
    chat(start, "e37c0280")