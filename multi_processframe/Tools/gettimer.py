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
import time

def get_time():
    """
    获取当前时间
    :return:  返回当前时间
    """
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return nowtime