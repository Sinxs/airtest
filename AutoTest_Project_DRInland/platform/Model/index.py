# -*- coding: utf-8 -*-
__author__ = "Lee.le"
from Model.tools import *
import os
from django.shortcuts import render


def start(request):
    """
    启动脚本
    :param request:
    :return:
    """
    if request.method == 'POST':
        stop = request.POST.get("stop")  # 处理关闭按钮事件
        start = request.POST.get("start")
        if stop == "stop" or start == 'start':  # TODO 停止测试的请求处理
            for i in range(10):
                pidcmd = 'tasklist  /fi "WINDOWTITLE eq start_auto"'  # 查看进程信息
                result = os.popen(pidcmd).read()
                if '运行' not in result:
                    killcmd = 'taskkill /f /fi "WINDOWTITLE eq start_auto"'  # 杀掉进程
                    os.popen(killcmd)
                else:
                    print('已经终止了程序运行')
                    break
        else:
            packageurl = request.POST.get("packageurl")  # "http://art.123u.com/lzghwnew5/arts/t_20190603171414.apk"
            devicesnumber = request.POST.get("devicesnumber")
            email = request.POST.get("email")  # 接受报告的邮件
            check_box_list = request.POST.getlist('check_box_list') # 需要测试的模块
            steptype = request.POST.get("check_box_step")
            smoke = request.POST.get("check_box_smoke")
            performance = request.POST.get("check_box_performance") # 性能测试开关
            username = request.POST.get("username") # 账号
            password = request.POST.get("password") # 密码
            server = request.POST.get("server")
            # TODO 设备列表
            if devicesnumber != '' and devicesnumber != None:
                print(devicesnumber)
                deviceslist = get_workdevices()[0:(int(devicesnumber))]
                rewrite_config('devicesList', deviceslist)
            else:
                deviceslist = get_workdevices()[0:1]
                rewrite_config('devicesList', deviceslist)
            # TODO 实现email的重写
            if email != '':
                rewrite_config('email', email)
            # TODO 实现testcase的重写
            if 'all' in check_box_list:
                key = list(case_translate().keys())
                rewrite_config('testCase', key)
            else:
                rewrite_config('testCase', check_box_list)
            # TODO testtype重写，False是分布执行，True是单步执行
            if steptype != '' and steptype == 'substep':
                rewrite_config('testtype', 'False')
            else:
                rewrite_config('testtype', 'True')
            # TODO performancetype重写
            if steptype != '' and steptype == 'substep':
                rewrite_config('testtype', 'False')
            else:
                rewrite_config('testtype', 'True')
            if performance == 'performance':
                rewrite_config('performancetype', 'True')
            else:
                rewrite_config('performancetype', 'False')
            # TODO 实现  1. 是否安装包的重写 2.根据URL下载测试包
            if packageurl != '':
                rewrite_config("packagepath", download(packageurl))
                rewrite_config("installapk", "True")
                download(packageurl)
            else:
                rewrite_config("installapk", "False")
            # TODO 实现账号密码
            if username != '':
                if '，' in username:
                    username = username.replace('，', ',')
                rewrite_config('username', username)
            if password != '':
                rewrite_config('password', password)
            # TODO 实现服务器选择
            if server != '' and server != None:
                if server == '日补丁qq android一服':
                    server = "1server"
                else:
                    server = "2server"
                rewrite_config('server', server)
            #  TODO 实现脚本开始
            path = os.path.abspath(os.path.join(os.getcwd(), "../start.bat"))
            os.popen(f'start {path}')  # 重新打开cmd执行
            # os.popen(f'{path}')  # 当前cmd执行
    return render(request, "index.html", {'data': case_translate(), 'addr': get_addr(), 'count': len(get_workdevices())})








