# -*- encoding=utf8 -*-
__author__ = "Lee.li"



from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco


def device(devices):
    """
    用于poco实例化的公用方法
    :param devices: 制定设备
    :return:
    """
    dev = connect_device("android:///" + devices)
    poco = UnityPoco(device=dev)
    return poco
