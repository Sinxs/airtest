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
def printred(mes):
    """
    这是打印红色加粗字体，在html显示报错信息信息d函数
    :param mes: 需要打印的信息
    :return: 返回加工后的打印内容
    """
    return print(f"<font color=\"red\" ><b>{mes}</b></font>")

def printgreen(mes):
    """
    这是打印绿色字体，在html显示正确信息的函数
    :param mes: 需要打印的信息
    :return: 返回加工后的打印内容
    """
    return print(f"<font color=\"green\" >{mes}</font>")