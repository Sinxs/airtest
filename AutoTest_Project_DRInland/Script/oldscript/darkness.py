"""
黑暗神殿模块自动化脚本
"""

from multi_processframe.ProjectTools import common,common,common
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from multi_processframe.ProjectTools import common


def butpos(devices,butpos,pos1=0.4,pos2=0.81,high=1330,low=930,lows=482):
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
            common.setswipe(1, [high, lows], [high, low], devices)
        elif but[1] > pos2:
            common.setswipe(1, [high, low], [high, lows], devices)
        else:
            break



def darkness(poco,devices):
    """
    时间太长，所以只打前30关，如果初始关卡大于30，则只打当前关卡
    :param poco:
    :return:
    """
    dev = connect_device("android:///" + devices)
    Androidpoco = AndroidUiautomationPoco(device=dev, use_airtest_input=True, screenshot_each_action=False)
    for i in range(200):
        sleep(1)
        if int(poco("InfoBack").offspring("Level").get_text()) < 10:
            if poco("Avatar").exists():  # 呼出GM
                poco("Avatar").click()
                text("killall")  # 再次输入killall
                common.printgreen("开始通过第 " + poco("InfoBack").offspring("Level").get_text() + " 关！！！")
                Androidpoco("android.widget.Button").click()
                sleep(18)
        elif int(poco("InfoBack").offspring("Level").get_text()) >= 10:
            common.printgreen("关卡数量大于10")
            if poco("Avatar").exists():
                poco("Avatar").click()
                text("killall")
                Androidpoco("android.widget.Button").click()
                common.printgreen("第 " + poco("InfoBack").offspring("Level").get_text() + " 关，测试完成！！！！！\n打完这局下一关返回不打了。。")
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
            common.printgreen("挑战结束,没打过,鄙视，哈哈哈哈……，不过也算测试完成。")
            break



def darkness_ectype(start, devices):
    poco = common.deviceconnect(devices)
    if poco("Duck").exists():
        poco("Duck").click()
        sleep(2)
        poco("XSys_Activity").click()  # 点击日常按钮
    else:
        common.printgreen("主界面缺少日常按钮，请检查...")
        common.get_screen_shot(start, time.time(), devices, "主界面缺少日常按钮")
    pos = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item530").offspring("Background")  # 黑暗神殿参加按钮
    if pos.exists():
        butpos(devices,butpos=pos, pos1=0.4, pos2=0.79, high=565, low=511, lows=240)  # 调用butpos方法
        pos.click()  # 点击黑暗神殿参加按钮
    else:
        common.printgreen("日常界面没有黑暗神殿选项，请检查...")
        common.get_screen_shot(start, time.time(), devices, "日常界面没有黑暗神殿选项")
    if poco("Title").exists():  # 排行榜
        poco("Rank").click()
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("1").exists() and freeze_poco("2").exists() and freeze_poco("3").exists() and freeze_poco("4").exists() and freeze_poco("5").exists():
            for i in range(1,20):
                common.printgreen("检查点 " + freeze_poco(str(i)).child("Label").get_text() + " 显示正确")
            common.printgreen("排行榜首界面显示正确，详细内容不做判断，如果需要，后期优化")
            poco("Close").click()
        else:
            common.printred("排行榜界面显示错误，请检查....")
            common.get_screen_shot(start, time.time(), devices, "排行榜界面显示错误")
    if poco("FirstBlood").exists():  # 首通奖励
        poco("FirstBlood").click()
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("TeamTowerNewDlg(Clone)").offspring("CheckReward").offspring("T").exists() and \
                freeze_poco(texture="l_imageView_07").exists() and freeze_poco("GetAfterPass").exists():
            common.printgreen("首通奖励显示正确...")
            poco("Close").click()
        else:
            common.printred("首通奖励显示错误，请检查.....")
            common.get_screen_shot(start, time.time(), devices, "首通奖励显示错误")

    if poco("times").get_text()[0] == "1":
        common.printgreen("黑暗神殿有重置次数...")
        poco("Reset").click()
        if poco("OK").exists():
            poco("OK").click()
            common.printgreen("重置完成...")
        else:
            common.printred("连第一层都没有打过，不能重置。。。")
            common.get_screen_shot(start, time.time(), devices, "不能重置")
    else:
        common.printgreen("当前没有重置次数，接着打吧....")
        common.get_screen_shot(start, time.time(), devices, "当前没有重置次数")
    if poco("GoBattle").exists():
        poco("GoBattle").click()
        sleep(15)
        darkness(poco,devices)
        sleep(15)

        return poco("Title").get_text()

