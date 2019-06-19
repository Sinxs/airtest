"""
黑暗神殿模块自动化脚本
"""

from multi_processframe.Tools import printcolor,adb_connect,screenshot
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
Androidpoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def butpos(butpos,pos1=0.4,pos2=0.81,high=1330,low=930,lows=482):
    """
把不在屏幕内部的控件滑动到屏幕内，使之可被操作
:param butpos: 控件的坐标值
:param pos1: 希望控件所在屏幕上的最低限
:param pos2: 希望控件所在屏幕上的最上限
:param high: 固定坐标
:param low: 滑动起始或终点位置
:param lows: 滑动起始或终点位置
:return:
    """
    for i in range(20):
        but = butpos.get_position()
        if but[1] < pos1:
            swipe([high, lows], [high, low], 5)
        elif but[1] > pos2:
            swipe([high, low], [high, lows], 5)
        else:
            break


def darkness(poco):
    """
    时间太长，所以只打前30关，如果初始关卡大于30，则只打当前关卡
    :param poco:
    :return:
    """
    for i in range(200):
        sleep(1)
        if int(poco("InfoBack").offspring("Level").get_text()) < 10:
            if poco("Avatar").exists():  # 呼出GM
                poco("Avatar").click()
                text("killall")  # 再次输入killall
                printcolor.printgreen("开始通过第 " + poco("InfoBack").offspring("Level").get_text() + " 关！！！")
                Androidpoco("android.widget.Button").click()
                sleep(18)
        elif int(poco("InfoBack").offspring("Level").get_text()) >= 10:
            printcolor.printgreen("关卡数量大于10")
            if poco("Avatar").exists():
                poco("Avatar").click()
                text("killall")
                Androidpoco("android.widget.Button").click()
                printcolor.printgreen("第 "+poco("InfoBack").offspring("Level").get_text()+" 关，测试完成！！！！！\n打完这局下一关返回不打了。。")
                sleep(15)
                if poco("Pause").exists():
                    poco("Pause").click()
                    poco("Leave").click()  # 退出副本
                    sleep(10)
                    if poco("Text").exists():
                        poco("Cancel").click()  # 离开

                    elif poco("Continue").exists():  # 返回主城按钮
                        poco("Continue").click()
                break
        elif poco("Continue").exists():  # 返回主城按钮
            poco("Continue").click()
            printcolor.printgreen("挑战结束,没打过,鄙视，哈哈哈哈……，不过也算测试完成。")
            break



def darkness_ectype(devices):
    poco = adb_connect.device(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        printcolor.printgreen("主界面缺少日常按钮，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "主界面缺少日常按钮")
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item530").offspring("Background")  # 黑暗神殿参加按钮
    if pos.exists():
        butpos(butpos=pos, pos1=0.4, pos2=0.79, high=565, low=511, lows=240)  # 调用butpos方法
        pos.click()  # 点击黑暗神殿参加按钮
    else:
        printcolor.printgreen("日常界面没有黑暗神殿选项，请检查...")
        screenshot.get_screen_shot(time.time(), devices, "日常界面没有黑暗神殿选项")
    if poco("Title").exists():  # 排行榜
        poco("Rank").click()
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("1").exists() and freeze_poco("2").exists() and freeze_poco("3").exists() and freeze_poco("4").exists() and freeze_poco("5").exists():
            for i in range(1,20):
                printcolor.printgreen("检查点 "+freeze_poco(str(i)).child("Label").get_text()+" 显示正确")
            printcolor.printgreen("排行榜首界面显示正确，详细内容不做判断，如果需要，后期优化")
            poco("Close").click()
        else:
            printcolor.printred("排行榜界面显示错误，请检查....")
            screenshot.get_screen_shot(time.time(), devices, "排行榜界面显示错误")
    if poco("FirstBlood").exists():  # 首通奖励
        poco("FirstBlood").click()
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("TeamTowerNewDlg(Clone)").offspring("CheckReward").offspring("T").exists() and \
                freeze_poco(texture="l_imageView_07").exists() and freeze_poco("GetAfterPass").exists():
            printcolor.printgreen("首通奖励显示正确...")
            poco("Close").click()
        else:
            printcolor.printred("首通奖励显示错误，请检查.....")
            screenshot.get_screen_shot(time.time(), devices, "首通奖励显示错误")

    if poco("times").get_text()[0] == "1":
        printcolor.printgreen("黑暗神殿有重置次数...")
        poco("Reset").click()
        if poco("OK").exists():
            poco("OK").click()
            printcolor.printgreen("重置完成...")
        else:
            printcolor.printred("连第一层都没有打过，不能重置。。。")
            screenshot.get_screen_shot(time.time(), devices, "不能重置")
    else:
        printcolor.printgreen("当前没有重置次数，接着打吧....")
        screenshot.get_screen_shot(time.time(), devices, "当前没有重置次数")
    if poco("GoBattle").exists():
        poco("GoBattle").click()
        sleep(15)
        darkness(poco)
        sleep(15)

        return poco("Title").get_text()

