"""
公会模块
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"

from airtest.core.api import *
from multi_processframe.ProjectTools import common
import random


def guild(start, devices):
    poco = common.deviceconnect(devices)
    guildbutlist = ["BtnSignIn", "BtnGz", "BtnRanking", "BtnRed", "BtnMall", "BtnJoker", "GuildTreasureIcon"]
    if poco("SysCGuild").exists():
        poco("SysCGuild").click()  # 点击主界面公会按钮
        if poco("Create").exists():  # 创建公会
            poco("Create").click()
            if poco("GuildListDlg(Clone)").offspring("CreateMenu").child("T")[0].exists():
                poco("NameInput").set_text(f"{random.randint(100000,99999999)}")  # 输入公会名称
                poco("Highlight").click()  # 点击创建公会
        common.printgreen("进入" + poco(texture="tybg_h2Split").child("T").get_text())
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("NewGuildHall(Clone)").offspring("NewGuildHallDlg").child("Bg").exists() and \
            freeze_poco("GuildName").exists() and \
            freeze_poco("Btnpositions").exists() and \
            freeze_poco("NewGuildHall(Clone)").offspring("item0").exists() and \
            freeze_poco("NewGuildHall(Clone)").offspring("item1").exists() and \
            freeze_poco("NewGuildHall(Clone)").offspring("item2").exists() and \
            freeze_poco("NewGuildHall(Clone)").offspring("item3").exists() and \
            freeze_poco("Btninto").exists() and \
            freeze_poco(texture="Chat_icon_4").exists() and \
            freeze_poco("BtnGz").exists() and \
            freeze_poco("BtnRed").exists() and \
            freeze_poco("BtnMall").exists() and \
            freeze_poco("BtnJoker").exists() and \
            freeze_poco("GuildTreasureIcon").exists():
        for guildbut in guildbutlist:
            if poco(guildbut).exists():
                poco(guildbut).click()
                if guildbut == "BtnSignIn":
                    BtnSignIn(start, poco, devices)  # 签到
                if guildbut == "BtnGz":
                    BtnGz(start, poco, devices)  # 工资
                if guildbut == "BtnRanking":
                    BtnRanking(start, poco, devices)  # 排行
                if guildbut == "BtnSkill":
                    BtnSkill(start, poco, devices)  # 技能
                if guildbut == "BtnRed":
                    BtnRed(start, poco, devices)  # 红包
                if guildbut == "Donation":
                    Donation(start, poco, devices)  # 捐赠
                if guildbut == "BtnMall":
                    BtnMall(poco, devices)  # 商店
                if guildbut == "BtnJoker":
                    BtnJoker(start, poco, devices)  # 小丑扑克
                if guildbut == "Btnfish":
                    Btnfish(start, poco, devices)  # 钓鱼
                if guildbut == "BtnBuild":
                    BtnBuild(start, poco, devices)  # 建造
                if guildbut == "BtnConsider":
                    BtnConsider(start, poco, devices)  # 研究
                if guildbut == "GuildTreasureIcon":  # 宝藏
                    common.printgreen("进入宝藏界面")
                    freeze_poco = poco.freeze()  # TODO：定义冻结poco
                    if freeze_poco("Title").exists() and \
                        freeze_poco("GuildTreasureDlg(Clone)").offspring("item0").exists() and \
                        freeze_poco("GuildTreasureDlg(Clone)").offspring("item1").exists() and \
                        freeze_poco("GuildTreasureDlg(Clone)").offspring("item2").exists():
                        pass
                    else:
                        common.printred("公会宝藏界面缺少控件，请检查")
                        common.get_screen_shot(start, time.time(), devices, "公会宝藏界面缺少控件")
                    close(poco)
    else:
        common.printred("公会界面缺少控件，请检查")
        common.get_screen_shot(start, time.time(), devices, "公会界面缺少控件")
    if poco("NewGuildHall(Clone)").offspring("item1").exists():
        common.printgreen("进入内政界面")
        poco("NewGuildHall(Clone)").offspring("item1").click()  # 点击内政
        if poco("NewGuildHall(Clone)").offspring("NewGuildInterior").offspring("item0").child("GO").exists():
            BtnSkill(start, poco, devices)  # 技能
        if poco("NewGuildHall(Clone)").offspring("NewGuildInterior").offspring("item1").child("GO").exists():
            BtnBuild(start, poco, devices)  # 建造
        if poco("NewGuildHall(Clone)").offspring("NewGuildInterior").offspring("item2").child("GO").exists():
            Donation(start, poco, devices)  # 捐赠
        if poco("NewGuildHall(Clone)").offspring("NewGuildInterior").offspring("item3").child("GO").exists():
            PlayerBg(start, poco, devices)
        if poco("NewGuildHall(Clone)").offspring("NewGuildInterior").offspring("item4").child("GO").exists():
            BtnConsider(start, poco, devices)  # 研究
    if poco("NewGuildHall(Clone)").offspring("item2").exists():
        poco("NewGuildHall(Clone)").offspring("item2").click()  # 点击活动
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        for item in range(len(freeze_poco("Panel").child())-2):
            if freeze_poco("NewGuildHall(Clone)").offspring("NewGuildLeisureTime").\
                    offspring("Panel").child(f"item{str(item)}").exists():
                pass
            else:
                print("工会活动界面缺少控件，请检查")
                common.get_screen_shot(start, time.time(), devices, "工会活动界面缺少控件")
    if poco("NewGuildHall(Clone)").offspring("item3").exists():
        poco("NewGuildHall(Clone)").offspring("item3").click()  # 点击福利
        for item in range(len(poco("WrapContent").child()) - 1):
            # 福利点击前往
            poco("NewGuildHall(Clone)").offspring("NewGuildWelfare").offspring(f"item{str(item)}").child("GO").click()
            if item == 0:
                BtnMall(poco, devices)  # 商店
            if item == 1:
                BtnGz(start, poco, devices)  # 工资
            if item == 2:  # 宝藏
                freeze_poco = poco.freeze()  # TODO：定义冻结poco
                if freeze_poco("Title").exists() and \
                        freeze_poco("GuildTreasureDlg(Clone)").offspring("item0").exists() and \
                        freeze_poco("GuildTreasureDlg(Clone)").offspring("item1").exists() and \
                        freeze_poco("GuildTreasureDlg(Clone)").offspring("item2").exists():
                    pass
                else:
                    common.printred("公会宝藏界面缺少控件，请检查")
                    common.get_screen_shot(start, time.time(), devices, "公会宝藏界面缺少控件")
                close(poco)
            if item == 3:
                BtnRed(start, poco, devices)  # 红包
            if item == 4:
                Btnfish(start, poco, devices)  # 钓鱼
    return poco("NewGuildHall(Clone)").offspring("NewGuildWelfare").offspring("item4").child("Name").get_text()  # 工会钓鱼


def BtnSignIn(start, poco, devices): # 签到
    common.printgreen("进入签到界面")
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco(texture="public_Flag").exists() and \
            freeze_poco("GuildSignInDlg(Clone)").offspring("SignInButtons").child("item0").child("BtnOK").exists() and \
            freeze_poco("GuildSignInDlg(Clone)").offspring("SignInButtons").child("item0").exists() and \
            freeze_poco("GuildSignInDlg(Clone)").offspring("SignInButtons").child("item1").child("BtnOK").exists() and \
            freeze_poco("GuildSignInDlg(Clone)").offspring("SignInButtons").child("item1").exists() and \
            freeze_poco("GuildSignInDlg(Clone)").offspring("SignInButtons").child("item2").child("BtnOK").exists() and \
            freeze_poco("GuildSignInDlg(Clone)").offspring("SignInButtons").child("item2").exists() and \
            freeze_poco("GuildSignInDlg(Clone)").child("Bg").offspring("item0").exists() and \
            freeze_poco("GuildSignInDlg(Clone)").child("Bg").offspring("item1").exists() and \
            freeze_poco("GuildSignInDlg(Clone)").child("Bg").offspring("item2").exists() and \
            freeze_poco("GuildSignInDlg(Clone)").child("Bg").offspring("item3").exists():
        freeze_poco("GuildSignInDlg(Clone)").offspring("SignInButtons").child("item2").child("BtnOK").click()  # 点击龙币签到
        close(poco)
    else:
        common.printgreen("工会签到界面缺少控件元素")
        common.get_screen_shot(start, time.time(), devices, "工会签到界面缺少控件元素")
        close(poco)


def BtnGz(start, poco, devices):  # 工资
    common.printgreen("进入工资界面")
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("T").exists() and \
            freeze_poco("Scoret").exists() and \
            freeze_poco("Label").exists() and \
            freeze_poco("GuildSalaryDlg(Clone)").offspring("frame").offspring("Up")\
                    .offspring("Background").exists() and \
            freeze_poco("GuildSalaryDlg(Clone)").offspring("frame").child("Left")\
                    .child("Left").offspring("Background").exists() and \
            freeze_poco("GuildSalaryDlg(Clone)").offspring("frame").offspring("Bottom")\
                    .offspring("Background").exists() and \
            freeze_poco("GuildSalaryDlg(Clone)").offspring("frame").child("Left")\
                    .child("Right").offspring("Background").exists() and \
            freeze_poco("GuildSalaryDlg(Clone)").offspring("frame").offspring("item0").exists() and \
            freeze_poco("GuildSalaryDlg(Clone)").offspring("frame").offspring("item1").exists() and \
            freeze_poco("p5").exists():
        poco("GuildSalaryDlg(Clone)").offspring("frame").child("Left").child("Left").child("Go").click()  # 点击提升
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("2").exists() and \
                freeze_poco("0").exists() and \
                freeze_poco("3").exists() and \
                freeze_poco("1").exists():
            common.printgreen("提升界面检查完毕")
            poco("Close").click()
        else:
            common.printred("提升子界面缺少元素，请检查。。。")
            common.get_screen_shot(start, time.time(), devices, "提升子界面缺少元素")
            poco("Close").click()
    close(poco)


def BtnRanking(start, poco, devices):  # 排行
    common.printgreen("进入排行榜界面")
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("16").exists() and freeze_poco("17").exists() and freeze_poco("18").exists():
        freeze_poco("16").click()
        freeze_poco("17").click()
        freeze_poco("18").click()
    else:
        common.printred("进入排行榜界面控件缺失，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "进入排行榜界面控件缺失")
    close(poco)


def BtnSkill(start, poco, devices):  # 技能
    common.printgreen("进入技能界面")
    poco("NewGuildHall(Clone)").offspring("NewGuildInterior").offspring("item0").child("GO").click()
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    for skill in range(1, len(freeze_poco("SkillList").child())):
        skill1 = "Skill" + str(skill)
        if freeze_poco(skill1).exists():
            pass
        else:
            common.printred("工会技能缺失，请检查。。。")
            common.get_screen_shot(start, time.time(), devices, "工会技能缺失")
    if freeze_poco("texbg").exists() and \
            freeze_poco("Name").exists() and \
            freeze_poco("Levelup").exists():
        pass
    else:
        common.printred("工会技能界面元素缺失，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "工会技能界面元素缺失")
    freeze_poco("Levelup").click()  # 点击升级按钮，没办法做是否成功的判断
    close(poco)


def BtnRed(start, poco, devices):  # 红包
    common.printgreen("进入红包界面")
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("Fiexd").exists() and \
            freeze_poco("History").exists():
        poco("Fiexd").click()  # 点击红包池
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco(texture="l_tip_00").exists() and \
            freeze_poco("T3").exists() and \
            freeze_poco("T2").exists() and \
            freeze_poco("T1").exists() and \
            freeze_poco("ailin").exists():
            poco(texture="l_close_00").click()
            poco("History").click()  # 点击历史红包
            if poco("Help").exists():
                poco("Close").click()  # 点击返回
                close(poco)
        else:
            common.printred("红包池界面元素缺失，请检查。。。")
            common.get_screen_shot(start, time.time(), devices, "红包池界面元素缺失")
    else:
        common.printred("工会红包界面元素缺失，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "工会红包界面元素缺失")


def Donation(start, poco, devices):  # 捐赠
    common.printgreen("进入捐赠界面")
    poco("NewGuildHall(Clone)").offspring("NewGuildInterior").offspring("item2").child("GO").click()
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("T").exists() and freeze_poco("RankBtn").exists():
        poco("RankBtn").click()  # 点击排行榜
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("Tittle").exists() and \
                freeze_poco("All").exists() and \
                freeze_poco("Self").exists() and \
                freeze_poco(text="排名").exists() and \
                freeze_poco("Top").child("T")[2].exists() and \
                freeze_poco(text="角色").exists():
            poco("Self").child("TextLabel").click()  # 点击历史排名
            freeze_poco = poco.freeze()  # TODO：定义冻结poco
            if freeze_poco(text="排名").exists() and \
                    freeze_poco("Top").child("T")[2].exists() and \
                    freeze_poco(text="角色").exists():
                poco(texture="l_close_00").click()
            else:
                common.printred("捐赠历史排行界面元素缺失，请检查。。。")
                common.get_screen_shot(start, time.time(), devices, "捐赠历史排行界面元素缺失")
                poco(texture="l_close_00").click()
        else:
            common.printred("捐赠今日排行界面元素缺失，请检查。。。")
            common.get_screen_shot(start, time.time(), devices, "捐赠今日排行界面元素缺失")
            poco(texture="l_close_00").click()
    poco("GrowthDonation").click()  # 点击资材收集
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    for item in range(len(freeze_poco("List").child())):
        item1 = "item" + str(item)
        if freeze_poco(item1).exists() and freeze_poco(item1).child("Do").exists() and freeze_poco("box").exists():
            freeze_poco(item1).child("Do").click()  # 点击缴纳
        else:
            common.printred("捐赠今日排行界面元素缺失，请检查。。。")
            common.get_screen_shot(start, time.time(), devices, "捐赠今日排行界面元素缺失")
    poco("RecordBtn").click()  # 点击捐献记录
    if poco("Tittle").exists():
        poco(texture="l_close_00").click()
    else:
        common.printred("捐赠记录没有弹出，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "捐赠记录没有弹出")
    poco("WeeklyDonation").click()  # 点击悬赏捐赠
    if poco("Bg2").exists():
        close(poco)
    else:
        common.printred("悬赏捐赠，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "悬赏捐赠")


def BtnMall(poco, devices):  # 商店
    common.printgreen("进入商店界面")
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    for item in range(len(freeze_poco("Panel").child())):
        item1 = "item" + str(item)
        if freeze_poco("MallDlg(Clone)").offspring(item1).exists():
            pass
    poco("MallDlg(Clone)").offspring("item0").child("BtnBuy").click()  # 购买商品
    if poco("OK").exists():
        poco("OK").click()
    else:
        common.printgreen("不能购买商品")
    close(poco)

def BtnJoker(start, poco, devices):  # 小丑扑克
    common.printgreen("进入小丑扑克界面")
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco(text="小丑扑克").exists() and \
            freeze_poco(texture="gh_tab_0").exists() and \
            freeze_poco("GameCount").exists() and \
            freeze_poco("FreeChangeCount").exists() and \
            freeze_poco("GuildJokerDlg(Clone)").offspring("Team").child("TextLabel").exists() and \
            freeze_poco("GuildJokerDlg(Clone)").offspring("Guild").exists() and \
            freeze_poco("Button").exists() and \
            freeze_poco("Help"):
        poco("GuildJokerDlg(Clone)").offspring("Guild").click()  # 点击工会排名
        poco("Help").click()  # 点击奖励规则
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if poco("RulePanel").exists():
            for item in range(len(freeze_poco("RulePanel").child()) - 8):
                item1 = "item" + str(item)
                if freeze_poco("Title").exists() and \
                        freeze_poco("RuleTip").exists() and \
                        freeze_poco("GuildJokerDlg(Clone)").offspring("Rule").child("Bg").child("Bg")[0].exists() and \
                        freeze_poco("RuleTpl1").exists() and \
                        freeze_poco("GuildJokerDlg(Clone)").offspring("Rule").offspring(item1).exists():
                    pass
                else:
                    common.printred("奖励规则界面缺少元素，请检查。。。")
                    common.get_screen_shot(start, time.time(), devices, "奖励规则界面缺少元素")
            freeze_poco(texture="l_close_00").click()
        else:
            common.printred("没有进入奖励界面，请检查。。。")
            common.get_screen_shot(start, time.time(), devices, "没有进入奖励界面")
        if int(poco("GuildJokerDlg(Clone)").offspring("GameCount").child("Num").get_text()) != 0:
            poco(text="开始游戏").click()  # 点击开始游戏
            sleep(5)
            poco("Button").click()  # 领取奖励或者结束本居
        else:
            common.printgreen("小丑扑克没有游戏次数了")
    close(poco)


def Btnfish(start, poco, devices):  # 钓鱼
    common.printgreen("进入钓鱼界面")
    poco("NewGuildHall(Clone)").offspring("NewGuildWelfare").offspring("item4").child("GO").click()
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if poco("Title").exists():
        for item in range(len(freeze_poco("ScrollView").child())):
            item1 = "item" + str(item)
            if freeze_poco("NewGuildHall(Clone)").offspring("GuildFishDlg").child("Bg")\
                    .offspring("ScrollView").child(item1).exists():
                pass
        poco(texture="l_close_00").click()  # 点击返回
    else:
        common.printred("没有进入工会钓鱼界面，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "没有进入工会钓鱼界面")


def BtnBuild(start, poco, devices):  # 建造
    common.printgreen("进入建造界面")
    poco("NewGuildHall(Clone)").offspring("NewGuildInterior").offspring("item1").child("GO").click()
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco(text="公会建设").exists():
        if freeze_poco(text="公会建设").exists() and \
                freeze_poco("title3").exists() and \
                freeze_poco("title1").exists() and \
                freeze_poco("title2").exists() and \
                freeze_poco(texture="public_Flag").exists() and \
                freeze_poco("num").exists() and \
                freeze_poco("Go2").exists() and \
                freeze_poco("GuildGrowthBuildDlg(Clone)").offspring("Go2").child("BtnEnter").exists():
            for item in range(len(freeze_poco("WrapContent").child()) - 8):
                item1 = "item" + str(item)
                if freeze_poco("GuildGrowthBuildDlg(Clone)").offspring(item1).exists():
                    poco("GuildGrowthBuildDlg(Clone)").offspring("Go2").child("Help").click()  # 点击帮助介绍
                    if poco("Title").exists():
                        poco("Btn").click()  # 关闭帮助
                    else:
                        common.printred("帮助界面没有打开，请检查。。。")
                        common.get_screen_shot(start, time.time(), devices, "捐赠今日排行界面元素缺失")
                    poco("GuildGrowthBuildDlg(Clone)").offspring("Go2").child("BtnEnter").click()  # 点击前往捐献
                    freeze_poco = poco.freeze()  # TODO：定义冻结poco
                    for item in range(len(freeze_poco("List").child())):
                        item1 = "item" + str(item)
                        if freeze_poco(item1).exists() and \
                                freeze_poco(item1).child("Do").exists() and \
                                freeze_poco("box").exists():
                            freeze_poco(item1).child("Do").click()  # 点击缴纳
                        else:
                            common.printred("捐赠今日排行界面元素缺失，请检查。。。")
                            common.get_screen_shot(start, time.time(), devices, "捐赠今日排行界面元素缺失")
                    poco("Close").click()
    close(poco)


def PlayerBg(start, poco, devices):  # 政厅
    common.printgreen("进入政厅界面")
    poco("NewGuildHall(Clone)").offspring("NewGuildInterior").offspring("item3").child("GO").click()
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("GuildGrowthBuffDlg(Clone)").offspring("Detail").child("Name").exists() and \
            freeze_poco("MaxLevel").exists() and \
            freeze_poco("CurrentLevel").exists() and \
            freeze_poco("CurrentAttr").exists() and \
            freeze_poco("Levelup").exists():
        # TODO：一下是循环点击升级，暂时屏蔽，以免造成不稳定的情况
        # for item in range(len(freeze_poco("SkillList").child())):
        #     item1 = "item" + str(item)
        #     poco("GuildGrowthBuffDlg(Clone)").offspring(item1).click()  # 循环点击技能
        #     freeze_poco("Levelup").click()  # 点击升级按钮
        poco("Close").click()
    else:
        common.printred("工会政厅界面缺少元素，请检查。。。")
        common.get_screen_shot(start, time.time(), devices, "工会政厅界面缺少元素")
        poco("Close").click()


def BtnConsider(start, poco, devices):  # 研究
    common.printgreen("进入研究界面")
    poco("NewGuildHall(Clone)").offspring("NewGuildInterior").offspring("item4").child("GO").click()
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    if freeze_poco("item0").wait().exists() and \
            freeze_poco("item1").wait().exists() and \
            freeze_poco("item2").wait().exists() and \
            freeze_poco("item3").wait().exists():
        freeze_poco("item0").click()
        sleep(1)
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("T").exists() and \
                freeze_poco("GuildGrowthLabDlg(Clone)").offspring("Detail").child("Icon").exists() and \
                freeze_poco("GuildGrowthLabDlg(Clone)").offspring("Detail").child("Name").exists() and \
                freeze_poco("CurrentLevel").exists() and \
                freeze_poco("CurrentAttr").exists() and \
                freeze_poco("Tip").exists() and \
                freeze_poco("Levelup").exists() and \
                freeze_poco("Cost").exists():
            # TODO：一下是循环点击升级，暂时屏蔽，以免造成不稳定的情况
            # for item in range(len(freeze_poco("SkillList").child())):
            #     item1 = "item" + str(item)
            #     poco("GuildGrowthLabDlg(Clone)").offspring(item1).click()   # 循环点击技能
            #     freeze_poco("Levelup").click()  # 点击研究
            poco("Close").click()
            close(poco)
        else:
            common.printred("工会研究所界面缺少元素，请检查。。。")
            common.get_screen_shot(start, time.time(), devices, "工会研究所界面缺少元素")
            poco("Close").click()



def close(poco):
    for i in range(3):
        if not poco(text="公会大厅").exists():
            if poco(texture="l_close_00").exists():
                poco(texture="l_close_00").click()
            elif poco("Close").exists():
                poco("Close").click()
            else:
                common.printred("没有进入公会子界面，请检查")
        else:
            pass


if __name__ == "__main__":
    start = time.localtime()
    guild(start, "e37c0280")