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
import configparser  # 配置文件分析器
import os

def analysis_config(path,section):
    """
    读取配置文件并且获得的值返回一个列表,对单个的value，到时候可以用[0]来取到
    :param path: 路径，要写绝对路径 D:/scriprt/auto_test.air/Common/config.ini
    :param section: 你需要在配置文件中查找的值
    :return:
    """
    config = configparser.ConfigParser() # 实现插值的配置器
    config.read(path) # 读取和分析文件名或可读取的文件名
    result = config.get("config",section) # configf是配置文件中的打标签，需要根据配置文件中填写
    result_list = result.split(",") # 用逗号分隔，存储在列表中
    return result_list

def get_script_list(file_Path):
    """
    这是一个处理TestCase目录下的模块脚本文件，获取文件名称
    :param file_Path:  文件路径，就是TestCase的路径
    :return: 返回值是是TestCase下所有需要测试的用例脚本
    """
    dir_List = os.listdir(file_Path) # 返回包含目录中文件名的列表
    script_List = [] # 定义一个空列表，用来存储脚本模块
    for i in range(len(dir_List)):
        mode_Name = dir_List[i].split(".") # 把模块文件分割成["name","py"]的形式赋值给mode_Name
        if mode_Name[0] != "__init__" and mode_Name[0] != "__pycache__": # 去除构造函数和运行文件
            if mode_Name[1].lower() == "py": # 获取所需要的模块py文件
                script_List.append(mode_Name[0]) # 把满足上两个条件的的模块名称添加给script_List
    return script_List
