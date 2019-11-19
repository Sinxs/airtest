"""
技能模块，界面判断
"""
from airtest.core.api import *
from multi_processframe.ProjectTools import common


def skill(start, devices):
    poco = common.deviceconnect(devices)
    if poco("SysBSkill").get_position()[0] > 1:
        poco(texture="halln_4").click()
        sleep(2)
    else:
        common.printgreen("当前界面就有技能按钮")
    poco("SysBSkill").click()  # 点击技能按钮
    if poco("SkillTreeBox").exists():
        common.printgreen("进入技能界面")
        chongzhi(poco)
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        # for item in freeze_poco("SkillTree(Clone)").offspring("Tabs").offspring("Selected"):
        for item in freeze_poco("SkillTree(Clone)").offspring("Tabs").offspring("SelectedTextLabel"):
            # 点击职业选项
            common.printgreen(f"开始点击  {item.get_text()}  页签")
            item.click()
            sleep(2)
            freeze_poco = poco.freeze()  # TODO：定义冻结poco
            if freeze_poco("SkillTree(Clone)").offspring("Icon").exists():
                count = 0
                for skill in freeze_poco("SkillTree(Clone)").offspring("Icon"):
                    skill.click()
                    count += 1
                    if count >= 2:
                        break
    return poco("SkillTree(Clone)").offspring("Tabs").child("item3").child("SelectedTextLabel").get_text()  # 觉醒


def switch_roles(start, devices):
    poco = common.deviceconnect(devices)
    if poco("SysBSkill").get_position()[0] > 1:
        poco(texture="halln_4").click()
        sleep(2)
    else:
        common.printgreen("当前界面就有技能按钮")
    poco("SysBSkill").click()  # 点击技能按钮
    if poco("item4").exists():  # 点击职业切换
        poco("item4").click()
        if poco("SkillTree(Clone)").offspring("WrapContent").offspring("item3").exists():  # 点击牧师icon
            poco("SkillTree(Clone)").offspring("WrapContent").offspring("item3").click()
            if poco("jihuob").exists():  # 点击激活职业按钮
                poco("jihuob").click()
                sleep(1.5)
                if poco("ItemAccessDlg(Clone)").offspring("Title").exists():  # 如果没有职业变更券
                    goumai(poco)  # 进入购买
                    common.printgreen("购买完成")
                    if poco("jihuob").exists():  # 点击激活职业按钮
                        poco("jihuob").click()
                        sleep(1.5)
                        if poco("ItemAccessDlg(Clone)").offspring("Title").exists():  # 如果没有职业变更券
                            common.printred("上次购买失败，有bug")
                            goumai(poco)  # 进入购买

            if poco("qiehuan").exists():  # 点击切换该职业
                common.printgreen("点击切换该职业")
                poco("qiehuan").click()
                if poco("OK").exists():  # 点击确定切换
                    poco("OK").click()
                    if poco("OK").exists():
                        common.printgreen("已经拥有该职业")
                        poco("OK").click()
                    if not poco("qiehuan").exists():
                        common.printgreen("切换成功")
                    else:
                        common.printred("职业切换失败")
                        common.get_screen_shot(start, time.time(), devices, "职业切换失败")
                        return None

                    # 转回战士职业
                    common.printgreen("转回战士职业")
                    if poco("SkillTree(Clone)").offspring("WrapContent").offspring("item0").exists():
                        poco("SkillTree(Clone)").offspring("WrapContent").offspring("item0").click()
                        if poco("jihuob").exists():  # 点击激活职业按钮
                            poco("jihuob").click()
                            sleep(1.5)
                            if poco("ItemAccessDlg(Clone)").offspring("Title").exists():  # 如果没有职业变更券
                                goumai(poco)  # 进入购买
                                common.printgreen("购买完成")
                                if poco("jihuob").exists():  # 点击激活职业按钮
                                    poco("jihuob").click()
                                    sleep(1.5)
                                    if poco("ItemAccessDlg(Clone)").offspring("Title").exists():  # 如果没有职业变更券
                                        common.printred("上次购买失败，有bug")
                                        goumai(poco)  # 进入购买
                        if poco("qiehuan").exists():  # 点击切换该职业
                            common.printgreen("点击切换该职业")
                            poco("qiehuan").click()
                            if poco("OK").exists():  # 点击确定切换
                                poco("OK").click()
                                if poco("OK").exists():
                                    common.printgreen("已经拥有该职业")
                                    poco("OK").click()
                                if not poco("qiehuan").exists():
                                    common.printgreen("切换成功")
                                else:
                                    common.printred("职业切换失败")
                                    common.get_screen_shot(start, time.time(), devices, "职业切换失败")
                                    return None
                                chongzhi(poco)
    return poco("SkillTree(Clone)").offspring("Tabs").child("item3").child("SelectedTextLabel").get_text()  # 觉醒


def chongzhi(poco):
    """
    重置技能脚本环境
    :param poco:
    :return:
    """
    if poco("SkillTree(Clone)").offspring("Tabs").child("item1").exists():
        poco("SkillTree(Clone)").offspring("Tabs").child("item1").click()
        if poco("CatchButton").exists():
            poco("CatchButton").click()
            poco("OK").click()
            sleep(1)
    if poco("SkillTree(Clone)").offspring("Tabs").child("item2").exists():
        poco("SkillTree(Clone)").offspring("Tabs").child("item2").click()
        if poco("TurnProBtn").exists():
            poco("TurnProBtn").click()
            poco("OK").click()
            sleep(1)
    if poco("SkillTree(Clone)").offspring("Tabs").child("item3").exists():
        poco("SkillTree(Clone)").offspring("Tabs").child("item3").click()
        if poco("TurnAwakeBtn").exists():
            poco("TurnAwakeBtn").click()

def goumai(poco):
    """
    购买转职券
    :param poco:
    :return:
    """
    poco("access212").click()  # 点击龙币商城
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    for i in range(10):
        freeze_poco("OK").click()  # 点击购买
    poco("Close")

if __name__ == "__main__":
    start = time.localtime()
    switch_roles(start, "9b57691d")
    # skill(start, "9b57691d")