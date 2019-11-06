"""
奖励模块
"""
# -*- encoding=utf8 -*-
__author__ = "Lee.li"

from multi_processframe.ProjectTools.common import *
from airtest.core.api import *


# 福利模块

def reward(start, devices):
    poco = deviceconnect(devices)
    if poco("SysEReward").exists():
        poco("SysEReward").click()
        print("测试奖励模块")
        with poco.freeze() as freezepoco:
            count = freezepoco("RewardDlg(Clone)").child("Bg").child("Tabs").offspring("SelectedTextLabel")
            print(f"奖励中一共有{len(count)}个模块，分别为：")
            number = 1
            for x in count:
                item = x.parent().parent().get_name()
                uiname = freezepoco("RewardDlg(Clone)").child("Bg").child("Tabs").child(item).offspring("SelectedTextLabel").get_text()
                printgreen(f"{number}.{uiname}")
                number += 1
            for i in count:
                item = i.parent().parent().get_name()
                uiname = freezepoco("RewardDlg(Clone)").child("Bg").child("Tabs").child(item).offspring("SelectedTextLabel").get_text()
                if uiname == "成就奖励":
                    design_achieve(start, poco,item,devices)
                elif uiname == "等级奖励":
                    level_reward(start, poco,item,devices)
                elif uiname == "目标奖励":
                    reward_target(start, poco,item,devices)
                elif uiname == "战力奖励":
                    server_activity(start, poco,item,devices)
                elif uiname == "分享奖励":
                    share_reward(start, poco,item,devices)
                elif uiname == "龙穴助战":
                    reward_dragon(start, poco,item,devices)
    else:
        printred("主界面没有找到奖励模块")
        get_screen_shot(start, time.time(), devices, "主界面没有找到奖励模块，请详细查看")
    return poco("XSys_Reward_Dragon").get_name() # 返回主界面上的按钮


def design_achieve(start, poco,item,devices): # 成就奖励
    poco("XSys_Design_Achieve").click()
    try:
        with poco.freeze() as freezepoco:
            count = freezepoco("padTabs").child()
            for i in range(len(count)):
                TabTpl = "TabTpl" + str(i)
                freezepoco("padTabs").child(TabTpl).click()
        printgreen("成就界面按钮点击正常")
    except Exception as e:
        printred("成就界面按钮点击异常")
        printred(e)
        get_screen_shot(start, time.time(), devices, "成就界面按钮点击异常")


def level_reward(start, poco,item,devices): # 等级奖励
    poco("XSys_LevelReward").click()
    with poco.freeze() as freezepoco:
        if freezepoco("Panel").exists() and \
                freezepoco("T1").exists() and \
                freezepoco("T3").exists() and \
                freezepoco("T4").exists() and \
                freezepoco("Panel").offspring("Name").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("Panel").offspring("Fetch").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("Panel").offspring("ItemReward").exists():
            printgreen("等级奖励界面UI元素显示正常")
        else:
            printred("等级奖励界面缺少UI元素，详情见截图")
            get_screen_shot(start, time.time(), devices, "等级奖励界面缺少UI元素")


def reward_target(start, poco,item,devices): # 目标奖励
    poco("XSys_Reward_Target").click()
    try:
        with poco.freeze() as freezepoco:
            count = freezepoco("padTabs").child("TabList").child()
            for i in range(len(count)):
                if i == 2:
                    TabTpl = "TabTpl3"
                else:
                    TabTpl = "TabTpl" + str(i)
                freezepoco("padTabs").child("TabList").child(TabTpl).click()
        printgreen("目标奖励界面按钮点击正常")
    except Exception as e:
        printred("目标奖励界面按钮点击异常")
        printred(e)
        get_screen_shot(start, time.time(), devices, "目标奖励界面按钮点击异常")


def server_activity(start, poco,item,devices): # 战力奖励
    poco("XSys_ServerActivity").click()
    pass


def share_reward(start, poco,item,devices): # 分享奖励
    poco("XSys_WeekShareReward").click()
    with poco.freeze() as freezepoco:
        if freezepoco("item0").exists() and \
                freezepoco("BtnShare").exists() and \
                freezepoco("Label").exists() and \
                freezepoco("WeekDesc").exists() and \
                freezepoco("ActivityDes").exists():
            printgreen("分享奖励界面UI元素显示正常")
        else:
            printred("分享奖励界面缺少UI元素，详情见截图")
            get_screen_shot(start, time.time(), devices, "分享奖励界面缺少UI元素")


def reward_dragon(start, poco,item,devices): # 分享奖励
    poco("XSys_Reward_Dragon").click()
    with poco.freeze() as freezepoco:
        if freezepoco(texture="l_frame_02").exists() and \
                freezepoco(text="本周助战次数：").exists() and \
                freezepoco("Time").exists() and \
                freezepoco("Agreement").exists() and \
                freezepoco("Category").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item0").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item1").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item2").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item0").child("tmp2").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item1").child("tmp2").exists() and \
                freezepoco("tmp1").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item1").child("Get").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item2").child("Get").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item0").child("Get").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item0").child("Icon").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item1").child("Icon").exists() and \
                freezepoco("RewardDlg(Clone)").offspring("item2").child("Icon").exists():
            printgreen("龙穴助战界面UI元素显示正常")
        else:
            printred("龙穴助战界面缺少UI元素，详情见截图")
            get_screen_shot(start, time.time(), devices, "龙穴助战界面缺少UI元素")


if __name__ == "__main__":
    start = time.localtime()
    reward(start, "9b57691d")