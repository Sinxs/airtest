# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from multi_processframe.ProjectTools import common
import time

from poco.utils.simplerpc import simplerpc
from multi_processframe.ProjectTools.androidtools import AndroidTools as tool
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


def butpos(posb, butpos,pos1=0.4,pos2=0.81):
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
    # butpos = butpos
    for i in range(20):
        but = butpos.get_position()
        if but[1] < pos1:
            posb.swipe([0, 0.25])
        elif but[1] > pos2:
            posb.swipe([0, -0.25])
        else:
            break


def select_server(poco,server):
    print(f"要找的服务器为  {server} 开始查找服务器")
    poco(text=server)
    for Area in range(len(poco("AreaList").child())):
        Area = "Area" + str(Area)
        pos = poco(Area)
        posb = poco("AreaList")
        butpos(posb, butpos=pos, pos1=0.2282, pos2=0.79)  # 调用butpos方法
        pos.click()  # 点击服务器
        if poco("LoginDlg(Clone)").offspring("Bg").child("Name").exists():
            for servers in poco("LoginDlg(Clone)").offspring("Bg").child("Name"):
                common.sleep(2)
                if str(servers.get_text()) == server:
                    pos = servers
                    posb = poco("SelectServer")
                    butpos(posb, butpos=pos, pos1=0.265, pos2=0.753)  # 调用butpos方法
                    servers.click()
                    common.sleep(2)
                    return


def firststartgame(username, password, packname, devices, server):
    dev = common.connect_device("android:///" + devices)
    common.start_app(packname)  # 启动app
    Androidpoco = AndroidUiautomationPoco(device=dev, use_airtest_input=True, screenshot_each_action=False)
    common.sleep(2)
    while True:
        common.sleep(1)
        if Androidpoco("android:id/button1").exists():
            Androidpoco("android:id/button1").click()
        else:
            break
    if Androidpoco("android:id/message").exists():
        Androidpoco("android:id/button1").click()
    common.sleep(5)
    while True:
        poco = common.deviceconnect(devices)
        common.sleep(5)
        try:
            poco("iptAccount").wait_for_appearance(60)
            common.sleep(3)
            print(f"{devices}加载完成，开始登录账号")
            poco("iptAccount").set_text(username)
            poco("iptPassword").set_text(password)
            common.sleep(3)
            poco("btnLogin").click()
            common.sleep(3)
            if poco(texture="l_button_00").exists():  # 公告
                poco(texture="l_button_00").click()
            if poco("Panel").exists():  # 前往新区
                poco(texture="btk5").click()
            if poco("Label").get_text().split(" ")[0] == "OB+13":
                print(f"要找的服务器为 {server} , 现在已经是需要的服务器了，不需要重新选择...")
            else:
                if poco("zhanghao").exists():  # 更换服务器按钮
                    poco("zhanghao").click()
                    select_server(poco, server)
            print(f"选择 {server} 服务器成功")
            common.sleep(2)
            if poco("Enter").exists():
                poco("Enter").click()
                common.sleep(2)
            if poco(text="进入游戏").exists():
                poco(text="进入游戏").click()
                common.sleep(2)
            print("点击进入游戏，开始选择角色。。。")
            poco("EnterGame").wait_for_appearance()
            if poco("EnterGame").exists():
                poco("EnterGame").click()
                print("角色自动寻找成功，点击开始游戏。。。")
                common.sleep(15)
            break
        except:
            print(f"{devices}还未加载完毕，请稍等.....")
    common.sleep(5)
    common.stop_app(packname)


def RpcTimeoutime():  # rpc超时问题重置次数  1 重置2次 2 重置4次 以此类推
    item = 1
    return item


def sleeptiem():  # 脚本等待时间，如果时间过长，说明出现意外
    item = 1000
    return item

def startgame(devices):
    packagename = tool(devices).get_packagename()
    try:
        if not common.os.system(f"adb -s {devices} shell pidof {packagename}") == 1:
            print("游戏已经启动...")
            # 判断主界面
            if interface(devices, packagename) == "主界面":
                return None
        else:
            try:
                stop_APP(devices, packagename)
                return None
            except:
                print("重置游戏脚本失败，重新启动游戏")
                stop_APP(devices, packagename)
                startgame(devices)
    except simplerpc.RpcTimeoutError:
        for i in range(RpcTimeoutime()):  # rpc超时问题重置次数
            try:
                print("重置脚本环境期间，Rpc重连失败，杀掉游戏进程，脚本重新启动")
                common.stop_app(packagename)
                startgame(devices)
                break
            except simplerpc.RpcTimeoutError:
                print("重置脚本环境期间，Rpc重连失败，杀掉游戏进程，脚本重新启动")
                common.stop_app(packagename)
                startgame(devices)
    except ConnectionAbortedError as e:
        common.stop_app(packagename)
        print(f"{e},主机断开连接，杀掉游戏进程，脚本重新启动")
        startgame(devices)
    return None



def interface(devices, packagename):

    poco = common.deviceconnect(devices)
    with poco.freeze() as freeze_poco:
        if freeze_poco(text="重新连接").exists():
            common.printgreen("网络断开连接，重启游戏....")
            stop_APP(devices, packagename)
        if freeze_poco("Avatar").exists() and \
                freeze_poco("Duck").exists() and \
                freeze_poco("SysCGuild").exists() and \
                freeze_poco("SysEPVP").exists() and \
                not freeze_poco(texture="l_close_00").exists() and \
                not freeze_poco("Cancel").exists() and \
                not freeze_poco("Close").exists() and \
                not freeze_poco("RecruitPublishView(Clone)").offspring("Close").exists() and \
                not freeze_poco("SettingDlg(Clone)").child("Bg").child("Close").exists():
            common.printgreen("现在场景为主界面")
            return "主界面"
        else:
            openinterface(devices, packagename)
            if interface(devices, packagename) == "主界面":
                return None
            else:
                stop_APP(devices, packagename)


def openinterface(devices, packagename):
    try:
        common.sleep(2)
        common.printgreen("游戏已经启动，但是不在主界面，现在回到主界面")
        poco = common.deviceconnect(devices)
        freeze_poco = poco.freeze()  # TODO：定义冻结poco
        if freeze_poco("Pause").exists():
            poco("Pause").click()  # 准备退出副本
            poco("Leave").click()  # 点击退出副本
            common.sleep(20)
        if poco(text="返回主城").exists():
            poco(text="返回主城").click()  # 准备返回主城
            common.sleep(20)
        if poco("OK").exists():
            poco("OK").click()
        # touch((45,9))
        time.sleep(1)
        # touch((45,9))
        for x in range(4):
            freeze_poco = poco.freeze()  # TODO：定义dongjiepoco
            time.sleep(1)
            if freeze_poco("Btn").exists():
                if freeze_poco("Btn").get_position()[1] < 1 and \
                        poco("Btn").get_position()[1] > 0:
                    if freeze_poco("Btn").get_position()[0] < 1 and \
                            poco("Btn").get_position()[0] > 0:
                        time.sleep(1.5)
                        freeze_poco("Btn").click()
            if poco(texture="l_close_00").exists():
                time.sleep(1)
                poco(texture="l_close_00").click()
            elif freeze_poco("Cancel").exists():
                poco("Cancel").click()
            elif poco(texture="l_close_00").exists():
                time.sleep(1)
                poco(texture="l_close_00").click()
            elif freeze_poco("RecruitPublishView(Clone)").offspring("Close").exists():
                time.sleep(1)
                poco("RecruitPublishView(Clone)").offspring("Close").click()
            if poco("SettingDlg(Clone)").child("Bg").child("Close").exists():
                poco("SettingDlg(Clone)").child("Bg").child("Close").click()
            if poco("SettingDlg(Clone)").offspring("Close").exists():
                poco("SettingDlg(Clone)").offspring("Close").click()
                time.sleep(1)
            if poco("Close").exists():
                time.sleep(1)
                poco("Close").click()
                if poco("Close").exists():
                    time.sleep(1)
                    poco("Close").click()
            poco = common.deviceconnect(devices)
            with poco.freeze() as freeze_poco:
                if freeze_poco(text="重新连接").exists():
                    common.printgreen("网络断开连接，重启游戏....")
                    stop_APP(devices, packagename)
                if freeze_poco("Avatar").exists() and \
                        freeze_poco("Duck").exists() and \
                        freeze_poco("SysCGuild").exists() and \
                        freeze_poco("SysEPVP").exists() and \
                        not freeze_poco(texture="l_close_00").exists() and \
                        not freeze_poco("Cancel").exists() and \
                        not freeze_poco("Close").exists() and \
                        not freeze_poco("RecruitPublishView(Clone)").offspring("Close").exists() and \
                        not freeze_poco("SettingDlg(Clone)").child("Bg").child("Close").exists():
                    common.printgreen("现在场景为主界面")
                    return None
                else:
                    common.printgreen("游戏没有会到主界面，现在进行重启操作。。。")
                    stop_APP(devices, packagename)
    except simplerpc.RpcTimeoutError:
        for i in range(RpcTimeoutime()):  # rpc超时问题重置次数
            try:
                print("重置脚本环境期间，Rpc重连失败，杀掉游戏进程，脚本重新启动")
                common.stop_app(packagename)
                restart_app(devices)
                break
            except simplerpc.RpcTimeoutError:
                print("重置脚本环境期间，Rpc重连失败，杀掉游戏进程，脚本重新启动")
                common.stop_app(packagename)
                restart_app(devices)
    except ConnectionAbortedError:
        common.stop_app(packagename)
        print("ConnectionResetError,主机断开连接，杀掉游戏进程，脚本重新启动")
        restart_app(devices)


def restart_app(devices):
    packagename = tool(devices).get_packagename()
    return stop_APP(devices, packagename)


def stop_APP(devices, packagename):
    try:
        print("游戏未启动，开始启动游戏...")
        print(packagename)
        common.stop_app(packagename)
        common.sleep(1)
        common.start_app(packagename)
        common.sleep(3)
        start = time.time()
        while True:
            common.os.system(f"adb -s {devices} shell input tap {100} {100}")
            common.sleep(3)
            common.os.system(f"adb -s {devices} shell input tap {100} {100}")
            poco = common.deviceconnect(devices)
            try:
                if poco("Dialog").exists():
                    poco("OK").click()
                if poco("LabelStatus").exists():
                    common.printgreen("等待更新完成....")
                    poco("AnnouncementDlg(Clone)").child("Bg").child("Enter").wait_for_appearance()
                common.printgreen("请耐心等待...")
                poco("AnnouncementDlg(Clone)").child("Bg").child("Enter").wait_for_appearance(25)
                break
            except:
                if time.time() - start > 120:
                    print(f"游戏启动时间超过 {start}s，现在进行重新启动")
                    stop_APP(devices, packagename)
                    break
                print("正在启动游戏，请稍后...")
        poco(texture="l_button_00").wait_for_appearance()
        poco(texture="l_button_00").click()
        common.sleep(3)
        if poco(text="进入游戏").exists():
            poco(text="进入游戏").click()
            if poco(text="进入游戏").exists():
                poco(text="进入游戏").click()
            print("点击进入游戏，开始选择角色。。。")
            poco("EnterGame").wait_for_appearance(5)
            common.sleep(3)
            if poco("EnterGame").exists():
                poco("EnterGame").click()
                print("角色自动寻找成功，点击开始游戏。。。")
                common.sleep(15)
            else:
                print("进入游戏失败，请检查。。。。")
        else:
            print("进入游戏失败，请检查。。。。")
        interface(devices, packagename)
    except ConnectionAbortedError as e:
        print(f"{e} 主机断开连接，杀掉游戏进程，脚本重新启动")
        restart_app(devices)


if __name__=="__main__":
    devices = "e37c0280"
    packagename = tool(devices).get_packagename()
    common.printgreen(packagename)
    poco = common.deviceconnect(devices)
    stop_APP(devices, packagename)



    # start_app("com.tencent.tmgp.dragonnest")  # 启动app
    # startgame(devices)
    # packname = "com.dragonnestm.ggplay.koramgame.global"
    # firststartgame(packname, devices)
    # dev = connect_device("android:///" + devices)
    # Androidpoco = AndroidUiautomationPoco(device=dev, use_airtest_input=True, screenshot_each_action=False)
    # sleep(2)
    # while True:
    #     if Androidpoco("android:id/button1").exists():
    #         Androidpoco("android:id/button1").click()
    #     else:
    #         break
    # startgame(devices)
    # poco = deviceconnect(devices)
    # text("wtt111")
    # text("123465")
    # poco.click([0.474, 0.544])
