# -*- encoding=utf8 -*-
__author__ = "Lee.li"
import xlwings as xw
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import sys
import re
from airtest.core.api import *
import json
import numpy as np
import configparser  # 配置文件分析器
import traceback
import os
import time
import inspect
from PIL import Image
from airtest.core.android.adb import ADB
from poco.drivers.unity3d import UnityPoco
from multi_processframe.ProjectTools import initial

excelpath = os.path.abspath(os.path.join(os.getcwd(), "../platform/static/Report/Excel"))

"""
命名规则：
1.模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)
2.类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
3.函数名一律小写，如有多个单词，用下划线隔开，私有函数在函数前加一个下划线_
4.变量名首字母尽量小写, 如有多个单词，用下划线隔开，后续字母大写
5.常量采用全大写，如有多个单词，使用下划线隔开
"""

_print = print


def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)


config = configparser.ConfigParser()  # 实现插值的配置器


def set_config(case):
    _parentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # 获取当前文件上层路径
    _rootPath = os.path.dirname(os.path.abspath(_parentPath))  # 获取当前目录根目录
    config_Path = _rootPath + '\\config.ini'  # 获取config.ini的路径
    key = "progress"
    temp = get_value(config_Path, key)
    if case not in temp:
        temp.append(case)
    if "None" in temp:
        temp.remove("None")
    if '' in temp:
        del(temp[0])
    getdata = str(temp).replace(" ", "").replace("[", "").replace("]", "").replace("\'", "").replace("\"", "")
    if getdata != "":
        config.read(config_Path)
        config.set("config", key, getdata)
        config.write(open(config_Path, "w"))

def del_progress():
    _parentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # 获取当前文件上层路径
    _rootPath = os.path.dirname(os.path.abspath(_parentPath))  # 获取当前目录根目录
    config_Path = _rootPath + '\\config.ini'  # 获取config.ini的路径
    key = "progress"
    config.read(config_Path)
    config.set("config", key, "")
    config.write(open(config_Path, "w"))

def get_value(path, key):
    config.read(path, encoding='utf-8-sig')
    # config.read(path, encoding='GBK')
    temp = config.get('config', key)
    result_list = temp.split(',')
    return result_list


def get_script_list(file_Path):
    """
    这是一个处理TestCase目录下的模块脚本文件，获取文件名称
    :param file_Path:  文件路径，就是TestCase的路径
    :return: 返回值是是TestCase下所有需要测试的用例脚本
    """
    dir_List = os.listdir(file_Path)  # 返回包含目录中文件名的列表
    script_List = []  # 定义一个空列表，用来存储脚本模块
    for i in range(len(dir_List)):
        mode_Name = dir_List[i].split(".")  # 把模块文件分割成["name","py"]的形式赋值给mode_Name
        if mode_Name[0] != "__init__" and mode_Name[0] != "__pycache__":  # 去除构造函数和运行文件
            if mode_Name[1].lower() == "py":  # 获取所需要的模块py文件
                script_List.append(mode_Name[0])  # 把满足上两个条件的的模块名称添加给script_List
    return script_List


def deviceconnect(devices):
    """
    用于poco实例化的公用方法
    :param devices: 制定设备
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    return poco


def goback(devices):
    try:
        poco = deviceconnect(devices)
        for i in range(3):
            if poco("Close").exists():
                poco("Close").click()
            else:
                return None
    except ConnectionAbortedError as e:
        print(f"{e} 主机断开连接，杀掉游戏进程，脚本重新启动")
        initial.restart_app(devices)


def printred(mes, end='\n'):
    """
    这是打印红色加粗字体，在html显示报错信息信息d函数
    :param mes: 需要打印的信息
    :return: 返回加工后的打印内容
    """
    if end == "，" or end == ",":
        return print(f"<font color=\"red\" ><b>ERROR：</b>{mes}</font>", end="，")
    elif end == "":
        return print(f"<font color=\"red\" ><b>ERROR：</b>{mes}</font>", end=" ")
    else:
        return print(f"<font color=\"red\" ><b>ERROR：</b>{mes}</font>")


def printgreen(mes, end='\n'):
    """
    这是打印绿色字体，在html显示正确信息的函数
    :param mes: 需要打印的信息
    :return: 返回加工后的打印内容
    """
    if end == "，" or end == ",":
        return print(f"<font color=\"green\" >{mes}</font>", end="，")
    elif end == "":
        return print(f"<font color=\"green\" >{mes}</font>", end=" ")
    else:
        return print(f"<font color=\"green\" >{mes}</font>")


def printcolor(mes, color, end='\n'):
    """
    这是打印定制颜色字体，在html显示正确信息的函数
    :param mes: 需要打印的信息
    :return: 返回加工后的打印内容
    red=红
    green=绿
    """
    if end == "，" or end == ",":
        return print(f"<font color=\"{color}\" >{mes}</font>", end="，")
    elif end == "":
        return print(f"<font color=\"{color}\" >{mes}</font>", end=" ")
    else:
        return print(f"<font color=\"{color}\" >{mes}</font>")


def sendemail(report_Name, receivers):
    addr = socket.gethostbyname(socket.gethostname())
    SENDER = '827435858@qq.com'
    PASSWORD = 'mjpuxtwhyatgbcga'
    # RECEIVERS = ['xiaomingli@123u.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    mailtitle = '龙之谷国内版本自动化测试报告'
    report_Name = f'{report_Name}.html'
    # htmlfile = report_Path + '\\' + report_Name # 获取报告路径
    # accessory = MIMEApplication(open(htmlfile,'rb').read())
    # accessory.add_header('Content-Disposition', 'attachment', filename=report_Name)
    try:
        message = MIMEMultipart()
        message['From'] = Header("Lee.li", 'utf-8')
        message['To'] = Header("123u.com", 'utf-8')
        message['Subject'] = Header(mailtitle, 'utf-8')
        # 邮件正文内容
        message.attach(MIMEText('''Dar all :
            测试报告已经生成，详情见http://''' + str(addr) + ''':8000/report
            界面按F5刷新出最新测试报告，
            此报告名称是：''' + str(report_Name)))
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, receivers, message.as_string())
        server.quit()
        print("邮件发送成功...")
    except smtplib.SMTPException as e:
        print('邮件发送失败...:', e)  # 打印错误


def _get_screen_size(devices):
    '获取手机屏幕大小'
    size_str = os.popen(f'adb -s {devices} shell wm size').read()
    if not size_str:
        print('请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        sizeheight = "{height}".format(height=m.group(1))
        sizewidth = "{width}".format(width=m.group(2))
        return int(sizeheight), int(sizewidth)
    return "1920x1080"


def setswipe(type, x, y, devices):
    if type == 1:  # 1280 * 720
        devicessizi = _get_screen_size(devices)
        x0 = x[0] / 1280 * devicessizi[1]
        y0 = x[1] / 720 * devicessizi[0]
        x1 = y[0] / 1280 * devicessizi[1]
        y1 = y[1] / 720 * devicessizi[0]
        swipe((x0, y0), (x1, y1), 5)


def settouch(type, x, y, devices, times=1):
    if type == 1:  # 1280 * 720
        devicessizi = _get_screen_size(devices)
        x = x / 1280 * devicessizi[0]
        y = y / 720 * devicessizi[1]
        touch([x, y], times=times)


# -*- coding: utf-8 -*-


def create_log_json(start, nowtime, devices):
    devices_name = os.popen(f"adb -s {devices} shell getprop ro.product.name").read()
    nowstime = f'{time.strftime("%Y-%m-%d-%H-%M-%S", start)}'
    report_Name = devices_name.split()[0] + "_" + str(nowstime)
    # 获取测试报告路径
    report_path = (os.path.abspath(os.path.join(os.getcwd(), f"../platform/static/Report/{report_Name}")))
    datapath = report_path + '/data'
    create_time = time.strftime("%m%d%H%M", nowtime)
    jsonfile = datapath + f'\\{create_time}_{report_Name}_log.json'
    if os.path.exists(jsonfile):
        raise Exception("FileHasExisted")
    f = open(jsonfile, "w")
    resultData = {
        "Time_series": [],
        "TotalMemory": [],
        "AllocatedMemory": [],
        "UsedMemory": [],
        "FreeMemory": [],
        "TotalCPU": [],
        "AllocatedCPU": [],
        "FPS": [],
        "PNGAddress": [],
        "data_count": [],
    }
    f.write(json.dumps(resultData))
    f.close()
    return jsonfile


def record_to_json(jsonfilepath, list):
    for i in range(len(list)):
        if list[i] == "N/a":
            list[i] = "0"
    list[1] = float(list[1])
    list[2] = float(list[2])
    list[3] = float(list[3])
    list[4] = float(list[4])
    # todo:因为totalcpu的数值进行了处理但是allocatedcpu却没有进行相同的处理，在报告中就会显示应用占比高于总占比
    list[5] = float(list[5]) * 100
    list[6] = float(list[6]) * 100
    list[7] = float(list[7])
    f = open(jsonfilepath, "r+")
    strdata = f.read()
    f.seek(0)
    dictdata = json.loads(strdata)
    dictdata = json.loads(strdata)
    dictdata["Time_series"].append(list[0])
    dictdata["TotalMemory"].append(list[1])
    dictdata["AllocatedMemory"].append(list[2])
    dictdata["UsedMemory"].append(list[3])
    dictdata["FreeMemory"].append(list[4])
    dictdata["TotalCPU"].append(list[5])
    dictdata["AllocatedCPU"].append(list[6])
    dictdata["FPS"].append(list[7])
    dictdata["PNGAddress"].append(list[8])
    strdata = json.dumps(dictdata)
    f.write(strdata)
    f.close()


def calculate_by_json(jsonfile):
    f = open(jsonfile, "r+")
    strdata = f.read()
    f.seek(0)
    dictdata = json.loads(strdata)
    memorylist = list(dictdata["AllocatedMemory"])
    cpulist = list(dictdata["AllocatedCPU"])
    fpslist = list(dictdata["FPS"])
    while 0 in memorylist:
        memorylist.remove(0)
    while 0 in cpulist:
        cpulist.remove(0)
    while 0 in fpslist:
        fpslist.remove(0)
    Max_AllocatedMemory = max(memorylist)
    Min_AllocatedMemory = min(memorylist)
    Avg_AllocatedMemory = format(np.average(memorylist), ".2f")
    Max_AllocatedCPU = max(cpulist)
    Min_AllocatedCPU = min(cpulist)
    Avg_AllocatedCPU = format(np.average(cpulist), ".2f")
    # Max_FPS = max(fpslist)
    # Min_FPS = min(fpslist)
    # Avg_FPS = format(np.average(fpslist), ".2f")
    Max_FPS = Min_FPS = Avg_FPS = "N/a"
    # 防止对某些应用或某些机型，因取不到fps导致max函数报错因而中断流程的问题。
    if len(fpslist) != 0:
        Max_FPS = max(fpslist)
        Min_FPS = min(fpslist)
        Avg_FPS = format(np.average(fpslist), ".2f")
    dictdata["data_count"].append({"Max_AllocatedMemory": [Max_AllocatedMemory],
                                   "Min_AllocatedMemory": [Min_AllocatedMemory],
                                   "Avg_AllocatedMemory": [Avg_AllocatedMemory],
                                   "Max_AllocatedCPU": [str(Max_AllocatedCPU) + "%"],
                                   "Min_AllocatedCPU": [str(Min_AllocatedCPU) + "%"],
                                   "Avg_AllocatedCPU": [str(Avg_AllocatedCPU) + "%"],
                                   "Max_FPS": [Max_FPS], "Min_FPS": [Min_FPS],
                                   "Avg_FPS": [Avg_FPS]})
    strdata = json.dumps(dictdata)
    f.write(strdata)
    f.close()


# if __name__=="__main__":
#     jsonfile=r"D:\AirtestID\AutoTest_Project_DRInland\platform\static\Report\Excel\08051847_62001_log.json"
#     calculate_by_json(jsonfile)
#     # nowtime = time.localtime()
#     # device = "123465"
#     # create_log_json(nowtime,device)


# 创建一个log_excel用以记录性能数据
def create_log_excel(start, nowtime, devices):
    devices_name = os.popen(f"adb -s {devices} shell getprop ro.product.name").read()
    nowstime = f'{time.strftime("%Y-%m-%d-%H-%M-%S", start)}'
    report_Name = devices_name.split()[0] + "_" + str(nowstime)
    # 获取测试报告路径
    report_path = (os.path.abspath(os.path.join(os.getcwd(), f"../platform/static/Report/{report_Name}")))
    datapath = report_path + '/data'
    create_time = time.strftime('%m%d%H%M', nowtime)
    exclefile = datapath + f'\\{create_time}_{devices_name}_log.xlsx'
    app = xw.App(visible=True, add_book=False)
    wb = app.books.add()
    sheet = wb.sheets("Sheet1")
    sheet.range('A1').value = ["Time", "TotalMemory(MB)", "AllocatedMemory(MB)", "UsedMemory(MB)", "FreeMemory(MB)",
                               "TotalCPU", "AllocatedCPU", "FPS", "", "PNG", "PNGAddress"]
    sheet.range('A1:I1').color = 205, 197, 191
    print("创建Excel文件：{}".format(exclefile))
    return exclefile, sheet, wb


# 计算一个sheet里已存在的所有数据，然后返回该sheet里的各项的平均、最大、最小值。
def calculate(sheet):
    rng = sheet.range('A1').expand()
    nrow = rng.last_cell.row
    AllocatedMemory = sheet.range("C2:C{}".format(nrow)).value
    sum_UsedMemory = sheet.range("D2:D{}".format(nrow)).value
    sum_FreeMemory = sheet.range("E2:E{}".format(nrow)).value
    TotalCPU = sheet.range("F2:F{}".format(nrow)).value
    AllocatedCPU = sheet.range("G2:G{}".format(nrow)).value
    FPS = sheet.range("H2:H{}".format(nrow)).value
    JankCount = sheet.range("I2:I{}".format(nrow)).value
    sum_TotalCPU = []
    while "N/a" in AllocatedMemory:
        AllocatedMemory.remove("N/a")
    while "N/a" in AllocatedCPU:
        AllocatedCPU.remove("N/a")
    while "N/a" in FPS:
        FPS.remove("N/a")
    while "N/a" in JankCount:
        JankCount.remove("N/a")
    for i in range(len(TotalCPU)):
        tmp = float(TotalCPU[i].split("%")[0])
        sum_TotalCPU.append(tmp)
    avg_am, max_am, min_am = getcount(AllocatedMemory)
    avg_um, max_um, min_um = getcount(sum_UsedMemory)
    avg_fm, max_fm, min_fm = getcount(sum_FreeMemory)
    avg_tc, max_tc, min_tc = getcount(sum_TotalCPU)
    avg_ac, max_ac, min_ac = getcount(AllocatedCPU)
    avg_fps, max_fps, min_fps = getcount(FPS)
    avg_jc, max_jc, min_jc = getcount(JankCount)
    if avg_tc == "N/a":
        pass
    else:
        avg_tc = str(format(avg_tc, ".2f")) + "%"
        max_tc = str(format(max_tc, ".2f")) + "%"
        min_tc = str(format(min_tc, ".2f")) + "%"
    if avg_ac == "N/a":
        pass
    else:
        avg_ac = str(format(avg_ac * 100, ".2f")) + "%"
        max_ac = str(format(max_ac * 100, ".2f")) + "%"
        min_ac = str(format(min_ac * 100, ".2f")) + "%"
    avglist = ["平均值", "", avg_am, avg_um, avg_fm, avg_tc, avg_ac, avg_fps, avg_jc]
    maxlist = ["最大值：", "", max_am, max_um, max_fm, max_tc, max_ac, max_fps, max_jc]
    minlist = ["最小值：", "", min_am, min_um, min_fm, min_tc, min_ac, min_fps, min_jc]
    return avglist, maxlist, minlist


# 统计一个list的平均、最大、最小值
def getcount(list):
    sum = avg = max = min = 0
    flag = 0
    try:
        for Na in list:
            flag = flag + 1
            if flag == 1:
                sum = float(Na)
                max = float(Na)
                min = float(Na)
            else:
                sum = sum + float(Na)
                if float(Na) > max:
                    max = float(Na)
                elif float(Na) < min:
                    min = float(Na)
    except Exception as e:
        print(e)
    if sum == 0:
        avg = "N/a"
        max = "N/a"
        min = "N/a"
    else:
        avg = float(format(sum / flag, ".2f"))
    return avg, max, min


# 读取传过来的list和excel，将list写入excel的下一行
def record_to_excel(sheet, list, **kwargs):
    rng = sheet.range('A1').expand()
    nrow = rng.last_cell.row
    currentcell = "A" + str(nrow + 1)
    currentcellpng = "J" + str(nrow + 1)
    currentcellpngvalue = "K" + str(nrow + 1)
    currentcellrange = currentcell + ":" + "H" + str(nrow + 1)
    sheet.range(currentcell).value = list
    if nrow % 2 == 0:
        sheet.range(currentcellrange).color = 173, 216, 230
    else:
        sheet.range(currentcellrange).color = 221, 245, 250
    for key, value in kwargs.items():
        if key == "color":
            sheet.range(currentcellrange).color = value
        if key == "png":
            sheet.range(currentcellpng).add_hyperlink(value, "截图", "提示：点击打开截图")
            sheet.range(currentcellpngvalue).value = value
    sheet.autofit()


# 在excel里查找指定键名的列，将该列所有数值（不算最后3行统计行）返回成一个serieslist
def get_series(sheet, Key):
    rng = sheet.range('A1').expand()
    nrow = rng.last_cell.row - 3
    rng2 = sheet.range('A1:K1')
    serieslist = []
    for key in rng2:
        if key.value == Key:
            cum = key.address
            cum = cum.split("$")[1]
            tmp = cum + "2:" + cum + str(nrow)
            serieslist = sheet.range(tmp).value
            break
    if Key == "TotalCPU":
        for i in range(len(serieslist)):
            serieslist[i] = float(
                format(float(serieslist[i].split("%")[0]) / float(serieslist[i].split("%")[1].split("/")[1]) * 100,
                       "0.2f"))
            if serieslist[i] == "N/a":
                serieslist[i] = 0
    if Key == "AllocatedCPU":
        for i in range(len(serieslist)):
            if serieslist[i] == "N/a":
                serieslist[i] = 0
            else:
                serieslist[i] = float(format(float(serieslist[i]) * 100, "0.2f"))

    return serieslist


# 在序列表里查询指定键值对，转成json返回
def get_json(sheet, Key):
    series = get_series(sheet, Key)
    series_json = json.dumps({Key: series})
    return series_json


adb = ADB().adb_path


# 用来给设备初始化MiniCap的，介绍见 https://blog.csdn.net/saint_228/article/details/92142914
def ini_MiniCap(devices):
    try:
        parent_path = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".")
        root_path = os.path.abspath(os.path.dirname(parent_path) + os.path.sep + ".")
        ABIcommand = adb + " -s {} shell getprop ro.product.cpu.abi".format(devices)
        ABI = os.popen(ABIcommand).read().strip()
        AndroidVersion = os.popen(adb + " -s {} shell getprop ro.build.version.sdk".format(devices)).read().strip()
        airtest_minicap_path = os.path.abspath(
            os.path.dirname(root_path) + os.path.sep + ".") + "\\airtest\\core\\android\\static\\stf_libs"
        airtest_minicapso_path = os.path.abspath(os.path.dirname(
            root_path) + os.path.sep + ".") + "\\airtest\\core\\android\\static\\stf_libs\\minicap-shared\\aosp\\libs\\" + "android-{}\\{}\\minicap.so".format(
            AndroidVersion, ABI)
        push_minicap = adb + " -s {} push {}/{}/minicap".format(devices, airtest_minicap_path,
                                                                ABI) + " /data/local/tmp/"
        push_minicapso = adb + " -s {} push {}".format(devices, airtest_minicapso_path) + " /data/local/tmp/"
        os.popen(push_minicap)
        os.popen(push_minicapso)
        chmod = adb + " -s {} shell chmod 777 /data/local/tmp/*".format(devices)
        os.popen(chmod)
        wm_size_command = adb + " -s {} shell wm size".format(devices)
        vm_size = os.popen(wm_size_command).read()
        vm_size = vm_size.split(":")[1].strip()
        start_minicap = adb + " -s {} shell LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P {}@{}/0 -t".format(
            devices, vm_size, vm_size)
        result = os.popen(start_minicap).read()
        print(result)
        print("设备{}上已经成功安装并开启了MiniCap。".format(devices))
    except Exception as e:
        print(e, traceback.format_exc())


def get_screen_shot(start, starttime, devices, action):
    """
    实现手机截图功能
    :param devices: 截图的设备
    :param start: 截图发生的时间
    :param action: 当时的操作描述，属于哪个测试用例下的
    :return:
    """
    devices_name = os.popen(f"adb -s {devices} shell getprop ro.product.name").read()
    nowtime = f'{time.strftime("%Y-%m-%d-%H-%M-%S", start)}'
    report_Name = devices_name.split()[0] + "_" + str(nowtime)
    # 获取测试报告路径
    report_path = (os.path.abspath(os.path.join(os.getcwd(), f"../platform/static/Report/{report_Name}")))
    screenpath = report_path + '/Screenshot'
    pngtime = time.strftime('%Y%m%d_%H%M%S', time.localtime(starttime))
    picture_PNG = screenpath + "\\" + pngtime + "_" + "_" + action + ".png"
    packname = pngtime + "_" + "_" + action + ".png"
    os.system("adb -s " + devices + " shell screencap -p /sdcard/screencap.png")  # 调用adb命令实现截图
    file_Path = open(picture_PNG, "a+", encoding="utf-8")  # 打开文件启用添加模式
    file_Path.close()  # 关闭打开的文件路径
    time.sleep(1)
    os.system(f"adb -s {devices} pull /sdcard/screencap.png {picture_PNG}")  # 把截图放到截图路径中去
    time.sleep(1)
    print(
        "<img src='" + f"\static\Report\{report_Name}\Screenshot\\" + packname + "' width=600 />")  # 通过src路径获取图片，并显示出来
    return picture_PNG


def GetScreen(start, starttime, devices, action):
    ABIcommand = adb + " -s {} shell getprop ro.product.cpu.abi".format(devices)
    ABI = os.popen(ABIcommand).read().strip()
    if ABI == "x86":
        png = GetScreenbyADBCap(start, starttime, devices, action)
    else:
        try:
            png = GetScreenbyMiniCap(start, starttime, devices, action)
        except:
            print("MiniCap截图失败，换ADB截图")
            png = GetScreenbyADBCap(start, starttime, devices, action)
    return png


# 用ADBCAP的方法截图
def GetScreenbyADBCap(start, starttime, devices, action):
    devices_name = os.popen(f"adb -s {devices} shell getprop ro.product.name").read()
    nowtime = f'{time.strftime("%Y-%m-%d-%H-%M-%S", start)}'
    report_Name = devices_name.split()[0] + "_" + str(nowtime)
    # 获取测试报告路径
    report_path = (os.path.abspath(os.path.join(os.getcwd(), f"../platform/static/Report/{report_Name}")))
    screenpath = report_path + '/Screenshot'
    # 先给昵称赋值，防止生成图片的命名格式问题。
    if ":" in devices:
        nickname = devices.split(":")[1]
    else:
        nickname = devices
    pngtime = time.strftime('%Y%m%d_%H%M%S', time.localtime(starttime))
    png = screenpath + "\\" + pngtime + nickname + "_" + action + ".png"
    pngname = pngtime + nickname + "_" + action + ".png"
    os.system(adb + " -s " + devices + " shell screencap -p /sdcard/screencap.png")
    time.sleep(1)
    fp = open(png, "a+", encoding="utf-8")
    fp.close()
    os.system(adb + " -s " + devices + " pull /sdcard/screencap.png " + png)
    time.sleep(0.5)
    # ADB截图过大，需要压缩，默认压缩比为0.2，全屏。
    compressImage(png)
    print("<img src='" + f"\static\Report\{report_Name}\Screenshot\\" + pngname + "' width=600 />")
    return png


# 用MiniCap的方法截图，使用前需要确保手机上已经安装MiniCap和MiniCap.so。一般用过STF和airtestide的手机会自动安装，若未安装，则可以执行Init_MiniCap.py，手动安装。
def GetScreenbyMiniCap(start, starttime, devices, action):
    devices_name = os.popen(f"adb -s {devices} shell getprop ro.product.name").read()
    nowtime = f'{time.strftime("%Y-%m-%d-%H-%M-%S", start)}'
    report_Name = devices_name.split()[0] + "_" + str(nowtime)
    # 获取测试报告路径
    report_path = (os.path.abspath(os.path.join(os.getcwd(), f"../platform/static/Report/{report_Name}")))
    screenpath = report_path + '/Screenshot'
    # 先给昵称赋值，防止生成图片的命名格式问题。
    if ":" in devices:
        nickname = devices.split(":")[1]
    else:
        nickname = devices
    # 创建图片
    pngtime = time.strftime('%Y%m%d_%H%M%S', time.localtime(starttime))
    png = screenpath + "\\" + pngtime + nickname + "_" + action + ".png"
    pngname = pngtime + nickname + "_" + action + ".png"

    # 获取设备分辨率
    wmsizecommand = f"adb  -s {devices} shell wm size"
    size = os.popen(wmsizecommand).read()
    size = size.split(":")[1].strip()
    slist = size.split("x")
    size = slist[1] + "x" + slist[0]
    # 将设备号和分辨率填入minicap的命令，获得截图。
    screen = f"adb -s {devices} shell \"LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P {size}@{size}/0 -s > /sdcard/screencap.png\""
    os.system(screen)
    time.sleep(0.5)
    os.system(adb + " -s " + devices + " pull /sdcard/screencap.png " + png)
    print("<img src='" + f"\static\Report\{report_Name}\Screenshot\\" + pngname + "' width=600 />")
    return png

    # 图片压缩批处理，cr为压缩比，其他参数为屏幕截取范围


def compressImage(path, cr=0.7, left=0, right=1, top=0, buttom=1):
    # 打开原图片压缩
    sImg = Image.open(path)
    w, h = sImg.size  # 获取屏幕绝对尺寸
    box = (int(w * left), int(h * top), int(w * right), int(h * buttom))
    sImg = sImg.crop(box)
    time.sleep(0.1)
    # 设置压缩尺寸和选项
    dImg = sImg.resize((int(w * cr), int(h * cr)), Image.ANTIALIAS)
    time.sleep(0.1)
    # 压缩图片路径名称
    dImg.save(path)  # save这个函数后面可以加压缩编码选项JPEG之类的