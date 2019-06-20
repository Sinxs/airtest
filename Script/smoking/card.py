"""
图鉴模块-判断图鉴功能中的界面元素-进行按钮点击
"""
from multi_processframe.Tools import printcolor,adb_connect
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco


def card(devices):
    poco = adb_connect.device(devices)
    if poco("SysD_CardCollect").get_position()[0] > 1:
        poco(texture="halln_4").click()
        poco("SysD_CardCollect").click()
    else:
        printcolor.printgreen("界面上就有图鉴按钮")
        poco("SysD_CardCollect").click()
    if poco("DeckPanel").exists():
        for item in range(len(poco("DeckPanel").child())):
            item1 = "item"+str(item)
            poco("CardCollectDlg(Clone)").offspring("Deck").offspring("DeckPanel").child(item1).click()
            if poco("CardCollectDlg(Clone)").offspring("Deck").offspring("DeckPanel").child(item1).offspring("Name").get_text() == poco("Title").get_text():
                printcolor.printgreen("图鉴-->>  "+poco("Title").get_text()+"  界面显示正确")
                freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                for item in range(len(freeze_poco("WrapContent").child())):
                    item1 = "item"+str(item)
                    but = freeze_poco("CardCollectDlg(Clone)").offspring("Deck").offspring("WrapContent").child(item1).child("Name").get_text()
                    printcolor.printgreen("检查点-->>  " + but + "  显示正确")
        if poco("OpenCardList").exists():
            poco("OpenCardList").click()
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            for Quality in range(1,len(freeze_poco("Panel").child())+1):
                Quality1 = "Quality" + str(Quality)
                if freeze_poco(Quality1).exists():
                    for item in range(len(freeze_poco(Quality1).child("item").child())):
                        item1 = "item" + str(item)
                        if freeze_poco("CardCollectDlg(Clone)").offspring("CardList").offspring(Quality1).offspring(item1).child("Icon").exists():
                            pass
                    printcolor.printgreen("检查点-->> 图鉴显示  界面显示正确\n接下来点击图鉴分解")
                    poco("AutoResolve").click()  # 图片分解
                    if poco("GreyModalDlg(Clone)").child("Bg").child("Label").exists():
                        printcolor.printgreen("检查点-->>"+poco("GreyModalDlg(Clone)").child("Bg").child("Label").get_text()+" 界面显示正确")
                        poco("OK").click()  # 点击确认分解图鉴
                        if poco(text="分 解").exists():
                            printcolor.printgreen("检查点-->>" + poco(text="分 解").get_text() + " 界面显示正确")
                            poco("Cancel").click()  # 点击返回
                            poco(texture="l_close_00").click()  # 点击返回
                    else:
                        if poco(text="分 解").exists():
                            printcolor.printgreen("检查点-->>" + poco(text="分 解").get_text() + " 界面显示正确")
                            poco("Cancel").click()  # 点击返回
                            poco(texture="l_close_00").click()  # 点击返回
                    if poco("OpenShop").exists():  # 图鉴兑换
                        poco("OpenShop").click()
                        freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
                        if freeze_poco("Sprite").exists():
                            printcolor.printgreen("进入图鉴兑换界面，开始检查界面元素")
                            for item in range(len(freeze_poco("ShopPanel").child())):
                                item1 = "item" + str(item)
                                icon = freeze_poco("CardCollectDlg(Clone)").offspring("Shop").offspring(item1).child("Item").child("Name").get_text()
                                printcolor.printgreen(f"兑换图鉴 {icon} 显示正确")


    else:
        printcolor.printred("没有进入图鉴界面，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "没有进入图鉴界面")
    return poco("CardCollectDlg(Clone)").offspring("Shop").offspring("Title").get_text()  # 兑 换



