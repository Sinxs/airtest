# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from multi_processframe.ProjectTools.common import *
from airtest.core.api import *


def npcfavor(start, devices):
    """
    佣兵测试脚本
    :param devices:
    :return:
    """
    poco = deviceconnect(devices)
    check_menu("SysF_Machine", poco)  # 进入精灵
    if poco("MachineArmorDlg(Clone)").exists():  # 判断佣兵界面是否存在
        with poco.freeze() as freeze_poco:
            if freeze_poco("MachineArmorDlg(Clone)").offspring("MachineScrollview").child("Wrapcontent").exists() and \
                    freeze_poco("Title1").exists() and \
                    freeze_poco("Title2").exists() and \
                    freeze_poco("ActivationBtn").exists() and \
                    freeze_poco("List").exists() and \
                    freeze_poco("say").exists() and \
                    freeze_poco("SnapDrag").exists() and \
                    freeze_poco("MachineArmorDlg(Clone)").offspring("SkillScrollview").child("Wrapcontent").exists():
                printgreen("佣兵界面UI元素显示正常")
            else:
                printred("佣兵界面UI元素显示异常，详情见截图")
                get_screen_shot(start, time.time(), devices, "佣兵界面UI元素显示异常")
            try:
                count = 0
                with poco.freeze() as freeze_poco:
                    for i in freeze_poco("MachineArmorDlg(Clone)").offspring("MachineScrollview").child("Wrapcontent").offspring("HeadIcon"):  # 循环有多少个佣兵
                        uiname = i.parent().get_name()
                        name = freeze_poco(uiname).child("Name").get_text()
                        freeze_poco(uiname).click()
                        poco("MachineArmorDlg(Clone)").offspring("MachineScrollview").offspring(uiname).offspring("Frame").click()
                        poco("Obtain").click()
                        poco("Obtain").click()
                        if poco("main").exists():
                            poco("Obtain").click()
                        poco(texture="l_close_00").click()
                        if poco("SnapDrag").exists():

                            printgreen(f"{name}佣兵模型显示正常")
                        else:
                            printred(f"{name}佣兵模型不显示")
                            get_screen_shot(start, time.time(), devices, "佣兵模型不显示")
                        freeze_poco("ActivationBtn").click()
                        freeze_poco("ActivationBtn").click()
                        with poco.freeze() as freeze_poco1:
                            for i in freeze_poco1("MachineArmorDlg(Clone)").offspring("SkillScrollview").child("Wrapcontent").child():  # 循环有多少个技能
                                i.click()
                                if poco("MachineSkillPreView(Clone)").child("Bg").child("p").exists():
                                    i.click()
                        count += 1
                        if count == 5:
                            break
                    printgreen("佣兵模块所有按钮点击正常")
            except Exception as e:
                printred("佣兵界面按钮点击流程异常")
                printred(e)
                get_screen_shot(start, time.time(), devices, "佣兵界面按钮点击流程异常")
    else:
        printred("佣兵界面报错，详情见截图")
        get_screen_shot(start, time.time(), devices, "佣兵界面报错")
    return poco("SnapDrag").get_name()  # 返回值poco("Duck").get_name()


def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 1:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco("MenuSwitchBtn").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()


if __name__ == "__main__":
    start = time.localtime()
    npcfavor(start, "9b57691d")