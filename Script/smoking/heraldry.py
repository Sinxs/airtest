"""
纹章模块
判断纹章模块中的界面元素-点击按钮
"""
from multi_processframe.Tools import printcolor,adb_connect
devices = "127.0.0.1:62025"
def card(devices):
    poco = adb_connect.device(devices)
    