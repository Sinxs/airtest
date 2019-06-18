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
    else:
        printcolor.printred("没有进入图鉴界面，请检查...")
    return poco("Title").get_text()



