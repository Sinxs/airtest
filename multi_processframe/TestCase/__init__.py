# -*- coding: utf-8 -*-
__author__ = "Lee.li"
import os
from multi_processframe.Tools import analysis

case_Path = os.path.join(os.getcwd(), "TestCase")
script_List = analysis.get_script_list(case_Path)
__all__ = script_List
