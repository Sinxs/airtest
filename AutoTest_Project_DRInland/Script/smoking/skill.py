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
            if poco("WrapContent").offspring("head").exists():
                count = 0
                for skill in freeze_poco("WrapContent").offspring("head"):
                    skill.click()
                    count += 1
                    if count >= 4:
                        break
    return poco("jihuob").child("T").get_text()  # 激活职业


if __name__ == "__main__":
    start = time.localtime()
    skill(start, "e37c0280")