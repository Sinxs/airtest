from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
Androidpoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
devicces = "127.0.0.1:62001"

def addgm(poco,item1):
    GM_gad = "1321001"  # GM获取纹章
    GM_Longqi = "3128"  # GM获取龙器碎片
    if poco("Open").exists():
        poco("Open").click()
        poco(text=">").click()
        text(f"item {GM_gad} 1")  # GM获取纹章
        Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮
        poco(text=">").click()
        text(f"item {GM_Longqi} 160")  # GM获取龙器碎片
        Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮
        poco(text=">").click()
        text(f"item 1 9999999")  # GM获金币
        Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮

        poco(text=">").click()
        text("clearbag 0")  # 删除已经获取到的所有道具
        Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮

        for i in str(range(0, 10)):  # 增加装备
            poco(text=">").click()
            text(f"item 9360{i} 1")  # GM获取装备
            Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮
        poco("Close").click()  # 取消GM窗口
        poco("Avatar").click()
        poco("Close").click()  # 取消GM选项
    else:
        poco("Avatar").click()
        text(f"item {GM_gad} 1")  # GM获取纹章
        Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮
        poco("SettingDlg(Clone)").offspring("Close").click()  # 点击返回
        poco(text=">").click()
        text(f"item {GM_Longqi} 160")  # GM获取龙器碎片
        Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮
        poco(text=">").click()
        text(f"item 1 9999999")  # GM获金币
        Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮
        for i in range(0, 10):  # 增加装备
            item = "9360" + str(i)
            poco(text=">").click()
            text(f"item {item} 1")  # GM获金币
            Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮
        for i in range(6, 9):  # 增加升级石
            item = "108" + str(i)
            poco(text=">").click()
            text(f"item {item} 100")  # GM获金币
            Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮
        poco("Close").click()  # 取消GM窗口
        poco("Avatar").click()
        poco("Close").click()  # 取消GM选项

    SysAItem = poco("SysAItem")  # 选择角色按钮
    AItempos = SysAItem.get_position()
    if AItempos[0] > 1:
        print("当前界面没有技能按钮，点击 + 号")
        poco(texture="switch").click()  # 点击+号
        if poco("SysAItem").exists():
            poco("SysAItem").click()  # 点击角色按钮
            poco("ItemNewDlg(Clone)").offspring("XSys_Item_Equip").child("Bg").click()  # 点击装备按钮
    else:
        print("当前界面就有角色按钮")
        if poco("SysAItem").exists():
            poco("SysAItem").click()  # 点击角色按钮
            poco("ItemNewDlg(Clone)").offspring("XSys_Item_Equip").child("Bg").click()  # 点击装备按钮

    for i in range(0, 10):  # 穿戴装备
        item = "9360" + str(i)
        if poco(f"equip{item}").exists():
            poco(f"equip{item}").click()
            poco("Button6").click()  # 点击鉴定
        if poco("GreyModalDlg(Clone)").child("Bg").exists():
            poco("OK").click()
        else:
            print("没有弹出鉴定弹窗....检查一下吧，不应该啊...可能是没有这件装备")

        if poco(f"equip{item1}{item}").exists():
            poco(f"equip{item1}{item}").click()  # 点击穿戴
        elif poco(f"equip10{item1}{item}").exists():
            poco(f"equip10{item1}{item}").click()  # 点击穿戴# 点击穿戴
            print("出现稀有的装备了....神烦...该怎么办呢？？？？")
        else:
            print("找不到装备")
        if poco("main").exists():  # 点击穿戴
            poco("Button1").click()
            # TODO：：穿戴装备的时候会弹出一个警告弹窗，需要进行判断................................................
            if poco("ItemBlock").exists():  # 更换装备可能会弹出一个警告框，需要点掉
                poco(texture="l_button_05").click()  # 点击不在提示
                poco("Close").click()  # 点击返回，以消掉弹窗
        else:
            print("没有弹出穿戴弹窗....检查一下吧，不应该啊...")

    poco("Close").click()  # 返回到主界面


def manufacture(poco, item1):
    addgm(poco,item1)  # TODO 前置测试环境，增加需要使用的道具
    SysAItem = poco("SysDEquipCreate")
    AItempos = SysAItem.get_position()
    if AItempos[0] > 1:
        print("当前界面没有制作按钮，点击 + 号")
        poco(texture="switch").click()  # 点击+号
        if poco("SysDEquipCreate").exists():
            poco("SysDEquipCreate").click()

    else:
        print("当前界面制作按钮存在")
        poco("SysDEquipCreate").click()
    poco("XSys_EquipCreate_EmblemSet").click()  # 点击纹章制作
    if poco("1321001").exists():
        poco("1321001").click()
        poco("Create").click()
        if poco("EquipCreateDlg(Clone)").offspring("EquipSetCreateConfirmFrame").child("Bg").exists():
            poco("OK").click()
            sleep(6)
            poco("Do").click()
            print("纹章制作测试完成...")
    else:
        print("没有可以制作的金属片")

    if poco("EquipCreateDlg(Clone)").offspring("XSys_EquipCreate_ArtifactSet").child("Bg").exists():  # 点击龙器制作
        poco("EquipCreateDlg(Clone)").offspring("XSys_EquipCreate_ArtifactSet").child("Bg").click()
        for item in range(0, 8):
            for i in range(5):
                item1 = poco("EquipCreateDlg(Clone)").offspring(f"{item}").offspring("Selected").get_position()
                if item1[1] < 0.34:
                    swipe((700, 500), (700, 900))
                elif item1[1] > 0.91:
                    swipe((700, 900), (700, 500))
                else:
                    break
            poco("EquipCreateDlg(Clone)").offspring(f"{item}").offspring("Selected").child("P").click()  # 点击选择龙器
            poco("EquipCreateDlg(Clone)").offspring("0").child("Create").click()  # 点击制作龙器
            if poco("EquipCreateDlg(Clone)").offspring("EquipSetCreateConfirmFrame").child("Bg").exists():
                poco("OK").click()  # 点击确定
                sleep(10)
                if poco("Text").exists():
                    print(f"第{item+1}件龙器制作完成")
                    poco("Do").click()
        print(f"一共8种属性，每种属性一件龙器，全部制作完成")
    else:
        print("龙器制作按钮未找到，请检查....")

    # 以下是装备升级测试
    poco("EquipCreateDlg(Clone)").offspring("XSys_EquipCreate_Upgrade").offspring("SelectedTextLabel").click()
    poco("红龙套装").click()  # 点击红龙套装
    for i in range(7, 11):  # 升级三件套装首饰
        item3 = str(i)
        poco("193607").child("Create")
        if poco(f"{item1}9360{item3}").child("Create").exists():
            poco(f"{item1}9360{item3}").child("Create").click()
        elif poco(f"10{item1}9360{item3}").child("Create").exists():
            poco(f"10{item1}9360{item3}").child("Create").click()  # 点击制造
            print("稀有的装备能制造出什么呢？？敬请期待...")
        else:
            print("找不到装备")
        if poco("EquipmentUpgradeWindow(Clone)").child("Bg").exists():
            poco("OK").click()
            sleep(10)
            if poco("Text").exists():
                print(f"19360{item3}制作成功")
                poco("Do").click()
        else:
            print(f"19360{item3}装备找不到...")
    for i in range(7):  # 升级三件套装首饰
        item3 = str(i)
        if poco(f"19360{item3}").child("Create").exists():
            poco(f"19360{item3}").child("Create").click()
            if poco("EquipmentUpgradeWindow(Clone)").child("Bg").exists():
                poco("OK").click()
                sleep(10)
                if poco("Text").exists():
                    poco("Do").click()
            else:
                print("没有弹出升级弹窗，不应该啊....检查一下吧")
        else:
            print("没有可以升级的装备，检查一下吧")


def start(devicces):
    dev = connect_device("android:///" + devicces)
    poco = UnityPoco(device=dev)
    for item2 in range(1, 8):  # 切换职业角色
        for i in range(5):
            if poco("SettingDlg(Clone)").offspring("Close").exists():
                poco("SettingDlg(Clone)").offspring("Close").click()
            elif poco("Close").exists():
                poco("Close").click()
            else:
                break
        poco("Avatar").click()
        if Androidpoco("android.widget.Button").exists():
            Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮
        poco(text="切换角色").click()
        sleep(20)
        poco(f"Prof{item2}").click()
        sleep(2)
        if poco("EnterGame").exists():
            poco("EnterGame").click()
            sleep(35)
        for i in range(5):
            if poco("Close").exists():
                poco("Close").click()
            else:
                break
        manufacture(poco, item2)
        for i in range(5):
            poco("Close").click()
        poco("Avatar").click()
        if Androidpoco("android.widget.Button").exists():
            Androidpoco("android.widget.Button").click()  # 点击GM窗口的确定按钮
        poco(text="切换角色").click()
        sleep(20)

start(devicces)

# def A(devicces):
#     dev = connect_device("android:///" + devicces)
#     poco = UnityPoco(device=dev)
#     for item in range(0, 8):
#         for i in range(5):
#             item1 = poco("EquipCreateDlg(Clone)").offspring(f"{item}").offspring("Selected").get_position()
#             print(item)
#             if item1[1] < 0.34:
#                 swipe((700, 500), (700, 900))
#             elif item1[1] > 0.91:
#                 swipe((700, 900), (700, 500))
#             else:
#                 break
#
# A(devicces)