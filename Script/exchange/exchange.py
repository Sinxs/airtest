from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
devices = "127.0.0.1:62001"  # todo:需要传入的设备号,等完善脚本后需要放在配置文件中，
def Auction(devices):  # 点击交易所按钮
    """
    点击交易所按钮，进入交易所界面
    :param devices:移动设备端口号，用于识别设备
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)  # 链接设备，并且重置poco
    poco("SysCAuction").click()  # 点击交易所
    poco("AuctionDlg(Clone)").offspring("Buy").child("Selected").click()  # 点击我要购买
    poco("AuctionDlg(Clone)").offspring("ItemLevel").child("Arrow").click()  # 仅显示当前可用
    poco("AuctionDlg(Clone)").offspring("ItemBlock").child("Arrow").click()  # 仅显示有货，他俩一起点击可以把几乎所有的货物显示出来
    name = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("1").child("Label")
    name.click()  # 点击装备
    for item in range(6,9):
        item1 = str(item)
        poco(f"{item1}").click()
        for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
            item1 = "item" + str(item)
            if poco("AuctionDlg(Clone)").offspring(item1).exists():
                print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                    "Name").get_text() + "   道具显示正常")
    name.click()  # 点击装备用来恢复界面
    poco("2").click()  # todo:点击龙器
    for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
        item1 = "item" + str(item)
        if poco("AuctionDlg(Clone)").offspring(item1).exists():
            print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                "Name").get_text() + "   道具显示正常")

    poco("3").click()  # todo:点击纹章
    for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
        item1 = "item" + str(item)
        if poco("AuctionDlg(Clone)").offspring(item1).exists():
            print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                "Name").get_text() + "   道具显示正常")
    poco("3").click()  # todo:点击纹章恢复界面
    poco("4").click()
    for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
        item1 = "item" + str(item)
        if poco("AuctionDlg(Clone)").offspring(item1).exists():
            print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                "Name").get_text() + "   道具显示正常")
    poco("5").click()  # todo:点击其他按钮
    A = ["22", "23", "26", "27", "28"]
    for i in A:
        poco(f"{i}").click()
        if poco(f"{i}").exists():
            for ii in range(5):
                pos = poco(f"{i}").get_position()
                if pos[1] < 0.28:
                    swipe([686, 580], [686, 870], 5)
                else:
                    break
            for ii in range(5):
                pos = poco(f"{i}").get_position()
                if pos[1] > 0.8:
                    swipe([686, 870], [686, 580], 5)
                    break
            for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
                item1 = "item" + str(item)
                if poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").exists():
                    print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                        "Name").get_text() + "   道具显示存在")
                else:
                    pass

    poco("9").click()  # todo:点击菜肴按钮
    for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
        item1 = "item" + str(item)
        if poco("AuctionDlg(Clone)").offspring(item1).exists():
            print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                "Name").get_text() + "   道具显示存在")
    poco("AuctionDlg(Clone)").offspring("Sell").child("SelectedTextLabel").click()  # TODO:点击我要出售
    if poco("ailin").exists() and poco("t").exists() and poco("AuctionSellFrame").child("Title ").exists():
        print(poco("AuctionDlg(Clone)").offspring("Sell").child("SelectedTextLabel").get_text() + "界面显示正确")


    poco("AuctionDlg(Clone)").offspring("GuildAuc").child("SelectedTextLabel").click()  # TODO:点击拍卖行
    poco("AuctionDlg(Clone)").offspring("Table").child("item0").child("Label").click()  # TODO:点击工会拍卖
    poco("AuctionDlg(Clone)").offspring("Table").child("item1").child("Label").click()  # TODO:点击世界拍卖
    for item in range(6):
        item1 = "item" + str(item)
        if poco("AuctionDlg(Clone)").offspring("Table").child("item1").offspring(item1).child("Label").exists():
            pass
    print(poco("AuctionDlg(Clone)").offspring("GuildAuc").child("SelectedTextLabel").get_text()+"界面显示正确")






# devices = "127.0.0.1:62001"  # todo:需要传入的设备号,等完善脚本后需要放在配置文件中，
Auction(devices)  # 点击交易所按钮
