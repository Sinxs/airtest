from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

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
    if poco("ailin").exists() and not poco("AuctionDlg(Clone)").offspring("item9").offspring("ItemTpl").offspring("Name").exists():  # 如果选中框没有勾掉，他俩一起点击可以把所有的货物显示出来
        poco("AuctionDlg(Clone)").offspring("ItemLevel").child("Arrow").click()  # 仅显示当前可用
        poco("AuctionDlg(Clone)").offspring("ItemBlock").child("Arrow").click()  # 仅显示有货
    Type = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("1").child("Label").get_position()
    Selected = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("1").offspring("6").child("Selected").child(
        "P").get_position()
    name = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("1").child("Label")
    if Selected[1]-Type[1] < 0.08:  # 判断下拉框状态
        name.click()  # 点击装备
    for item in range(6, 9):
        item1 = str(item)
        poco(f"{item1}").click()
        for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
            item1 = "item" + str(item)
            if poco("AuctionDlg(Clone)").offspring(item1).exists():
                print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                    "Name").get_text() + "   道具显示正常")
    name.click()  # 点击装备用来恢复界面
    poco("AuctionDlg(Clone)").offspring("TypeList").offspring("2").child("Label").click()  # todo:点击龙器
    for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
        item1 = "item" + str(item)
        if poco("AuctionDlg(Clone)").offspring(item1).exists():
            print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                "Name").get_text() + "   道具显示正常")
    A = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("3").child("Label").get_position()
    B = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("3").offspring("Selected").child("P").get_position()
    if B[1] - A[1] < 0.08:  # 判断下拉框状态
        poco("AuctionDlg(Clone)").offspring("TypeList").offspring("3").child("Label").click()  # todo:点击纹章
    poco("AuctionDlg(Clone)").offspring("TypeList").offspring("3").offspring("Selected").child("P").click()
    for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
        item1 = "item" + str(item)
        if poco("AuctionDlg(Clone)").offspring(item1).exists():
            print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                "Name").get_text() + "   道具显示正常")
    poco("AuctionDlg(Clone)").offspring("TypeList").offspring("3").child("Label").click()  # todo:点击纹章恢复界面
    A = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("4").child("Label").get_position()
    B = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("4").offspring("Selected").child("P").get_position()
    if B[1] - A[1] < 0.08:  # 判断下拉框状态
        poco("AuctionDlg(Clone)").offspring("TypeList").offspring("4").child("Label").click()  # todo:金属板
    poco("AuctionDlg(Clone)").offspring("TypeList").offspring("4").offspring("Selected").child("P").click()
    for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
        item1 = "item" + str(item)
        if poco("AuctionDlg(Clone)").offspring(item1).exists():
            print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                "Name").get_text() + "   道具显示正常")
    poco("AuctionDlg(Clone)").offspring("TypeList").offspring("4").child("Label").click()  # todo:点击金属板恢复界面
    A = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("5").child("Label").get_position()
    B = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("5").offspring("22").child("Selected").child(
        "P").get_position()
    if B[1] - A[1] < 0.08:  # 判断下拉框状态
        poco("AuctionDlg(Clone)").offspring("TypeList").offspring("5").child("Label").click()  # todo:点击其他按钮
    A = ["22", "23", "26", "27", "28"]
    for i in A:
        # poco(f"{i}").click()
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
            poco(f"{i}").click()
            for item in range(10):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
                item1 = "item" + str(item)
                if poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").exists():
                    print(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                        "Name").get_text() + "   道具显示正常")
                else:
                    pass
    poco("AuctionDlg(Clone)").offspring("TypeList").offspring("5").child("Label").click()  # todo:点击恢复其他按钮
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
    if poco("Result").exists():  # 判断工会拍卖按钮是否存在
        poco("Result").click()
        if poco("AuctionDlg(Clone)").offspring("ResultWindow").child("Title").exists():  # 判断工会拍卖弹窗是否存在
            print(poco("AuctionDlg(Clone)").offspring("ResultWindow").child("Title").get_text() + "显示正确")
            poco(texture="l_close_00").click()  # 判断完成后点击返回
    poco("AuctionDlg(Clone)").offspring("Table").child("item1").child("Label").click()  # TODO:点击世界拍卖
    for item in range(6):
        item1 = "item" + str(item)
        if poco("AuctionDlg(Clone)").offspring("Table").child("item1").offspring(item1).child("Label").exists():
            print(poco("AuctionDlg(Clone)").offspring("Table").child("item1").offspring(item1).child("Label").get_text() + "显示正确")
    if poco("Result").exists():  # 判断世界拍卖是不是存在
        poco("Result").click()
        if poco("AuctionDlg(Clone)").offspring("ResultWindow").child("Title").exists():
            poco(texture="l_close_00").click()
            print(poco("AuctionDlg(Clone)").offspring("GuildAuc").child("SelectedTextLabel").get_text()+"界面显示正确")
    poco("AuctionDlg(Clone)").offspring("Buy").child("Selected").click()  # 点击我要购买
    poco("AuctionDlg(Clone)").offspring("ItemLevel").child("Arrow").click()  # 仅显示当前可用
    poco("AuctionDlg(Clone)").offspring("ItemBlock").child("Arrow").click()  # 点上，等于微瑕疵重置环境准备
    return poco("Title").get_text()



# def A(devices):
#     dev = connect_device("android:///" + devices)
#     poco = UnityPoco(device=dev)
#     print(poco("5").get_position())
#     poco("5").click()
#     poco("5").click()
#     print("点击第一次")
#     poco("5").click()
#     print("点击第二次")
# A(devices)