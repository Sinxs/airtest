"""
伙伴模块
"""
# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from multi_processframe.ProjectTools.common import *
from airtest.core.api import *


def monster(start, devices):
    """
    伙伴测试脚本
    :param devices:
    :return:
    """
    poco = deviceconnect(devices)
    check_menu("SysDMonster", poco)  # 进入精灵
    if poco("BookBg").exists():  # 判断伙伴界面是否存在
        with poco.freeze() as freeze_poco:
            if freeze_poco("item0").child("selected").exists() and \
                    freeze_poco("item1").child("selected").exists() and \
                    freeze_poco("item2").child("selected").exists() and \
                    freeze_poco("StarCount").exists() and \
                    freeze_poco("Stars").exists() and \
                    freeze_poco("BtnReward").exists() and \
                    freeze_poco("BtnAttrTotal").exists() and \
                    freeze_poco("WrapContent").exists() and \
                    freeze_poco("MonsterpreferenceDlg(Clone)").child("Help").exists() and \
                    freeze_poco("Icons").offspring("item0").exists() and \
                    freeze_poco("Icons").offspring("item1").exists() and \
                    freeze_poco("Select").exists() and \
                    freeze_poco("ActiveBtn").exists():
                printgreen("伙伴界面UI元素显示正常")
            else:
                printred("伙伴界面UI元素显示异常，详情见截图")
                get_screen_shot(start, time.time(), devices, "伙伴界面UI元素显示异常")
            try:
                freeze_poco("item1").child("selected").click()
                freeze_poco("item2").child("selected").click()
                freeze_poco("MonsterpreferenceDlg(Clone)").child("Help").click()
                poco("Btn").click()
                freeze_poco("BtnReward").click()
                poco("PointRewardFrame").offspring("Close").click()
                freeze_poco("BtnAttrTotal").click()
                freeze_poco("BtnAttrTotal").click()
                freeze_poco("ActiveBtn").click()
                printgreen("伙伴界面按钮点击正常")
            except Exception as e:
                printred("伙伴界面按钮点击流程异常")
                printred(e)
                get_screen_shot(start, time.time(), devices, "伙伴界面按钮点击流程异常")
            try:
                print("测试A级伙伴的数量")
                poco("item1").child("selected").click()
                for i in range(len(poco("WrapContent").child())):
                    PetGroup = "PetGroup" + str(i)
                    poco(PetGroup).click()
                    count = len(poco("MonsterpreferenceDlg(Clone)").child("ItemListPanel").child("Bg1").child("Icons").offspring("Item"))
                    if count == 4:
                        uiname = poco(PetGroup).child("Name").get_text()
                        printgreen(f"{uiname}的伙伴一共有4个")
                    else:
                        printred(f"{uiname}的伙伴少了，只出现了{count}个")
                        get_screen_shot(start, time.time(), devices, "遍历伙伴数量异常")
                print("测试B级伙伴的数量")
                poco("item2").child("selected").click()
                for i in range(len(poco("WrapContent").child())):
                    PetGroup = "PetGroup" + str(i)
                    poco(PetGroup).click()
                    count = len(poco("MonsterpreferenceDlg(Clone)").child("ItemListPanel").child("Bg1").child("Icons").offspring("Item"))
                    if count == 3:
                        uiname = poco(PetGroup).child("Name").get_text()
                        printgreen(f"{uiname}的伙伴一共有4个")
                    else:
                        printred(f"{uiname}的伙伴少了，只出现了{count}个")
                        get_screen_shot(start, time.time(), devices, "遍历伙伴数量异常")
            except Exception as e:
                printred("遍历伙伴数量异常，详情见截图")
                printred(e)
                get_screen_shot(start, time.time(), devices, "遍历伙伴数量异常")
    else:
        printred("伙伴界面报错，详情见截图")
        get_screen_shot(start, time.time(), devices, "伙伴界面报错")
    return poco("Title").get_name()   # 返回值poco("Duck").get_name()

def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 0.88:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco("MenuSwitchBtn").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()


if __name__ == "__main__":
    start = time.localtime()
    monster(start, "9b57691d")