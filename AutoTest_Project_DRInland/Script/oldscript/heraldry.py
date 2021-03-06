"""
纹章模块
判断纹章模块中的界面元素-点击按钮
"""
from multi_processframe.ProjectTools import common, common, common
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


def addheraldry(start, poco,devices):
    poco("Btn").click()
    but = poco("EquipCreateDlg(Clone)").offspring("WrapContent").offspring(name="Icon")  # 是否存在金属板
    if but.exists():
        but.click()  # 点击金属板
        if poco("EquipCreateDlg(Clone)").offspring("Item").child("Icon").exists():  # 制作窗口是否存在金属板
            common.printgreen("开始进行纹章制作")
            poco("Create").click()  # 纹章制作
            if poco("EquipCreateDlg(Clone)").offspring("EquipSetCreateConfirmFrame").child("Bg").exists():  # 是否存在制作纹章的弹窗
                poco("OK").click()  # 点击确定按钮
                sleep(12)  # 制作过程中等待10秒
                if poco("Do").exists():  # 界面是否存在确定按钮
                    poco("Do").click()  # 点击确定
                    sleep(3)
                    poco("Close").click()  # 点击返回，返回到纹章界面
            else:
                common.printred("没有弹出金属板制作弹窗，请检查。。")
                common.get_screen_shot(start, time.time(), devices, "没有弹出金属板制作弹窗")
    else:
        if not but.exists():  # 如果界面不存在金属板
            poco("BtnMaterialAccess").click()  # 点击获取金属板
            if poco("ListPanel").exists():  # 存在获取途径
                poco("ListPanel").click()  # 点击bossrush进入bossrush界面
                if poco(text="当前挑战BOSS").exists():
                    common.printgreen("进入bossrush界面，进行bossrush判断")
                    if int(poco("BossRushNewDlg(Clone)").child("Num").get_text()[0]) != 0:
                        common.printgreen("进入bossrush副本")
                        poco("Go").click()  # 点击挑战
                        sleep(15)  # 等待15秒进入副本时间
                        dev = connect_device("android:///" + devices)
                        Androidpoco = AndroidUiautomationPoco(device=dev, use_airtest_input=True, screenshot_each_action=False)
                        if poco("Avatar").exists():  # 头像，准备进行GM指令获取金属板
                            poco("Avatar").click()  # 点击头像
                            text("gmwin")  # 输入gm命令直接结束战斗
                            sleep(1)
                            Androidpoco("android.widget.Button").click()
                            sleep(20)
                            if poco("BattleContinueDlg(Clone)").offspring("Continue").exists():
                                poco("BattleContinueDlg(Clone)").offspring("Continue").click()  # 点击奖励的确定按钮，副本打完会出现奖励弹窗
                                sleep(3)
                                poco("Continue").click()  # 返回主城
                                sleep(20)
                                if poco("ToolTip").exists():
                                    poco("Open").click()  # 点击使用金属板袋子
                                    sleep(2)
                                if poco("SysAItem").get_position()[0] > 1:
                                    poco(texture="halln_4").click()
                                    sleep(1)
                                poco("SysAItem").click()  # 点击角色按钮
                                if poco("Title").exists():
                                    common.printgreen("进入角色界面")
                                    if poco("XSys_Char_Emblem").exists():
                                        poco("XSys_Char_Emblem").click()  # 点击纹章
                                        if poco("ItemNewDlg(Clone)").offspring("Items").child("Frame").offspring(
                                                "T").exists():
                                            common.printgreen("进入金属板界面，开始进行纹章制作")
                                            # TODO：接下来进行纹章制作，纹章装备和卸下的操作已经完成
                                            addheraldry(start, poco,devices)  # 调用纹章制作
                    else:
                        common.printgreen("bossrush没有次数了，不打了")
                        poco("Close").click()  # 点击返回，返回到制作界面
                        poco("Close").click()  # 点击返回，返回到纹章界面


def heraldry(start, devices):
    poco = common.deviceconnect(devices)
    if poco("SysAItem").get_position()[0] > 1:
        poco(texture="halln_4").click()
        sleep(1)
    poco("SysAItem").click()  # 点击角色按钮
    if poco("Title").exists():
        common.printgreen("进入角色界面")
        if poco("XSys_Char_Emblem").exists():
            poco("XSys_Char_Emblem").click()  # 点击纹章
            if poco("ItemNewDlg(Clone)").offspring("Items").child("Frame").offspring("T").exists():
                common.printgreen("进入金属板界面，开始进行纹章制作")
                # TODO：接下来进行纹章制作，纹章装备和卸下的操作已经完成
                addheraldry(start, poco,devices)  # 调用纹章制作

                common.printgreen("进入纹章界面，开始测试纹章")
                if poco("ItemNewDlg(Clone)").offspring("Items").offspring("Icon").exists():
                    but = poco("ItemNewDlg(Clone)").offspring("Items").offspring(name="Icon")
                    if but.exists():
                        but.click()  # 点击第一个纹章
                    if poco("main").exists():  # 打开纹章装备界面
                        poco("Button1").click()  # 点击装备
                        common.get_screen_shot(start, time.time(), devices, "装备纹章截图验证")
                        but = poco("ItemNewDlg(Clone)").offspring(name="Icon")
                        if but.exists():
                            but.click()  # 点击已经装备的纹章
                            if poco("main").exists():
                                poco("Button1").click()  # 点击卸下
                    else:
                        common.printgreen("点击纹章后没有打开纹章装备界面")
                        common.get_screen_shot(start, time.time(), devices, "点击纹章后没有打开纹章装备界面")
                else:
                    common.printred("没有纹章")
                    common.get_screen_shot(start, time.time(), devices, "没有纹章")
        else:
            common.printred("没有进入角纹章界面，请检查。。")
            common.get_screen_shot(start, time.time(), devices, "没有进入角色")
    else:
        common.printred("没有进入角色，请检查。。")
        common.get_screen_shot(start, time.time(), devices, "没有进入角色")
    return poco("ItemNewDlg(Clone)").offspring("EmblemListPanel").child("Frame").offspring("T").get_text()  # 纹章



