import os
import sys
import json
import re
def _get_screen_size(devices):
    '获取手机屏幕大小'
    size_str = os.popen(f'adb -s {devices} shell wm size').read()
    if not size_str:
        print('请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        sizeheight = "{height}".format(height=m.group(1))
        sizewidth = "{width}".format(width=m.group(2))
        return int(sizeheight),int(sizewidth)
    return "1920x1080"
