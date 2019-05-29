# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
import time
devices = "127.0.0.1:62001"
print("start...")

# 启动游戏
# Startgame.test_Start()
def test_SignInReward(devices):
    """1.每天第一次登陆弹出签到窗口进行签到
       2.第一次登陆的时候没有签到，就到福利中去签到
    """

    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("Check").exists() and poco("RedPoint").exists():  # 判断签到状态，有红点就是还没签到
        poco("Check").click()  # 点击签到
        print("签到成功!")

    else:
        poco("SysGWelfare").click()
        poco("WelfareDlg(Clone)").offspring("item4").click()
        if poco("RedPoint").exists():
            poco("Check").click()
            print("签到成功!")
        else:
            print("已经完成签到，未使用签到方法签到!")
    return "1"

def test_Close(poco):
    """界面关闭操作----通用函数
    """
    poco("Close").click()
    print("关闭窗口")
    return "1"

def test_sysPromote(devices):  # 提升
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("SysAAFPromote").exists():
        poco("SysAAFPromote").click()
        print("提升按钮点击正常")
    else:
        print("暂时没有可提升项目")
    return "1"
  # 变强
def test_SysStrengthen(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    poco("SysIBq").click()
    print("变强界面打开成功！")
    return "1"

# 奖励
def test_SysAward(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    poco("SysEReward").click()
    poco("XSys_Design_Achieve").click()
    poco("XSys_Reward_Target").click()
    poco("XSys_LevelReward").click()
    poco("XSys_WeekShareReward").click()
    poco("XSys_Reward_Dragon").click()
    print("奖励界面打开成功！")
    return "1"

# 交易所
def test_SysAuction(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    poco("SysCAuction").click()
    poco("AuctionDlg(Clone)").offspring("Sell").child("SelectedTextLabel").click()
    poco("AuctionDlg(Clone)").offspring("GuildAuc").child("SelectedTextLabel").click()
    print("交易所打开成功！")
    return "1"




# 商城
def test_SysGameMall(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    poco("SysAGameMall").click()
    '''
    进入钻石商店
    '''
    poco("XSys_GameMall_Diamond").click() # 钻石商城
    poco("GameMall(Clone)").offspring("TabsFrame").child("item1").click() # 点击装备页签
    diamondago = poco("TitanFrame").offspring("item0").child("value").get_text()  # 获取钻石数量
    poco("GameMall(Clone)").offspring("item0").child("item2").click()  # 确认商品
    name = poco("GameMall(Clone)").offspring("item0").child("item2").child("Name").get_text()  # 获取商品名称
    price = poco("GameMall(Clone)").offspring("item0").child("item2").child("Price").get_text()  # 获取商品价格
    print(f'购买钻石商品-{name}-价格：{price}',end=' ')
    poco("OK").click()  # 点击购买
    poco(texture="l_button_00").click()  # 确认购买
    diamondnew = poco("TitanFrame").offspring("item0").child("value").get_text()
    if int(price) == int(diamondago) - int(diamondnew):
        print("商品购买成功")
    elif int(price) != int(diamondago) - int(diamondnew):
        print("商品扣除价格错误")
    else:
        print("商品购买失败，请确认货币以及存货是否充足！！！")
    '''
     进入龙币商店
    '''
    poco("XSys_GameMall_Dragon").click()
    poco("GameMall(Clone)").offspring("TabsFrame").child("item1").click()  # 点击装备页签
    poco("GameMall(Clone)").offspring("item0").child("item2").click()
    name = poco("GameMall(Clone)").offspring("item0").child("item2").child("Name").get_text()
    print(f'购买龙币商品-{name}')
    poco("OK").click()  # 点击购买
    poco(texture="l_button_00").click()  # 确认购买
    '''
    进入系统商店
    '''
    poco("XSys_Mall").click()
    shopname = poco("item0").offspring(name="shopname").get_text()
    poco("GameMall(Clone)").offspring("ShopFrame").offspring("item0").click() # 进入子页商店
    entershopname = poco("ShopName").get_text()
    if shopname == entershopname:
        print(f"{shopname}进入成功")
        poco("Close").click()
    else:
        print(f"点击{shopname}进入了{entershopname},请检查商店链接是否正常！！")
        poco("Close").click()
    '''
    进入充值界面
    '''
    poco("XSys_GameMall_Pay").click()
    poco("GameMall(Clone)").offspring("DiamondFrame").offspring("item1").child("Price").click()
    time.sleep(2)
    systip = poco("SystemTip(Clone)").offspring("item0").child("Text").get_text()
    print(f"点击充值按钮获取的系统消息是：{systip[8:]}--ps：点击不闪退，有反应测试就通过")
    result = poco("CustomerService").get_name()
    return result

# test_SysGameMall(devices)

# 极限龙本
def test_SysLimitDragon(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("SysLimitDragon").exists():
        poco("SysLimitDragon").click()
        print("活动时间内，极限龙本打开正常！")
        sleep(2)
        touch([62, 44])  # 因为极限龙本的返回坐标无法确定，所以使用坐标
        print("关闭窗口")
    else:
        print("极限龙本不在时间内，无法进入功能！")
        sleep(2)
        touch([62, 44])  # 同上
        print("关闭窗口")
    return "1"

# 登陆奖励
def test_SysSevenActivity(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("SysISevenActivity").exists():
        poco("SysISevenActivity").click()
        for item in range(8):
            item1 = "WrapItem_" + str(item)
            if poco("SevenAwardDlg(Clone)").offspring(f"WrapItem_{item1}").offspring("Label").exists():
                poco("SevenAwardDlg(Clone)").offspring(f"WrapItem_{item1}").offspring("Label").click()

        print("七日登陆活动打开正常")
    else:
        print("七日登陆签到已经全部完成！")
    return "1"
# 观看
def test_SysLive(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    poco("SysG_Live").click()
    poco("SpectateDlg(Clone)").offspring("1").child("Bg").click()
    print("观战窗口打开正常！")
    return "1"
# 精彩活动
def test_SysOperatingActivity(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    poco("SysEOperatingActivity").click()
    for item in range(5):
        item1 = "item" + str(item)
        poco("OperatingActivityDlg(Clone)").offspring(item1).click()
    print("精彩活动打开正常！")
    return "1"
# 首冲
def test_SysFirstRecharge(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("SysCFirstRecharge").exists():
        poco("SysCFirstRecharge").click()
        print("首冲未充值，界面打开正常")
    else:
        print("首冲完成，入口消失")
    return "1"
# 开服狂欢
def test_SysCarnival(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("SysACarnival").exists():
        poco("SysACarnival").click()
        print("开服狂欢界面打开正常！")
    else:
        print("活动时间结束！")
    return "1"
# 竞技
def test_SysPVP(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("SysEPVP").exists():
        poco("SysEPVP").click()
        print("竞技打开正常")
    else:
        print("未达到开放等级")
    return "1"
# 公会
def test_SysGuild(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("SysCGuild").exists():
        poco("SysCGuild").click()
        print("公会打开正常")
    else:
        print("未达到开放等级")
    return "1"
# 日常
def test_SysActivity(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    if poco("SysAActivity").exists():
        poco("SysAActivity").click()
        print("日常打开正常")
    else:
        print("未达到开放等级")
    return "1"
#通用函数
#判断菜单是否存在屏幕中，函数调试通过，如果不能执行，poco(texture="switch").click()这个地方受到手机分辨率的影响，导致脚本无法继续执行，需要更改手机屏幕显示模式
def test_ComparepoMenuExists(sysmenu,poco):

    position = poco(sysmenu).get_position()
    if position[0] > 1:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco(texture="switch").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()
#打开角色
def test_SysItem(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ComparepoMenuExists("SysAItem", poco)
    print("角色打开成功")
    return "1"
#技能
def test_SysSkill(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ComparepoMenuExists("SysBSkill", poco)
    print("技能打开成功")
    return "1"
#精灵
def test_SysSprite(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ComparepoMenuExists("SysCSprite", poco)
    print("精灵打开成功")
    return "1"
#制作
def test_SysEquipCreate(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ComparepoMenuExists("SysDEquipCreate", poco)
    print("制作打开成功")
    return "1"

#坐骑
def test_SysHorse(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ComparepoMenuExists("SysEHorse", poco)
    print("坐骑打开成功")
    return "1"
#好友
def test_SysFriends(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ComparepoMenuExists("SysA_Friends", poco)
    print("好友打开成功")
    return "1"
#家园
def test_SysHome(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ComparepoMenuExists("SysB_Home", poco)
    print("家园打开成功")
    return "1"
#排行
def test_SysRank(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ComparepoMenuExists("SysC_Rank", poco)
    print("排行打开成功")
    return "1"
#图鉴
def test_SysCardCollect(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ComparepoMenuExists("SysD_CardCollect", poco)
    print("图鉴打开成功")
    return "1"
#头衔
def test_SysNPCFavor(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ComparepoMenuExists("SysE_NPCFavor", poco)
    print("头衔打开成功")
    return "1"
# 聊天
def test_ChatContent(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    poco("Back").click()
    # poco("chattext").click()
    # text("聊天输入测试")
    # touch([2257, 1000])
    # poco("label").click()
    # if poco(text="聊天输入测试").exists():
    #     print("输入测试成功")
    # else:
    #     print("输入字符失败")
    # print("聊天打开成功")
    return "1"


#盘算左下角菜单是否打开-----------通用函数
def test_ShortCutIcon(sysitem,poco):
    position = poco(sysitem).get_position()
    if position[1] > 1:
        poco("arrow").click()
        time.sleep(1)
        poco(sysitem).click()
    else:
        print(sysitem)
        poco(sysitem).click()

# 开拍照
def test_SysPhoto(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ShortCutIcon("SysAPhoto", poco)
    print("拍照打开正常")
    return "1"
# 打开双人动作
def test_SysLoverDance(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ShortCutIcon("SysBLoverDance", poco)
    poco("SysBLoverDance").click()
    print("开双人动作正常")
    return "1"

# 打开跳舞
def test_SysDance(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ShortCutIcon("SysCDance", poco)
    poco("SysCDance").click()
    print("打开跳舞正常")
    return "1"
# 骑乘功能
def test_SysHorseRide(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ShortCutIcon("SysEHorseRide", poco)
    poco("SysEHorseRide").click()
    print("骑乘功能正常")
    return "1"
# 变身
def test_SysChange(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    test_ShortCutIcon("SysFChange", poco)
    poco("SysFChange").click()
    print("变身功能正常")
    return "1"
