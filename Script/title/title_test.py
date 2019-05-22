from airtest.core.api import *
# from poco.drivers.unity3d import UnityPoco
# poco = UnityPoco()
import random

def enter_title(poco):  # TODO：在主界面寻找角色按钮并点击

    # Startgame(poco)
    SysAItem = poco("SysAItem")
    AItempos = SysAItem.get_position()
    if AItempos[0] > 1:
        print("当前界面没有角色按钮，点击 + 号")
        poco(texture="switch").click()  # 点击+号
        if poco("SysAItem").exists():
            poco("SysAItem").click()  # 点击角色按钮
        if poco("XSys_Design_Designation").exists():  # 判断称号按钮并点击
            poco("XSys_Design_Designation").click()

    else:
        print("当前界面就有角色按钮")
        if poco("SysAItem").exists():
            poco("SysAItem").click()  # 点击角色按钮
        if poco("XSys_Design_Designation").exists():  # 判断称号按钮并点击
            poco("XSys_Design_Designation").click()


def titlepos(posbut):
    """
    获取控件的坐标值，如果在标准之内打断循环，如果超出标准则进行滑动
    :param posbut: 传入需要获取坐标的控件
    :return:
    """
    for i in range(5):
        pos = posbut.get_position()
        # print(pos)
        if pos[1] > 0.730:
            swipe([1434, 746], [1434, 340])
        elif pos[1] < 0.260:
            swipe([1434, 340], [1434, 746])
        else:
            break



def titletest1(item2,poco):
    """
    循环获取当前页签中的称号控件，然后进行判断
    :return:
    """

    title1=["1"]
    code = False
    Fa = False
    for i in range(12):
        for item in range(8):
            item1 = "item" + str(item)
            if not poco("ItemNewDlg(Clone)").offspring(item1).child("Bg").exists():
                continue
            textlist = poco("ItemNewDlg(Clone)").offspring(item1).child("Animation").get_text()
            title = poco("ItemNewDlg(Clone)").child("Bg").child("RightPanel").child("DesignationFrame").child("Right").child("ScrollView").child("WrapContent").offspring(item1).child("Bg")  # 判断第一个循环
            if title.exists():  # 判断第二个循环
                titlepos(title)  # 检查当前控件的位置，并滑动到指定位置
                # todo:加上判断，已经测试过的控件直接打断当前循环，开始下个循环
                textlist1 = poco("ItemNewDlg(Clone)").offspring(item1).child("Animation").get_text()
                for i in range(len(title1)):
                    if textlist == title1[i-1]:
                        Fa = True
                        break
                if Fa == True:
                    break
                else:
                    if poco("ItemNewDlg(Clone)").offspring(item1).child("Animation").child("Sprite").exists() and poco("ItemNewDlg(Clone)").offspring(item1).child("Animation").exists():
                        n = poco("ItemNewDlg(Clone)").offspring(item1).child("Animation").child("Sprite").attr("texture")  #  拿到控件元素进行判断
                        title1.append(n)
                        print("这个称号是图片格式，内存地址是====》",n)

                    elif poco("ItemNewDlg(Clone)").offspring(item1).child("Animation").exists():  # 判断这个称号是不是存在
                        n = textlist1
                        print(f"称号 ==>>【 {textlist1} 】测试完成")  # 如果存在就打印出来
                        title1.append(textlist)  # 把元素加进列表


                    if n == "Target_reward_04":  # 如果相等，等于运行到了最后一步
                        print(poco("ItemNewDlg(Clone)").offspring("Tabs").child(item2).offspring("TextLabel"))  # 传入当前称号页签的text
                        code = True
                    if n == "[fff7b4]贝思柯德复原":
                        code = True
                    if n == "b'Title_JXLB_HL_3'":
                        code = True
                    if n == "[fff7b4]巨蜥猎手":
                        code = True
                    if n == "b'title_seasia_snhk'":
                        code = True
                    if n == "b'Terrytory_TKJJDS'":
                        code = True

        if code == True:
            break
    print(title1)


def test_titletets(int,poco):  #

    # Startgame()
    enter_title(poco)
    item1 = "item"+str(int)
    poco("ItemNewDlg(Clone)").offspring("Tabs").child(item1).click()
    print(f"开始测试     "+ poco("ItemNewDlg(Clone)").offspring("Tabs").child(item1).offspring("TextLabel").get_text()+"     的称号")
    # todo: 需添加测试模块方法
    titletest1(item1,poco)



def test_titletets0(poco):  # 普通称号
    poco = poco
    test_titletets(0,poco)
    return poco("ItemNewDlg(Clone)").child("Bg").offspring("XSys_Design_Designation").offspring("SelectedTextLabel").get_text()

def test_titletets1(poco):  # 副本称号
    poco = poco
    test_titletets(1,poco)
    return poco("ItemNewDlg(Clone)").child("Bg").offspring("XSys_Design_Designation").offspring("SelectedTextLabel").get_text()

def test_titletets2(poco):  # 巢穴称号
    poco = poco
    test_titletets(2,poco)
    return poco("ItemNewDlg(Clone)").child("Bg").offspring("XSys_Design_Designation").offspring("SelectedTextLabel").get_text()

def test_titletets3(poco):  # 战斗称号
    poco = poco
    test_titletets(3,poco)
    return poco("ItemNewDlg(Clone)").child("Bg").offspring("XSys_Design_Designation").offspring( "SelectedTextLabel").get_text()

def test_titletets4(poco):  # 活动称号
    poco = poco
    test_titletets(4,poco)
    return poco("ItemNewDlg(Clone)").child("Bg").offspring("XSys_Design_Designation").offspring("SelectedTextLabel").get_text()

def test_titletets5(poco):  # 限时称号
    poco = poco
    test_titletets(5,poco)
    return poco("ItemNewDlg(Clone)").child("Bg").offspring("XSys_Design_Designation").offspring("SelectedTextLabel").get_text()


