"""
登陆奖励
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from multi_processframe.ProjectTools import common

def loginreward(start, devices):
    poco = common.deviceconnect(devices)
    if poco("SysISevenActivity").exists():
        poco("SysISevenActivity").click()  # 点击登陆奖励按钮
        if poco(texture="SevenReward_Title").exists():
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for WrapItem_ in range(len(freeze_poco("ScrollView").child())):
                WrapItem = "WrapItem_" + str(WrapItem_)
                if freeze_poco(WrapItem).exists() and freeze_poco("Texture").exists():
                    pass
                else:
                    common.printred("登陆奖励缺少元素，请检查。。。")
                    common.get_screen_shot(start, time.time(), devices, "登陆奖励缺少元素")
            # todo:以下代码是做领取操作的，因为领完了这个按钮就没了，所以不做领取操作
            # if poco("SevenAwardDlg(Clone)").offspring("GetButton").offspring(text="领 取").exists():
            #     for Label in poco("SevenAwardDlg(Clone)").offspring("GetButton").offspring(text="领 取"):
            #         Label.click()
            #         for i in range(10):
            #             if poco(text="使用").wait().exists():
            #                 poco(text="使用").wait().click()
            #             else:
            #                 break
            #     if not poco("SevenAwardDlg(Clone)").offspring("WrapItem_6").offspring(text="领 取").exists():
            #         common.printgreen("已经全部领取")
            # else:
            #     common.printgreen("没有可领取的奖励")
        else:
            common.printred("没有弹出登陆奖励，请检查。。。")
            common.get_screen_shot(start, time.time(), devices, "主界面没有登陆奖励按钮")
    else:
        common.printred("主界面没有登陆奖励按钮，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "主界面没有登陆奖励按钮")
    if poco(texture="SevenReward_Title").exists():
        return poco(texture="SevenReward_Title").get_name()  # Title
    # TODO：说明一下，如果主界面没有登陆奖励按钮，那么报告给一个失败的提示，因为不确定是因为领完了消失还是BUG的原因
    else:
        return poco("Alphaboard").offspring("SysA_Friends").child("Name").get_text()  # 社交


if __name__ == "__main__":
    start = time.localtime()
    loginreward(start, "e37c0280")