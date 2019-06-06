# -*- encoding=utf8 -*-
__author__ = "Lee.li"
"""
命名规则：
1.模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)
2.类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
3.函数名一律小写，如有多个单词，用下划线隔开，私有函数在函数前加一个下划线_
4.变量名首字母尽量小写, 如有多个单词，用下划线隔开，后续字母大写
5.常量采用全大写，如有多个单词，使用下划线隔开
"""
import os, time

def get_screen_shot(start,devices,action):
    """
    实现手机截图功能
    :param devices: 截图的设备
    :param start: 截图发生的时间
    :param action: 当时的操作描述，属于哪个测试用例下的
    :return:
    """
    report_Path = os.path.join(os.getcwd(), "Report") # 获取报告路径 D:\AirtestIDE\Case\Common\Report
    screen_Shot = os.path.join(report_Path,"Screenshot") # 获取截图路径 D:\AirtestIDE\Case\Common\Report\Screenshot
    picture_PNG = screen_Shot + "\\" +time.strftime('%Y%m%d_%H%M%S',time.localtime(start)) + "_" + "_" + action+ ".png"  # 通过传参给截图命名，时间发生的时间
    os.system("adb -s " + devices + " shell screencap -p /sdcard/screencap.png") # 调用adb命令实现截图
    file_Path = open(picture_PNG, "a+", encoding="utf-8") # 打开文件启用添加模式
    file_Path.close() # 关闭打开的文件路径
    os.system(f"adb -s {devices} pull /sdcard/screencap.png {picture_PNG}")  # 把截图放到截图路径中去
    print("<img src='" + picture_PNG + "' width=600 />") # 通过src路径获取图片，并显示出来
    return picture_PNG