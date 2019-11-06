# -*- encoding=utf8 -*-
__author__ = "Lee.li"

# 英雄战场-上古力量
# 天梯赛
# 角斗场
# 竞技巢穴
# 神圣联赛
# 保护队长(限时开)

from airtest.core.api import *
from multi_processframe.ProjectTools import common, common, common
from multi_processframe.ProjectTools import common


def athletics(start, devices):
     poco = common.deviceconnect(devices)
     if poco("SysEPVP").exists():
         print("竞技场已开启，测试竞技场相关功能")
         poco("SysEPVP").click()
         with poco.freeze() as freezepoco:
             if freezepoco("Btn_MobaFamous").exists() and \
                     freezepoco("Btn_MobaRank").exists() and \
                     freezepoco("MobaActivityDlg(Clone)").offspring("item0").exists() and \
                     freezepoco("MobaActivityDlg(Clone)").offspring("item1").exists() and \
                     freezepoco("MobaActivityDlg(Clone)").offspring("item2").exists() and \
                     freezepoco("MobaActivityDlg(Clone)").offspring("item3").exists() and \
                     freezepoco("MobaActivityDlg(Clone)").offspring("item4").exists():
                 common.printgreen("竞技军衔，竞技名人堂，竞技副本显示正常")
             else:
                 common.printred("竞技界面缺少元素，请详细查看")
                 common.get_screen_shot(start, time.time(), devices, "竞技界面缺少元素，请详细查看")
             name = freezepoco("PVPActivityFrame").offspring("Panel").child()
             print(f"PVP开放内容的描述为：{len(name)}项内容")
             count = 1
             for i in name:
                 uiname = i.get_name()
                 print(f"{count}.",end="")
                 if freezepoco(uiname).offspring("Desc").get_text() == "实时对战，领取称号和时装":
                     common.printgreen("天梯赛--" + freezepoco(uiname).offspring("Desc").get_text())
                 elif freezepoco(uiname).offspring("Desc").get_text() == "巅峰对决，跨服对战":
                     common.printgreen("角斗场--" + freezepoco(uiname).offspring("Desc").get_text())
                 elif freezepoco(uiname).offspring("Desc").get_text() == "4V4争夺据点，赢取龙币":
                     common.printgreen("英雄战场--" + freezepoco(uiname).offspring("Desc").get_text())
                 elif freezepoco(uiname).offspring("Desc").get_text() == "释放操作，与全球玩家比拼":
                     common.printgreen("全球竞技--" + freezepoco(uiname).offspring("Desc").get_text())
                 elif freezepoco(uiname).offspring("Desc").get_text() == "保护队长，获得传说装备":
                     common.printgreen("保护队长--" + freezepoco(uiname).offspring("Desc").get_text())
                 else:
                     common.printgreen("其他的PVP模式--" + freezepoco(uiname).offspring("Desc").get_text())
                 count += 1
         if poco("Btn_MobaRank").exists():
             poco("Btn_MobaRank").click()
             with poco.freeze() as freezepoco:
                 if freezepoco("Date").exists() and \
                         freezepoco("RewardBtn").exists() and \
                         freezepoco("RecordBtn").exists() and \
                         freezepoco(text="排名").exists() and \
                         freezepoco("MilitaryRankDlg(Clone)").child("Bg").offspring("Titles").child("T")[1].exists() and \
                         freezepoco(text="角色").exists() and \
                         freezepoco("MilitaryRankDlg(Clone)").child("Bg").offspring("Titles").child("T")[3].exists() and \
                         freezepoco("MilitaryRankDlg(Clone)").offspring("Help").exists() :
                     common.printgreen("规则 赛季时间，军衔奖励，挑战记录，排名，军衔，角色，军功元素显示正常")
                 else:
                     common.printred("规则 赛季时间，军衔奖励，挑战记录，排名，军衔，角色，军功元素缺少，请具体核对")
                     common.get_screen_shot(start, time.time(), devices, "竞技军衔按钮不存在")
             poco("RewardBtn").click()
             poco("ToggleResult").click()
             with poco.freeze() as freezepoco:
                 uiname = freezepoco("MilitaryRankDlg(Clone)").offspring("Panel").child()
                 print("打印达成的条件")
                 common.printgreen("军衔           所需军功")
                 for i in uiname:
                     name = i.get_name()
                     if name[:4] == "item":
                         rank = freezepoco(name).child("MilitaryName").get_text()
                         exploit = freezepoco(name).child("Value").get_text()

                         print(rank,"           ",exploit.replace("\n", ""))
             poco("ToggleSeason").click()
             with poco.freeze() as freezepoco:
                 uiname = freezepoco("MilitaryRankDlg(Clone)").offspring("Panel").child()
                 count = 0
                 for i in uiname:
                     name = i.get_name()
                     if name[:4] == "item":
                         count += 1
                 print(f"赛季奖励一共有{count}个条目",end=",")
                 if count == 8:
                     common.printgreen("赛季奖励的条目正常")
                 else:
                     common.printred("赛季奖励的条目不是8条，请前往查看少了哪个")
                     common.get_screen_shot(start, time.time(), devices, "竞技军衔按钮不存在")
             common.settouch(1, 140, 389, devices, times=2)
             poco("Close").click()
         else:
             common.printred("竞技军衔按钮不存在")
             common.get_screen_shot(start, time.time(), devices, "竞技军衔按钮不存在")
         if poco("Btn_MobaFamous").exists():
             poco("Btn_MobaFamous").click()
             with poco.freeze() as freezepoco:
                 if freezepoco("item0").exists() and \
                        freezepoco("item1").exists() and \
                        freezepoco("item2").exists() and \
                        freezepoco("item3").exists() and \
                        freezepoco("HallFameDlg(Clone)").offspring("Help").exists() and \
                        freezepoco("RankList").exists() and \
                        freezepoco("Support").exists():
                     common.printgreen("1:1天梯赛，英雄战场，全球竞技，跨服巅峰对决，点赞，规则，排行榜按钮显示正常")
                 else:
                     common.printred("1:1天梯赛，英雄战场，全球竞技，跨服巅峰对决，点赞，规则，排行榜按钮显示异常")
                     common.get_screen_shot(start, time.time(), devices, "天梯赛报错异常")
             if poco("HallFameDlg(Clone)").offspring("Help").exists():
                poco("HallFameDlg(Clone)").offspring("Help").click()
                if poco("ScrollView").exists():
                    print(poco("ScrollView").offspring("Content").get_text())
                    poco("Btn").click()
                count = poco("Tabs").child()
                for i in range(len(count)):
                    item = "item" + str(i)
                    poco(item).click()
                    with poco.freeze() as freezepoco:
                        uiname = freezepoco(item).offspring("SelectedTextLabel").get_text()
                        print(f"测试{uiname}模块")
                        if freezepoco("Support").child("RedPoint").exists():
                            print("执行点赞操作")
                            freezepoco("Support").click()
                            if poco("ItemIconListBattleDlg(Clone)").exists():
                                common.printgreen("点赞成功，拿到了点赞奖励")
                                poco("ItemIconListBattleDlg(Clone)").offspring("Bg").child("Close").click() # 关闭点赞奖励窗口
                        if freezepoco("RankList").exists():
                            print("点击上赛季排行榜")
                            freezepoco("RankList").click()
                            if poco(text="排名"):
                                common.printgreen(f"排行榜打开正常")
                                poco(texture="l_close_00").click()
                        else:
                            print("此功能没有排行榜")
                poco("Close").click() # 回到初始界面
                poco("MobaActivityDlg(Clone)").offspring("item0").click() # 进入天梯赛
                with poco.freeze() as freezepoco:
                    if freezepoco("SelectedTextLabel").exists() and \
                            freezepoco("PointRewardBtn").exists() and \
                            freezepoco("RankRewardBtn").exists() and \
                            freezepoco(texture="l_frame_00").exists() and \
                            freezepoco("ShopBtn").exists() and \
                            freezepoco("RankBtn").exists() and \
                            freezepoco("HallDlg(Clone)").child("Adapter").exists() and \
                            freezepoco("BattleRecordBtn").exists() and \
                            freezepoco("RecommededTip").exists() and \
                            freezepoco("TrainingBtn").exists() and \
                            freezepoco("Match1V1Btn").exists():
                        common.printgreen("1:1天梯赛，评分奖励，排名奖励，荣誉商店，排行榜，对战记录，积分排名，开始匹配，技能教学，技能推荐按钮显示正常")
                    else:
                        common.printred("1:1天梯赛，评分奖励，排名奖励，荣誉商店，排行榜，对战记录，积分排名，开始匹配，技能教学，技能推荐按钮显示异常")
                        common.get_screen_shot(start, time.time(), devices, "天梯赛报错")
                    try:
                        poco("PointRewardBtn").click()
                        poco(texture="l_close_00").click()
                        poco("RankRewardBtn").click()
                        poco(texture="l_close_00").click()
                        poco("QualifierDlg(Clone)").child("Bg").offspring("ShopBtn").child("p").click()
                        poco("Close").click()
                        poco("RankBtn").click()
                        poco(texture="l_close_00").click()
                        poco("BattleRecordBtn").click()
                        poco(texture="l_close_00").click()
                        poco("P1").click()
                        poco("TabTpl0").offspring("Selected").click()
                        poco("Close").click()
                        poco("Match1V1Btn").click()
                        poco("Match1V1Btn").click()
                        poco("Close").click()
                        common.printgreen("天梯赛所有按钮点击关闭操作正常")
                    except Exception as e:
                        common.printred("天梯赛界面元素点击报错")
                        common.printred(e)
                        common.get_screen_shot(start, time.time(), devices, "天梯赛界面元素点击报错")
                        poco("Close").click()
                poco("MobaActivityDlg(Clone)").offspring("item1").click()  # 进入角斗场
                with poco.freeze() as freezepoco:
                    if freezepoco("Help").exists() and \
                            freezepoco("AbattoirDlg(Clone)").offspring("PointRewardBtn").exists() and \
                            freezepoco("RankBtn").exists() and \
                            freezepoco("ShopBtn").exists() and \
                            freezepoco("RecommededTip").exists() and \
                            freezepoco("MatchBtn").exists() and \
                            freezepoco("AbattoirDlg(Clone)").offspring("WinOfPoint").child("Num"):
                        common.printgreen("三个排名奖励，升段奖励，排行榜，荣誉商店，参与宝箱，胜利宝箱，技能推荐按钮显示正常")
                    else:
                        common.printred("三个排名奖励，升段奖励，排行榜，荣誉商店，参与宝箱，胜利宝箱，技能推荐按钮显示异常")
                        common.get_screen_shot(start, time.time(), devices, "角斗场报错")
                    try:
                        poco("Help").click()
                        poco("Btn").click()
                        poco("AbattoirDlg(Clone)").offspring("PointRewardBtn").child("p").click()
                        poco(texture="l_close_00").click()
                        poco("RankBtn").click()
                        poco(texture="l_close_00").click()
                        poco("ShopBtn").click()
                        poco("Close").click()
                        poco("RecommededTip").click()
                        poco("TabTpl0").offspring("Selected").click()
                        poco("Close").click()
                        poco("GoldJoyBtn").click()
                        if poco("GoldBoxBtn").exists():
                            poco("GoldBoxBtn").click()
                        common.printgreen("角斗场所有按钮点击关闭操作正常")
                        poco("MatchBtn").click()  # 进入角度场
                        time.sleep(20)
                        if poco("Pause").exists():
                            time.sleep(5)
                            poco("Pause").click()
                            poco("Leave").click()
                            time.sleep(15)
                            poco("SysEPVP").click()
                            common.printgreen("角斗场进入退出正常")
                            if poco("SysEPVP").exists():
                                poco("SysEPVP").click()
                        else:
                            common.printred("角斗场进入失败")
                            common.get_screen_shot(start, time.time(), devices, "角斗场进入失败")
                            poco("Close").click()
                    except Exception as e:
                        common.printred("角斗场界面元素点击报错")
                        common.printred(e)
                        common.get_screen_shot(start, time.time(), devices, "角斗场界面元素点击报错")
                        poco("Close").click()
                poco("MobaActivityDlg(Clone)").offspring("item2").click()  # 进入英雄战场
                with poco.freeze() as freezepoco:
                    if freezepoco("Help").exists() and \
                            freezepoco("tq").exists() and \
                            freezepoco("ResearchBtn").exists() and \
                            freezepoco("SkillBtn").exists() and \
                            freezepoco("RankBtn").exists() and \
                            freezepoco("ShopBtn").exists() and \
                            freezepoco("RecordBtn").exists() and \
                            freezepoco("RewardPreViewBtn").exists() and \
                            freezepoco("WeekReward").exists() and \
                            freezepoco("ExReward").exists() and \
                            freezepoco("SingleMatchBtn").exists() and \
                            freezepoco("TeamMatchBtn").exists() and \
                            freezepoco("BuyBtn").exists() and \
                            freezepoco("ScrollView").exists():
                        common.printgreen("规则，玩法攻略，技能预览，排行榜，商店，挑战记录，奖励预览，本周奖励，每日首胜，单人匹配，组队匹配，购买按钮，英雄列表等元素显示正常")
                    else:
                        common.printred("规则，玩法攻略，技能预览，排行榜，商店，挑战记录，奖励预览，本周奖励，每日首胜，单人匹配，组队匹配，购买按钮，英雄列表等元素显示异常")
                        common.get_screen_shot(start, time.time(), devices, "英雄战场点击报错")
                    try:
                        poco("Help").click()
                        poco("Btn").click()
                        poco("RankBtn").click()
                        poco("RankFrame").offspring("Bg").child("Close").click()
                        poco("HeroBattleDlg(Clone)").offspring("ShopBtn").click()
                        poco("MallDlg(Clone)").offspring("Bg").child("Close").click()
                        poco("RecordBtn").click()
                        poco("BattleRecordFrame").child("Close").click()
                        poco("RewardPreViewBtn").click()
                        poco("RewardPreView").offspring("Bg").child("Close").click()
                        poco("SingleMatchBtn").click()
                        poco("SingleMatchBtn").click()
                        poco("TeamMatchBtn").click()
                        poco("Close").click()
                        common.printgreen("英雄战场所有按钮点击关闭操作正常")
                    except Exception as e:
                        common.printred("英雄战场界面元素点击报错")
                        common.printred(e)
                        poco("Close").click()
                        common.get_screen_shot(start, time.time(), devices, "英雄战场界面元素点击报错")
                poco("MobaActivityDlg(Clone)").offspring("item3").click()  # 进入全球战场
                with poco.freeze() as freezepoco:
                    if freezepoco("0").exists() and \
                            freezepoco("GlobalCompetition").exists() and \
                            freezepoco("RankBtn").exists() and \
                            freezepoco("GoBtn").exists() and \
                            freezepoco("Tittle1").exists() and \
                            freezepoco("Times").exists() and \
                            freezepoco("t").exists():
                        common.printgreen("大标题，介绍内容，全球榜，排行榜，前往挑战按钮，可能获得的奖励显示正常")
                    else:
                        common.printred("大标题，介绍内容，全球榜，排行榜，前往挑战按钮，可能获得的奖励等元素显示异常")
                        common.get_screen_shot(start, time.time(), devices, "全球竞技缺少对应按钮")
                    try:
                        poco("0").child("Icon").click()
                        poco("0").child("Icon").click()
                        poco("RankBtn").click()
                        poco("WeekNestRank").child("Close").click()
                        poco("GoBtn").click()
                        poco("Close").click()
                        poco("Close").click()
                        common.printgreen("全球竞技缺所有按钮点击关闭操作正常")
                    except Exception as e:
                        common.printred("全球竞技缺界面元素点击报错")
                        common.printred(e)
                        poco("Close").click()
                        common.get_screen_shot(start, time.time(), devices, "全球竞技缺界面元素点击报错")
                poco("MobaActivityDlg(Clone)").offspring("item4").click()  # 进入保护队长
                with poco.freeze() as freezepoco:
                    if freezepoco("CaptainDlg(Clone)").offspring("WeekReward").child("ListPanel").exists() and \
                            freezepoco("CaptainDlg(Clone)").offspring("ExReward").child("ListPanel").exists() and \
                            freezepoco("BtnStartSingle").exists() and \
                            freezepoco("BtnStartTeam").exists() and \
                            freezepoco("BtnShop").exists() and \
                            freezepoco("BtnRecord").exists() and \
                            freezepoco("Help").exists() and \
                            freezepoco("BattleRecord").exists() and \
                            freezepoco("GameRule").exists() and \
                            freezepoco("MatchNum").exists():
                        common.printgreen("周奖励，日奖励，单人匹配，组队匹配，荣誉商店，对战记录，规则，场次计算显示正常")
                    else:
                        common.printred("周奖励，日奖励，单人匹配，组队匹配，荣誉商店，对战记录，规则，场次计算显示正常")
                        common.get_screen_shot(start, time.time(), devices, "保护队长元素报错")
                    try:
                        poco("Help").click()
                        poco("Btn").click()
                        poco("BtnShop").click()
                        poco("Close").click()
                        poco("BtnRecord").click()
                        poco(texture="l_close_00").click()
                        poco("BtnStartSingle").click()
                        poco("BtnStartSingle").click()
                        poco("BtnStartTeam").click()
                        poco("Close").click()
                        common.printgreen("保护队长所有按钮点击关闭操作正常")
                    except Exception as e:
                        common.printred("保护队长界面元素点击报错")
                        common.printred(e)
                        poco("Close").click()
                        common.get_screen_shot(start, time.time(), devices, "保护队长报错")
             else:
                common.printred("界面缺少元素，麻烦检查")
                common.get_screen_shot(start, time.time(), devices, "竞技军衔按钮不存在")
         else:
             common.printred("竞技名人堂按钮不存在")
             common.get_screen_shot(start, time.time(), devices, "竞技名人堂按钮不存在")
     else:
         common.printred("竞技场暂未开放，请升级或者查看相关配置")
         common.get_screen_shot(start, time.time(), devices, "竞技功能未开放")
     return poco("Btn_MobaRank").get_name()  # 返回值
# devices = "127.0.0.1:62001"
# athletics(devices)