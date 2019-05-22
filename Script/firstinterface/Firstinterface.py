# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from airtest.core.api import using
using("auto_test.air")
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
import time
print("start...")
poco = UnityPoco()
# 启动游戏
# Startgame.test_Start()
def test_SignInReward(): 
    """1.每天第一次登陆弹出签到窗口进行签到
       2.第一次登陆的时候没有签到，就到福利中去签到
    """
    #time.sleep(15)
    if poco("Check").exists() and poco("RedPoint").exists() : # 判断签到状态，有红点就是还没签到
        poco("Check").click() # 点击签到
        print("签到成功!")
    else:
        poco("SysGWelfare").click()
        poco("WelfareDlg(Clone)").offspring("item5").click()     
        if poco("RedPoint").exists():
            poco("Check").click()
            print("签到成功!")
        else:
            print("已经完成签到，未使用签到方法签到!")

def test_CheckSignIn():
    """
    """
            
#
def test_Close():
    """界面关闭操作----通用函数    
    """
    poco("Close").click()
    print("关闭窗口")
# 提升
def test_sysPromote():
    if poco("SysAAFPromote").exists():
        poco("SysAAFPromote")
        poco("SysAAFPromote").click()
        print("提升按钮点击正常")
    else:
        print("暂时没有可提升项目")
    test_Close()
    return "1"

  # 变强
def test_SysStrengthen():
    poco("SysIBq").click()
    print("变强界面打开成功！")
    test_Close()
    return "1"


# 奖励
def test_SysAward():
    poco("SysEReward").click()
    print("奖励界面打开成功！")
    test_Close()
    return "1"
# 交易所
def test_SysAuction():
    poco("SysCAuction").click()
    print("交易所打开成功！")
    test_Close()
    return "1"
# 商城
def test_SysGameMall():
    poco("SysAGameMall").click()
    print("商城打开成功！")
    test_Close()
    return "1"
# 极限龙本
def test_SysLimitDragon():
    if poco("SysLimitDragon").exists():
        poco("SysLimitDragon").click()
        print("活动时间内，极限龙本打开正常！")
        sleep(2)
        poco("Close").click()
        print("关闭窗口")
        return "1"
    else:
        print("极限龙本不在时间内，无法进入功能！")
        sleep(2)
        poco("Close").click()
        print("关闭窗口")

        return "1"

# 登陆奖励
def test_SysSevenActivity():
    if poco("SysISevenActivity").exists():
        poco("SysISevenActivity").click()
        print("七日登陆活动打开正常")
        test_Close()
        return "1"
    else:
        print("七日登陆签到已经全部完成！")
# 观看
def test_SysLive():
    poco("SysG_Live").click()
    print("观战窗口打开正常！")
    test_Close()
    return "1"
# 精彩活动
def test_SysOperatingActivity():
    poco("SysEOperatingActivity").click()
    print("精彩活动打开正常！")
    test_Close()
    return "1"

# 首冲
def test_SysFirstRecharge():
    if poco("SysCFirstRecharge").exists():
        poco("SysCFirstRecharge").click()
        print("首冲未充值，界面打开正常")
        test_Close()
        return "1"
    else:
        print("首冲完成，入口消失")
# 开服狂欢
def test_SysCarnival():
    if poco("SysACarnival").exists():
        poco("SysACarnival").click()
        print("开服狂欢界面打开正常！")
        test_Close()
        return "1"
    else:
        print("活动时间结束！")
        return "1"

# 竞技
def test_SysPVP():
    if poco("SysEPVP").exists():
        poco("SysEPVP").click()
        print("竞技打开正常")
        test_Close()
        return "1"
    else:
        print("未达到开放等级")
    
# 公会
def test_SysGuild():
    if poco("SysCGuild").exists():
        poco("SysCGuild").click()
        print("公会打开正常")
        test_Close()
        return "1"
    else:
        print("未达到开放等级")
        
# 日常
def test_SysActivity():
    if poco("SysAActivity").exists():
        poco("SysAActivity").click()
        print("日常打开正常")
        test_Close()
        return "1"
    else:
        print("未达到开放等级")
#通用函数
#判断菜单是否存在屏幕中，函数调试通过，如果不能执行，poco(texture="switch").click()这个地方受到手机分辨率的影响，导致脚本无法继续执行，需要更改手机屏幕显示模式
def test_ComparepoMenuExists(sysmenu):
    position = poco(sysmenu).get_position()
    if position[0] > 1: # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco(texture="switch").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()
#打开角色
def test_SysItem():
    test_ComparepoMenuExists("SysAItem")
    print("角色打开成功")
#技能
def test_SysSkill():
    test_ComparepoMenuExists("SysBSkill")
    print("技能打开成功")
#精灵
def test_SysSprite():
    test_ComparepoMenuExists("SysCSprite")
    print("精灵打开成功")
#制作
def test_SysEquipCreate():
    test_ComparepoMenuExists("SysDEquipCreate")
    print("制作打开成功")
#坐骑
def test_SysHorse():
    test_ComparepoMenuExists("SysEHorse")
    print("坐骑打开成功")
#好友
def test_SysFriends():
    test_ComparepoMenuExists("SysA_Friends")
    print("好友打开成功")
#家园
def test_SysHome():
    test_ComparepoMenuExists("SysB_Home")
    print("家园打开成功")
#排行
def test_SysRank():
    test_ComparepoMenuExists("SysC_Rank")
    print("排行打开成功")
#图鉴
def test_SysCardCollect():
    test_ComparepoMenuExists("SysD_CardCollect")
    print("图鉴打开成功")
#头衔
def test_SysNPCFavor():
    test_ComparepoMenuExists("SysE_NPCFavor")
    print("头衔打开成功")
# 聊天
def test_ChatContent():
    poco("ChatContent").click()
    print("聊天打开成功")
#盘算左下角菜单是否打开-----------通用函数
def test_ShortCutIcon(sysitem):
    position = poco(sysitem).get_position()
    if position[1] > 1:
        poco("arrow").click()
        time.sleep(1)
        poco(sysitem).click()
    else:
        print(sysitem)
        poco(sysitem).click()
# 开拍照
def test_SysPhoto():
    test_ShortCutIcon("SysAPhoto")
    print("拍照打开正常")
# 打开双人动作
def test_SysLoverDance():
    test_ShortCutIcon("SysBLoverDance")
    print("开双人动作正常")
# 打开跳舞
def test_SysDance():
    test_ShortCutIcon("SysCDance")
    print("打开跳舞正常")
# 骑乘功能
def test_SysHorseRide():
    test_ShortCutIcon("SysEHorseRide")
    print("骑乘功能正常")
# 变身
def test_SysChange():
    test_ShortCutIcon("SysFChange")
    print("变身功能正常")
    return "1"

# 爆红
def test_XMinClient():
    if exists(Template(r"XMinClient.png", record_pos=(-0.437, -0.038), resolution=(2280, 1080))):
        print("当前功能存在爆红")
        touch()
    else:
        print("功能正常，UI正常", end="")
       

