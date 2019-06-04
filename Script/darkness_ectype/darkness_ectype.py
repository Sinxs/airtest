from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco


def darkness(poco):
    for i in range(200):
        sleep(1)
        if not poco("InfoBack").offspring("Level").get_text() == "200":
            if poco("Avatar").exists():  # 呼出GM
                poco("Avatar").click()
                text("killall")  # 再次输入killall
                print("开始通第 " + poco("InfoBack").offspring("Level").get_text() + " 关！！！")
                poco("Skill1").offspring("cd").click()
                sleep(20)
        elif poco("Continue").exists():
            poco("Continue").click()
            print("挑战结束,没打过,鄙视，哈哈哈哈……，不过也算测试完成。")
            break
        elif poco("InfoBack").offspring("Level").get_text() == "200":
            if poco("Avatar").exists():
                poco("Avatar").click()
                text("killall")
                poco("Skill1").offspring("cd").click()
                print("最后第 "+poco("InfoBack").offspring("Level").get_text()+" 关，测试完成！！！！！")
                sleep(15)
                if poco("Continue").exists():
                    poco("Continue").click()
                    print("返回主城")
                break


def darkness_ectype(devices):
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)  # 链接设备，并且重置 poco
    # TODO：因为APK的问题，所以现在增加以下代码，等到apk打出来后干掉
    poco("Avatar").click()
    text("addgmattr 22 999999999")
    poco("MenuSwitchBtn").click()
    poco("SettingDlg(Clone)").offspring("Close").click()
    poco(text=">").click()
    text("addgmattr 12 999999999")
    poco("MenuSwitchBtn").click()
    poco(text=">").click()
    text("addgmattr 4 999999999")
    poco("MenuSwitchBtn").click()
    poco("Open").click()
    # TODO：以上代码有新的APK后干掉

    if poco("Duck").exists():
        poco("Duck").click()
    else:
        print("当前界面没有日常按钮，请检查。。。")
    item = poco("DailyActivityDlg(Clone)").offspring("XActivityHandler").offspring("Item530").offspring("Label")

    if item.exists():
        for ii in range(10):
            pos = item.get_position()
            if pos[1] < 0.14:
                swipe([1060, 350], [1060, 723], 5)
            if pos[1] > 0.78:
                swipe([1060, 723], [1060, 350], 5)
            else:
                break
        item.click()
    else:
        print("界面找不到黑暗神殿，前检查是否控件缺失........")
    if poco("Title").exists():  # 排行榜
        poco("Rank").click()
        if poco("RankDlg(Clone)").offspring("TabList").offspring("2").offspring("9").offspring("SelectedLabel").exists():
            print("排行榜界面显示正确")
            poco("Close").click()
        else:
            print("排行榜界面显示错误，请检查....")
    if poco("FirstBlood").exists():  # 首通奖励
        poco("FirstBlood").click()
        if poco("TeamTowerNewDlg(Clone)").offspring("CheckReward").offspring("T").exists():
            print("首通奖励显示正确...")
            poco("Close").click()
        else:
            print("首通奖励显示错误，请检查.....")

    if poco("times").get_text()[0] == "1":
        print("黑暗神殿有重置次数...")
        poco("Reset").click()
        if poco("OK").exists():
            poco("OK").click()
            print("重置完成...")
    else:
        print("当前没有重置次数，接着打吧....")

    if poco("GoBattle").exists():
        poco("GoBattle").click()
        sleep(15)
        darkness(poco)
        sleep(15)
        return poco("Title").get_text()
w