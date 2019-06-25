# -*- coding: utf-8 -*-
__author__ = "Lee.le"

import sys,os
config_Path = os.path.dirname(os.path.join(os.getcwd()))
sys.path.extend([config_Path])

from multi_processframe.Tools import multiprocessing

def begin():
    multiprocessing.main()


if __name__ == '__main__':
   begin()
