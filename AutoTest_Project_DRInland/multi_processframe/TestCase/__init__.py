# -*- coding: utf-8 -*-
__author__ = "Lee.li"
import os
from multi_processframe.ProjectTools.common import get_script_list

case_Path = os.path.join(os.getcwd(), "TestCase")
script_List = get_script_list(case_Path)
__all__ = script_List
