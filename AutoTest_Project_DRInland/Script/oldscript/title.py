"""
称号模块
检查所有称号
"""
from multi_processframe.ProjectTools import common,common,common
from airtest.core.api import *

def title(start,devices):
    poco = common.deviceconnect(devices)
    if poco("SysAItem").get_position()[0] > 1:
        poco(texture="halln_4").click()
        sleep(1)
    poco("SysAItem").click()  # 点击角色按钮
    if poco("Title").exists():
        common.printgreen("进入角色界面")
        if poco("XSys_Design_Designation").exists():
            poco("XSys_Design_Designation").click()  # 点击称号
            if poco(text="日常称号").exists():
                common.printgreen("进入称号界面，开始检测称号。。。")
                for i in range(1, 7):
                    for Label in poco("ItemNewDlg(Clone)").offspring(str(i)).child("ChildList").offspring("Label"):
                        Label.click()
                        freeze_poco = poco.freeze()  # TODO：定义冻结poco
                        for ii in range(len(freeze_poco("WrapContent").child())):
                            title = freeze_poco("ItemNewDlg(Clone)").offspring(f"item{ii}").offspring("Animation")
                            if title.exists():  # 判断称号存在
                                pass
                            else:
                                if "fff" in title:
                                    print(freeze_poco("ItemNewDlg(Clone)").offspring(f"item{ii}").offspring( "Animation").get_text() + "称号显示错误")
                                else:
                                    print("图片称号显示错误")
                                    common.get_screen_shot(start,time.time(), devices, "没有进入角色界面")
                    poco("ItemNewDlg(Clone)").offspring(str(i)).child("Bg").click()
                common.printgreen("称号检测完毕。。。没有发现异常")
    else:
        common.printred("没有进入角色界面，请检查")
        common.get_screen_shot(start,time.time(), devices, "没有进入角色界面")
    return poco(text="[fff7b4]钓鱼大师").get_text()  # [fff7b4]钓鱼大师