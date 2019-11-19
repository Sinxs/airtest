"""
背包
"""
# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from multi_processframe.ProjectTools.common import *
from airtest.core.api import *


def case(start, devices):
    print(start, devices)
    uwa_dot(1)
    get_screen_shot(start, time.time(), devices, "瞎几把截个图")
    uwa_dot(2)
    sleep(3)
    uwa_dot(10)
    sleep(5)
    uwa_dot(25)
    sleep(5)
    uwa_dot(30)
    sleep(5)
    uwa_dot(100)
    return 1


if __name__ == "__main__":
    start = time.localtime()
    case(start, "9b57691d")