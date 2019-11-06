"""
队伍模块-
脚本环境

"""

from airtest.core.api import *
from multi_processframe.ProjectTools import common, common, common

def troops(start,devices):
    poco = common.deviceconnect(devices)
    if poco("Team").exists():  # 队伍按钮
        if poco("Team").get_position()[0] < 0:
            poco("TaskSwitchBtn").click()
        poco("Team").click()  # 点击队伍按钮
        if not poco("BtnCreate").exists():  # 创建队伍按钮控件
            poco("Team").click()  # 点击队伍按钮
        if poco("BtnLeave").exists():
            common.printgreen("已经有了队伍，先把队伍解散")
            poco("BtnLeave").click()  # 如果已经创建了队伍，就点击离队取消队伍
    else:
        common.printgreen("主界面没有队伍按钮，请检查")
        common.get_screen_shot(start,time.time(), devices, "主界面没有队伍按钮")
    if poco("Title").exists():
        common.printgreen("进入队伍界面，开始判断队伍界面元素。。。")
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("P (1)").exists() and \
                freeze_poco("BtnRefresh").exists() and \
                freeze_poco("BtnTeamRoom").exists() and \
                freeze_poco("BtnCreate").exists() and \
                freeze_poco("BtnMatch").exists():
            common.printgreen("队伍界面控件显示正确，\n开始点击刷新按钮")
            poco("BtnRefresh").click()  # 点击刷新按钮
            common.printgreen("点击刷新按钮，但是因为没有队伍，所以实际上没有任何作用，点着玩吧。。。\n开始点击大厅按钮")
            poco("BtnTeamRoom").click()  # 点击大厅按钮
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if freeze_poco(texture="l_tip_00").exists() and \
                    freeze_poco("Title1").exists() and \
                    freeze_poco("Title2").exists() and \
                    freeze_poco("Title3").exists() and \
                    freeze_poco("Title4").exists() and \
                    freeze_poco("Title5").exists():
                common.printgreen("进入大厅成功")
                for item in range(1, len(freeze_poco("ScrollView").child())):
                    item1 = "item"+str(item)
                    if freeze_poco("TeamListDlg(Clone)").offspring(item1).exists():
                        common.printgreen("检查点 " + freeze_poco("TeamListDlg(Clone)").offspring(item1).child("Text").get_text() + " 显示正确")
                poco("Close").click()  # 点击返回
                for x in range(4):  # 回到主界面
                    if poco("Close").exists():
                        poco("Close").click()
                    else:
                        break
                common.printgreen("返回主界面\n开始进行《组队大厅》界面检测")
            else:
                common.printred("进入大厅失败，请检查")
                common.get_screen_shot(start,time.time(), devices, "进入大厅失败")
    else:
        common.printred("点击队伍按钮后没有进入队伍界面，请检查。。。")
        common.get_screen_shot(start,time.time(), devices, "点击队伍按钮后没有进入队伍界面")
        # todo:创建大厅
    if poco("Team").exists():  # 队伍按钮
        if poco("Team").get_position()[0] < 0:
            poco("TaskSwitchBtn").click()
        poco("BtnJoin").click()  # 点击组队大厅
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco(texture="l_tip_00").exists() and \
                freeze_poco("Title1").exists() and \
                freeze_poco("Title2").exists() and \
                freeze_poco("Title3").exists() and \
                freeze_poco("Title4").exists() and \
                freeze_poco("Title5").exists():
            common.printgreen("进入大厅成功")
            for item in range(1, len(freeze_poco("ScrollView").child())):
                item1 = "item" + str(item)
                if freeze_poco("TeamListDlg(Clone)").offspring(item1).exists():
                    common.printgreen("检查点 " + freeze_poco("TeamListDlg(Clone)").offspring(item1).child("Text").get_text() + " 显示正确")
            poco("Close").click()  # 点击返回
            for x in range(4):  # 回到主界面
                if poco("Close").exists():
                    poco("Close").click()
                else:
                    break
            common.printgreen("返回主界面\n开始进行《招募大厅》界面检测")
        else:
            common.printred("进入大厅失败，请检查")
            common.get_screen_shot(start,time.time(), devices, "进入大厅失败")
    else:
        common.printgreen("主界面没有队伍按钮，请检查")
        common.get_screen_shot(start,time.time(), devices, "主界面没有队伍按钮")

    # todo:招募大厅
    if poco("Team").exists():  # 队伍按钮
        if poco("Team").get_position()[0] < 0:
            poco("TaskSwitchBtn").click()
        poco("BtnGroupChat").click()  # 点击招募大厅
        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
        if freeze_poco("RecruitDlg(Clone)").child("Bg").offspring("Text")[1].exists() and \
                freeze_poco("RecruitDlg(Clone)").offspring("ToggleTeam").child("SelectedText").exists() and \
                freeze_poco("Title0").exists() and freeze_poco("Title2").exists() and freeze_poco("Title3").exists() and \
                freeze_poco("Title4").exists() and freeze_poco("Title1").exists() and freeze_poco(text="队友验证").exists() and \
                freeze_poco(text="发布招募").exists():
            common.printgreen("进入招募大厅大厅成功\n开始检测下级界面《队友验证》")
            poco("Btn_Authorise").click()  # 点击队友验证
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            if freeze_poco("RecruitDlg(Clone)").child("Bg").offspring("Text")[1].exists() and \
                    freeze_poco("Title1").exists() and freeze_poco("Title2").exists() and freeze_poco("Title3").exists() and \
                    freeze_poco("Title4").exists() and freeze_poco("Title5").exists():
                common.printgreen("进入招募队友验证成功")
                poco("RecruitAuthorizeView(Clone)").child("Close").click()  # 点击返回
                if poco("RecruitDlg(Clone)").child("Bg").offspring("Text")[1].exists():
                    common.printgreen("返回招募大厅成功\n开始检测下级界面《发布招募》")
                    poco("Btn_Publish").click()  # 点击发布招募
                    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                    if freeze_poco(text="队员招募").exists() and freeze_poco(text="队员招募").exists() and \
                            freeze_poco(text="擅长类型").exists() and freeze_poco(text="选择队伍").exists() and \
                            freeze_poco(text="发 布").exists() and freeze_poco(text="新建队伍").exists() and \
                            freeze_poco("GroupMember_Type0").exists() and freeze_poco("GroupMember_Type1").exists() and \
                            freeze_poco("GroupMember_Type2").exists() and freeze_poco("GroupMember_Type3").exists():
                        for Label in freeze_poco("RecruitGroupPublishFrame(Clone)").offspring("1").offspring(
                                "ChildList").offspring("Selected").offspring("Label"):
                            common.printgreen("检查点 《" + Label.get_text() + "》 显示正确")
                        for Label in freeze_poco("RecruitGroupPublishFrame(Clone)").offspring("2").offspring(
                                "ChildList").offspring("Selected").offspring("Label"):
                            common.printgreen("检查点《 " + Label.get_text() + "》 显示正确")
                        for Label in freeze_poco("RecruitGroupPublishFrame(Clone)").offspring("3").offspring(
                                "ChildList").offspring("Selected").offspring("Label"):
                            common.printgreen("检查点 《" + Label.get_text() + "》 显示正确")
                        common.printgreen("检查点 《发布招募》 界面显示正确\n点击返回到上级界面")
                        poco("RecruitGroupPublishFrame(Clone)").offspring("Close").click()
                        if poco("ToggleMember").exists():  # 寻找队友
                            poco("ToggleMember").click()
                            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                            if freeze_poco("Title0").exists() and \
                                    freeze_poco("Title0").exists() and \
                                    freeze_poco("Title0").exists() and \
                                    freeze_poco("Title0").exists() and \
                                    freeze_poco("Title0").exists():
                                common.printgreen("检查点 《寻找队友》 界面显示正确")
                                poco("ToggleTeam").click()  # 点击寻找队伍，回到上级界面，为下次测试恢复环境
                            else:
                                common.printred("寻找队友界面缺少按钮控件元素，请检查")
                                common.get_screen_shot(start,time.time(), devices, "队友验证界面缺少按钮控件元素")

            else:
                common.printred("队友验证界面缺少按钮控件元素，请检查")
                common.get_screen_shot(start,time.time(), devices, "队友验证界面缺少按钮控件元素")
        else:
            common.printred("招募大厅界面缺少按钮控件元素，请检查")
            common.get_screen_shot(start,time.time(), devices, "招募大厅界面缺少按钮控件元素")
    else:
        common.printred("主界面没有队伍按钮，请检查")
        common.get_screen_shot(start,time.time(), devices, "主界面没有队伍按钮")
    return poco("Btn_Authorise").child("T").get_text()  # 队友验证

