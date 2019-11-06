# -*- encoding=utf8 -*-
__author__ = "sinwu"

l=[1,2,15,41,54,5,15,4,4,4,54,54,54,8]
if l.index(41):
    print(l)


print(100%7)
print(4*"越南")


# from multiprocessing import Process
# import time
# import os
#
# def func():
#     print('aaaaa')
#     time.sleep(1)
#     print('该子进程ID:', os.getpid())  #获取自己的进程ID号
#     print('该子进程的父进程ID:', os.getppid())  #获取自己进程的父进程ID
#     print(12345)
#
# if __name__ == '__main__':
#     p = Process(target=func,)
#     p.start()
#     print('*'*10)
#     print('父进程ID>>>', os.getpid())
#     print('父进程的父进程ID>>>', os.getpid())
# module = "multi_processframe.ProjectTools.common"
# CC = __import__(module, fromlist=True)
# ipn = "print"
# A = getattr(CC, ipn[2])
# B = setattr(CC, ipn, "hello")
# A()

#
# class test():
#     name = "david"
#     def run(self):
#         return "Hello David"


# t = test()  # t 为一个test对象
# print(getattr(t, "name"))  # 获取name属性
#
# print(getattr(t, "run"))  # 获取run方法，存在就打印出方法的内存地址。
# # <bound method test.run of <__main__.test instance at 0x0269C878>>
# print(getattr(t, "run")())  # 获取run方法，后面加括号可以将这个方法运行。
# 'Hello David'
#
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # AttributeError: test instance has no attribute 'david'
# print(getattr(t, "david","18"))  # 若属性不存在，返回一个默认值。
# # print(getattr(t, "david"))  # 获取一个不存在的属性。
#
# print(hasattr(t, "name"))  # 判断对象有name属性
# print(hasattr(t, "run"))  # 判断对象有run方法
#
# print(hasattr(t, "hdw"))
# print(setattr(t, "hdw", "2"))
# print(hasattr(t, "hdw"))
# print(getattr(t, "hdw"))
# print(delattr(t, "hdw"))
# print(delattr(t, "hdw"))
# # url = input("url: ")
#
# target_module, target_func = url.split('/')
# m = __import__('lib.'+target_module, fromlist=True)
#
# inp = url.split("/")[-1]  # 分割url,并取出url最后一个字符串
# if hasattr(m,target_func):  # 判断在commons模块中是否存在inp这个字符串
#     target_func = getattr(m,target_func)  # 获取inp的引用
#     target_func()  # 执行
# else:
#     print("404")












# from multiprocessing import Process
# import datetime, time
#
# def func():
#     print(12345)
#
# if __name__ == '__main__':
#     p = Process(target=func,)
#     p.start()
#     print('*'*10)
# def add2(a,b):
#     time.sleep(2)
#     print(a+b, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
#
# def add1(a,c):
#     time.sleep(2)
#     # print(a + c, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#     print(a + c, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
#
# if __name__ == '__main__':
#     start1 = []
#     a, b, c = 3, 4, 5
#     for i in range(9):
#         add = Process(target=add2, args=(a, b))
#         add3 = Process(target=add1, args=(a, c))
#         start1.append(add)
#         start1.append(add3)
#     for start in start1:
#         start.start()
#     start.join()
    # for start in start1:
    #     start.join()
# from airtest.core.api import *
# from poco.drivers.unity3d import UnityPoco
# import random,os
# poco = UnityPoco()
# # script content
#
# for root, dirs, files in os.walk(f"D:\AirtestIDE\AutoTest_Project_DRInland\multi_processframe\TestCase"):
#         print(files) #当前路径下所有非目录子文件
# B = {"活跃奖励", "activereward", "交易所", "auction", "奖励", "award", "背包", "bag",
#             "图鉴", "card", "聊天", "chat", "黑暗神殿", "darkness", "装备", "equip", "时装", "fashion",
#             "龙魂禁地", "longhunforbidden","商城", "gamemall", "商店", "mall", "公会", "guild", "纹章", "heraldry",
#             "家园", "home", "头衔", "honor", "坐骑", "horse", "登陆奖励", "loginreward", "龙器", "longqi",
#             "龙穴", "longxue", "龙玉", "longyu","佣兵", "machine", "制作", "manufacture", "伙伴", "monster",
#             "巢穴", "nest", "噩梦庭院", "nightmare", "竞技", "pvp","悬赏", "reward", "设置", "setting",
#             "精灵", "sprite", "任务", "task", "称号", "title","队伍", "troops", "福利", "welfare", "观战", "witness",
#             "时空裂缝","space_time","无限幻境","fairyland"
#             }
#
# A = ['活跃奖励', 'activereward', '拍卖行', 'auction', '奖励', 'award',  '背包', 'bag', '图鉴', 'card', '聊天', 'chat', '黑暗神殿', 'darkness', '装备','equip', '无限幻境', 'fairyland', '时装', 'fashion', '商城', 'gamemall', '公会', 'guild', '纹章模块', 'heraldry', '家园', 'home', '头衔', 'honor', '坐骑', 'horse', '登陆奖励', 'loginreward', '龙魂禁地', 'longhunforbidden',  "龙器", 'longqi', "龙穴", 'longxue', "龙玉", 'longyu', "佣兵", 'machine', 'mall', 'manufacture', 'monster', 'nest', 'nightmare', 'ranklist', 'reward', 'space_time', 'task', 'title', 'troops', 'witness']
# B = ['活跃奖励','active_reward', '拍卖行', 'auction', '奖励', 'award',  '背包', 'bag', '图鉴', 'card', '聊天', 'chat', '黑暗神殿', 'darkness', '装备','equip', '无限幻境', 'fairyland', '时装', 'fashion', '商城', 'gamemall', '公会', 'guild', '纹章模块', 'heraldry', '家园', 'home', '头衔', 'honor', '坐骑', 'horse', '登陆奖励', 'loginreward', '龙魂禁地', 'longhunforbidden',  "龙器", 'longqi', "龙穴", 'longxue', "龙玉", 'longyu', "佣兵", 'machine', 'manufacture', 'monster', 'nest', 'nightmare', 'ranklist', 'reward', 'spacetime', 'task', 'title', 'troops', 'witness']
# C = {'活跃奖励': 'activereward', '拍卖行': 'auction', '奖励': 'award',  '背包': 'bag', '图鉴': 'card', '聊天': 'chat', '黑暗神殿': 'darkness', '装备':'equip', '无限幻境': 'fairyland', '时装': 'fashion', '商城': 'gamemall', '公会': 'guild', '纹章模块': 'heraldry', '家园': 'home', '头衔': 'honor', '坐骑': 'horse', '登陆奖励': 'loginreward', '龙魂禁地': 'longhunforbidden',  "龙器": 'longqi', "龙穴": 'longxue', "龙玉": 'longyu', "佣兵": 'machine','商店': 'mall','制造': 'manufacture', '伙伴': 'monster', '巢穴模块': 'nest', '噩梦庭院': 'nightmare', '竞技': 'pvp', '排行榜': 'ranklist', '悬赏任务': 'reward', '设置': 'setting', '时空裂缝': 'spacetime', '精灵': 'sprite', '任务': 'task', '称号': 'title', '队伍': 'troops', '福利': 'welfare', '观战': 'witness'}
# D = {'活跃奖励': 'activereward', '拍卖行': 'auction', '奖励': 'award',  '背包': 'bag', '图鉴': 'card', '聊天': 'chat', '黑暗神殿': 'darkness', '装备':'equip', '无限幻境': 'fairyland', '时装': 'fashion', '商城': 'gamemall', '公会': 'guild', '纹章模块': 'heraldry', '家园': 'home', '头衔': 'honor', '坐骑': 'horse', '登陆奖励': 'loginreward', '龙魂禁地': 'longhunforbidden',  "龙器": 'longqi', "龙穴": 'longxue', "龙玉": 'longyu', "佣兵": 'machine','商店': 'mall','制造': 'manufacture', '伙伴': 'monster', '巢穴模块': 'nest', '噩梦庭院': 'nightmare', '竞技': 'pvp', '排行榜': 'ranklist', '悬赏任务': 'reward', '设置': 'setting', '时空裂缝': 'space_time', '精灵': 'sprite', '任务': 'task', '称号': 'title', '队伍': 'troops','福利': 'welfare', '观战': 'witness'}
#
# CASELIST = {'活跃奖励': 'activereward', '拍卖行': 'auction', '奖励': 'award',  '背包': 'bag', '图鉴': 'card',
#             '聊天': 'chat', '黑暗神殿': 'darkness', '装备':'equip', '无限幻境': 'fairyland', '时装': 'fashion',
#             '商城': 'gamemall', '公会': 'guild', '纹章模块': 'heraldry', '家园': 'home', '头衔': 'honor',
#             '坐骑': 'horse', '登陆奖励': 'loginreward', '龙魂禁地': 'longhunforbidden',  "龙器": 'longqi',
#             "龙穴": 'longxue', "龙玉": 'longyu', "佣兵": 'machine','商店': 'mall','制造': 'manufacture',
#             '伙伴': 'monster', '巢穴模块': 'nest', '噩梦庭院': 'nightmare', '竞技': 'pvp', '排行榜': 'ranklist',
#             '悬赏任务': 'reward', '设置': 'setting', '时空裂缝': 'spacetime', '精灵': 'sprite', '任务': 'task',
#             '称号': 'title', '队伍': 'troops', '队伍': 'welfare', '观战': 'witness', '幻龙起源': 'nothosaur_origin'}
# # TODO：获取已经写好的模块
# undonelist = []
# for k, v in CASELIST.items():
#     undonelist.append(k)
#
# guess = int(input("输入数字: "))
# while guess != 8:
#     temp = input("猜错了，重新输入: ")
#     guess = int(temp)
#     if guess == 8:
#         print("猜对了")
#     else:
#         if guess > 8:
#             print("大了")
#         else:
#             print("小了")



# for C in C:
#     if C not in B:
#         print(C)
# print("-----------------")
# for D in D:
#     if D not in A:
#         print(D)
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
# if poco("SysG_Live").exists(),
#     poco("SysG_Live").click()
# else,
#     print("主界面没有观战按钮")
# if poco("SpectateDlg(Clone)").offspring("SpectateFrame").offspring("item0").child("Bg").child("TextLabel").exists(),
#     poco("SpectateDlg(Clone)").offspring("SpectateFrame").offspring("item0").child("Bg").child("TextLabel").click()
# else,
#     print("观战界面没有找到推荐按钮")
# if poco("SpectateDlg(Clone)").offspring("SpectateFrame").offspring("item1").child("Bg").child("TextLabel").exists(),
#     poco("SpectateDlg(Clone)").offspring("SpectateFrame").offspring("item1").child("Bg").child("TextLabel").click()
# else,
#     print("观战界面没有找到天梯赛按钮")
#
#
# poco("SpectateDlg(Clone)").offspring("SpectateFrame").offspring("item2").child("Bg").child("TextLabel").click()
# poco("SpectateDlg(Clone)").offspring("SpectateFrame").offspring("item3").child("Bg").child("TextLabel").click()
# poco("SpectateDlg(Clone)").offspring("SpectateFrame").offspring("item4").child("Bg").child("TextLabel").click()
# poco("SpectateDlg(Clone)").offspring("SpectateFrame").offspring("item5").child("Bg").child("TextLabel").click()
# poco(text="刷 新").click()
# poco("SpectateDlg(Clone)").child("Bg").offspring("1").offspring("SelectedTextLabel").click()
# poco("Text").click()
# poco("SpectateDlg(Clone)").offspring("BtnDeny").child("BtnHigh").click()
# poco("SpectateDlg(Clone)").offspring("BtnAllow").child("BtnHigh").click()
# Label = poco("Label").get_text()
# if Label == "保存设置",
#     print("脚本运行成功")
# else,
#     print("脚本运行失败")



# if __name__ == __main__,
#     import pocounit
#     pocounit.main()
