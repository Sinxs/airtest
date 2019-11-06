"""
交易所
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from multi_processframe.ProjectTools import common


def auction(poco):
    for item in range(0):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
        item1 = "item" + str(item)
        if poco("AuctionDlg(Clone)").offspring(item1).exists():
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            common.printgreen(freeze_poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
                "Name").get_text() + "   道具显示正常")


def Auction(devices):  # 点击交易所按钮
    """
    点击交易所按钮，进入交易所界面
    :param devices:移动设备端口号，用于识别设备
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)  # 链接设备，并且重置poco
    poco("SysCAuction").click()  # 点击交易所
    poco("AuctionDlg(Clone)").offspring("DragonCoin").child("SelectedTextLabel").click()  # 点击龙币交易所
    freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    if freeze_poco("ailin").exists() and not poco("AuctionDlg(Clone)").offspring("item9").offspring(
            "ItemTpl").offspring("Name").exists():  # 如果选中框没有勾掉，他俩一起点击可以把所有的货物显示出来
        poco("AuctionDlg(Clone)").offspring("ItemLevel").child("Arrow").click()  # 仅显示当前可用
        poco("AuctionDlg(Clone)").offspring("ItemBlock").child("Arrow").click()  # 仅显示有货
    for off in freeze_poco("AuctionDlg(Clone)").offspring("TypeList").offspring("Label"):
        common.printgreen(f"检查点《{off.get_text()}》存在")
    # 以下是用来点击每个小选项
    # Type = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("1").child("Label").get_position()
    # Selected = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("1").offspring("6").child("Selected").child(
    #     "P").get_position()
    # name = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("1").child("Label")
    # if Selected[1] - Type[1] < 0.06:  # 判断下拉框状态
    #     name.click()  # 点击装备
    # for item in range(6, 9):
    #     item1 = str(item)
    #     poco(f"{item1}").click()
    # auction(poco)
    # name.click()  # 点击装备用来恢复界面
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("2").child("Label").click()  # todo:点击龙器
    # auction(poco)
    # A = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("3").child("Label").get_position()
    # B = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("3").offspring("Selected").child("P").get_position()
    # if B[1] - A[1] < 0.06:  # 判断下拉框状态
    #     poco("AuctionDlg(Clone)").offspring("TypeList").offspring("3").child("Label").click()  # todo:点击纹章
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("3").offspring("Selected").child("P").click()
    # auction(poco)
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("3").child("Label").click()  # todo:点击纹章恢复界面
    # A = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("4").child("Label").get_position()
    # B = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("4").offspring("Selected").child("P").get_position()
    # if B[1] - A[1] < 0.06:  # 判断下拉框状态
    #     poco("AuctionDlg(Clone)").offspring("TypeList").offspring("4").child("Label").click()  # todo:金属板
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("4").offspring("Selected").child("P").click()
    # auction(poco)
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("4").child("Label").click()  # todo:点击金属板恢复界面
    # A = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("5").child("Label").get_position()
    # B = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("5").offspring("22").child("Selected").child(
    #     "P").get_position()
    # if B[1] - A[1] < 0.06:  # 判断下拉框状态
    #     poco("AuctionDlg(Clone)").offspring("TypeList").offspring("5").child("Label").click()  # todo:点击其他按钮
    # A = ["22", "23", "26", "27", "28"]
    # for i in A:
    #     # poco(f"{i}").click()
    #     if poco(f"{i}").exists():
    #         for ii in range(10):
    #             pos = poco(f"{i}").get_position()
    #             if pos[1] < 0.28:
    #                 common.setswipe(1, [319, 256], [319, 577], devices)
    #             elif pos[1] > 0.87:
    #                 common.setswipe(1, [319, 577], [319, 256], devices)
    #             else:
    #                 break
    #         poco(f"{i}").click()
    #         for item in range(0):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
    #             item1 = "item" + str(item)
    #             if poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").exists():
    #                 common.printgreen(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
    #                     "Name").get_text() + "   道具显示正常")
    #             else:
    #                 pass
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("5").child("Label").click()  # todo:点击恢复其他按钮
    # poco("9").click()  # todo:点击菜肴按钮
    # for item in range(0):  # 因为apk功能机制问题，所以只选择前10中商品进行抽样测试
    #     item1 = "item" + str(item)
    #     if poco("AuctionDlg(Clone)").offspring(item1).exists():
    #         common.printgreen(poco("AuctionDlg(Clone)").offspring(item1).offspring("ItemTpl").offspring(
    #             "Name").get_text() + "   道具显示存在")

    poco("AuctionDlg(Clone)").offspring("Crystal").child("SelectedTextLabel").click()  # TODO：点击水晶交易所
    if poco("ailin").exists() and not poco("AuctionDlg(Clone)").offspring("item9").offspring("ItemTpl").offspring(
            "Name").exists():  # 如果选中框没有勾掉，他俩一起点击可以把所有的货物显示出来
        poco("AuctionDlg(Clone)").offspring("ItemLevel").child("Arrow").click()  # 仅显示当前可用
        poco("AuctionDlg(Clone)").offspring("ItemBlock").child("Arrow").click()  # 仅显示有货
    for off in freeze_poco("AuctionDlg(Clone)").offspring("TypeList").offspring("Label"):
        common.printgreen(f"检查点《{off.get_text()}》存在")
    # A = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("30").child("Label").get_position()
    # B = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("30").offspring("31").child("Label").get_position()
    # if B[1] - A[1] < 0.06:  # 判断下拉框状态
    #     poco("AuctionDlg(Clone)").offspring("TypeList").offspring("30").child("Label").click()  # TODO：点击装备
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("30").offspring("31").child("Label").click()
    # auction(poco)
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("30").child("Label").click()  # TODO：点击恢复装备
    #
    # A = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("40").child("Label").get_position()
    # B = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("40").offspring("41").child("Label").get_position()
    # if B[1] - A[1] < 0.06:  # 判断下拉框状态
    #     poco("AuctionDlg(Clone)").offspring("TypeList").offspring("40").child("Label").click()  # TODO：点击家园
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("40").offspring("41").child("Label").click()  # 点击作物
    # auction(poco)
    #
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("40").offspring("42").child("Label").click()  # 点击料理
    # auction(poco)
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("40").child("Label").click()  # TODO：点击恢复家园
    #
    # A = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("50").child("Label").get_position()
    # B = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("50").offspring("29").child("Label").get_position()
    # if B[1] - A[1] < 0.06:  # 判断下拉框状态
    #     poco("AuctionDlg(Clone)").offspring("TypeList").offspring("50").child("Label").click()  # TODO：点击其他
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("50").offspring("29").child("Label").click()  # 点击活动礼包
    # auction(poco)
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("50").offspring("51").child("Label").click()  # 点击三件套时装
    # auction(poco)
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("50").offspring("52").child("Label").click()  # 点击坐骑
    # auction(poco)
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("50").child("Label").click()  # TODO：点击恢复其他
    #
    # A = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("60").child("Label").get_position()
    # B = poco("AuctionDlg(Clone)").offspring("TypeList").offspring("60").offspring("61").child("Label").get_position()
    # if B[1] - A[1] < 0.06:  # 判断下拉框状态
    #     poco("AuctionDlg(Clone)").offspring("TypeList").offspring("60").child("Label").click()  # TODO：点击纹章
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("60").offspring("61").child("Label").click()  # 点击金属板
    # auction(poco)
    #
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("60").offspring("62").child("Label")  # 点击属性纹章
    # auction(poco)
    # poco("AuctionDlg(Clone)").offspring("TypeList").offspring("60").child("Label").click()  # TODO：点击恢复纹章

    poco("AuctionDlg(Clone)").offspring("Sell").child("SelectedTextLabel").click()  # TODO:点击我要出售
    if poco("ailin").exists() and poco("Tip").exists() and poco(texture="l_frame_01").exists():
        common.printgreen(
            poco("AuctionDlg(Clone)").offspring("Sell").child("SelectedTextLabel").get_text() + "   界面显示正确")
        # 以下为出售道具
        if poco("AuctionDlg(Clone)").offspring("item0").child("Icon").exists():
            poco("AuctionDlg(Clone)").offspring("item0").child("Icon").click()
            common.printgreen("准备上架   " + poco("ItemTpl").child("Name").get_text())
            if poco("AuctionBillFrame(Clone)").child("Bg").exists():
                poco("RightButton").click()
                common.printgreen(poco("AuctionDlg(Clone)").offspring("item0").offspring("ItemTpl").offspring(
                    "Name").get_text() + "上架成功---测试完成，准备下架")
        if poco("AuctionDlg(Clone)").offspring("item0").offspring("ItemTpl").offspring("Name").exists():
            poco("AuctionDlg(Clone)").offspring("item0").offspring("ItemTpl").offspring("Name").click()
            if poco("LeftButton").exists():  # 点击商品下架
                common.printgreen(
                    "准备下架---" + poco("AuctionDlg(Clone)").offspring("item0").offspring("ItemTpl").offspring(
                        "Name").get_text())
                poco("LeftButton").click()
                common.printgreen("下架成功")
                if poco("SellListEmpty").exists():
                    common.printgreen("上架下架测试完成")
        else:
            common.printgreen("没有道具可以出售....")
    poco("AuctionDlg(Clone)").offspring("GuildAuc").child("SelectedTextLabel").click()  # TODO:点击拍卖行
    # 以下是为了省时间才做的
    freeze_poco = poco.freeze()  # TODO：定义冻结poco
    for off in freeze_poco("AuctionDlg(Clone)").offspring("Table").offspring("Label"):
        common.printgreen(f"检查点 《{off.get_text()}》 存在")
    # poco("AuctionDlg(Clone)").offspring("Table").child("item0").child("Label").click()  # TODO:点击工会拍卖
    # if poco("Result").exists():  # 判断工会拍卖按钮是否存在
    #     poco("Result").click()
    #     if poco("AuctionDlg(Clone)").offspring("ResultWindow").child("Title").exists():  # 判断工会拍卖弹窗是否存在
    #         common.printgreen(poco("AuctionDlg(Clone)").offspring("ResultWindow").child("Title").get_text() + "  显示正确")
    #         poco(texture="l_close_00").click()  # 判断完成后点击返回
    # A = poco("AuctionDlg(Clone)").offspring("Table").child("item1").child("Label").get_position()  # TODO:点击世界拍卖
    # B = poco("AuctionDlg(Clone)").offspring("Table").child("item1").offspring("item0").child("Label").get_position()
    # if A[1] - B[1] < 0.6:
    #     poco("AuctionDlg(Clone)").offspring("Table").child("item1").child("Label").click()
    # freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    # for item in range(8):
    #     item1 = "item" + str(item)
    #     if freeze_poco("AuctionDlg(Clone)").offspring("Table").child("item1").offspring(item1).child("Label").exists():
    #         common.printgreen(freeze_poco("AuctionDlg(Clone)").offspring("Table").child("item1").offspring(item1).child(
    #             "Label").get_text() + "  显示正确")
    # if poco("Result").exists():  # 判断世界拍卖是不是存在
    #     poco("Result").click()
    #     freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
    #     if freeze_poco("AuctionDlg(Clone)").offspring("ResultWindow").child("Title").exists():
    #         freeze_poco(texture="l_close_00").click()
    #         common.printgreen(
    #             freeze_poco("AuctionDlg(Clone)").offspring("GuildAuc").child("SelectedTextLabel")
    #             .get_text() + "  界面显示正确")
    poco("AuctionDlg(Clone)").offspring("DragonCoin").child("SelectedTextLabel").click()  # 点击龙币交易所
    poco("AuctionDlg(Clone)").offspring("ItemLevel").child("Arrow").click()  # 仅显示当前可用
    poco("AuctionDlg(Clone)").offspring("ItemBlock").child("Arrow").click()  # 点上，为下次重置环境准备
    return poco("t2").get_text()  # 商品购买后绑定


if __name__ == "__main__":
    start = time.localtime()
    Auction("e37c0280")
