# -*- coding: utf-8 -*-
__author__ = "Lee.le"

import random
import traceback
from collections import deque
from multi_processframe.ProjectTools.common import *
from multi_processframe.ProjectTools.androidtools import *


# reportpath = os.path.abspath(os.path.join(os.getcwd(), "../platform/static/Report"))
csspath = os.path.abspath(os.path.join(os.getcwd(), "../platform/static/assets/css/app.css"))
jspath = os.path.abspath(os.path.join(os.getcwd(), "../platform/static/Report/script/app.js"))
htmlpath = os.path.abspath(os.path.join(os.getcwd(), "../platform/templates/performance.html"))
headerpath = os.path.abspath(os.path.join(os.getcwd(), "../platform/templates/header.html"))


def firstinstall2(devices):
    while True:
        try:
            poco = common.deviceconnect(devices)
            sleep(5)
            poco("Duck").wait_for_appearance(150)
            print("游戏二次加载完成，开始进行性能测试....")
            sleep(10)
            return
        except:
            print("游戏还未加载完成。请稍后...")
def firstinstall(devices):
    sleep(200)
    while True:
        try:
            poco = common.deviceconnect(devices)
            sleep(5)
            poco("Duck").wait_for_appearance(150)
            print("游戏首次加载完成，等待游戏重启....")
            sleep(30)
            firstinstall2(devices)
            return
        except:
            print("游戏还未加载完成。请稍后...")


def enter_performance(sample, flag, start, storage_by_excel=True):
    devices = sample.get_momentdevices()  # 获取当前连接的设备
    time.sleep(20)
    if sample.get_installapk() == "True":
        print(f"设备{devices}正在重新安装测试包.................")
        firstinstall(devices)
    jsonfilepath = ""
    # wb = ""
    # 创表
    # if storage_by_excel:
    #     filepath, sheet, wb = create_log_excel(start, time.localtime(), sample.get_momentdevices())
    #     collect_data(start, sample, flag, storage_by_excel, sheet=sheet,)
    #     avglist, maxlist, minlist = calculate(sheet)
    #     record_to_excel(sheet, avglist, color=(230, 230, 250))
    #     record_to_excel(sheet, maxlist, color=(193, 255, 193))
    #     record_to_excel(sheet, minlist, color=(240, 255, 240))
    #     wb.save()
    #     # nowtime = f'{time.strftime("%Y-%m-%d-%H-%M-%S", start)}'
    #     # devices_name = os.popen(f"adb -s {sample.get_momentdevices()} shell getprop ro.product.name").read()
    #     # filename = reportpath + '\\' + devices_name.split()[0] + "_" + str(nowtime) + ".html"
    #     # editreport(filename, wb, avglist, maxlist, minlist)
    #     # nowtime = f'{time.strftime("%Y-%m-%d-%H-%M-%S", start)}'
    #     # devices_name = os.popen(f"adb -s {sample.get_momentdevices()} shell getprop ro.product.name").read()
    #     # filename = reportpath + '\\' + devices_name.split()[0] + "_" + str(nowtime) + ".html"
    #     # print("要操作的文件名为：", filename)
    #     # editreport(filename, wb, avglist, maxlist, minlist)
    # else:
    #     # 创建json文件
    #     jsonfilepath = create_log_json(start, time.localtime(), sample.get_momentdevices())
    #     print(f"创建json文件成功:{jsonfilepath}")
    #     collect_data(start, sample, flag, storage_by_excel, jsonfilepath=jsonfilepath)
    #     calculate_by_json(jsonfilepath)
    jsonfilepath = create_log_json(start, time.localtime(), sample.get_momentdevices())
    print(f"创建json文件成功:{jsonfilepath}")
    collect_data(start, sample, flag, storage_by_excel, jsonfilepath=jsonfilepath)
    calculate_by_json(jsonfilepath)
    nowtime = f'{time.strftime("%Y-%m-%d-%H-%M-%S", start)}'
    devices_name = os.popen(f"adb -s {sample.get_momentdevices()} shell getprop ro.product.name").read()

    report_Name = devices_name.split()[0] + "_" + str(nowtime)
    # 获取测试报告路径
    report_path = (os.path.abspath(os.path.join(os.getcwd(), f"../platform/static/Report/{report_Name}")))
    filename = report_path + '/' + devices_name.split()[0] + "_" + str(nowtime) + ".html"
    # if storage_by_excel:
    #     editreport(filename, storage_by_excel, avglist, maxlist, minlist, wb=wb)
    # else:
    #     editreport(filename, storage_by_excel, jsonfilepath=jsonfilepath)
    editreport(filename, storage_by_excel, jsonfilepath=jsonfilepath)


def collect_data(start, sample, flag, storage_by_excel, sheet="", jsonfilepath="", timeout=3600):
    print("nowjsonfile=", jsonfilepath)
    starttime = time.time()
    dequelist = deque([])
    n = 0
    try:
        while True:
            n += 1
            if (time.time() - starttime > timeout) or (flag.value == 1 and n > 3):
                break
            total = allocated = used = free = totalcpu = allocatedcpu = ""
            get_allocated_memory = mythread(sample.get_allocated_memory, args=())  # 判断给定设备运行指定apk时的内存占用
            get_memory_info = mythread(sample.get_memoryinfo, args=())  # 一次dump获取Total/Free/Used内存
            get_total_cpu = mythread(sample.get_totalcpu, args=())  # CPU总占用，os8以上CPU不一定是100%，
            get_allocated_cpu = mythread(sample.get_allocated_cpu, args=())  # 获取运行的测试包占用的cpu
            get_png = mythread(GetScreen, args=(start, time.time(), sample.get_momentdevices(), 'performance'))
            threadlist = []
            for i in range(8):
                get_fps = mythread(sample.get_fps, args=())
                threadlist.append(get_fps)
            # 批量执行
            get_allocated_memory.start()
            get_memory_info.start()
            get_total_cpu.start()
            get_allocated_cpu.start()
            get_png.start()
            for p in threadlist:
                p.start()
                temp = p.get_result()
                if temp == 'N/a':
                    temp = 0
                if len(dequelist) < 9:
                    dequelist.append(temp)
                else:
                    dequelist.popleft()
                    dequelist.append(temp)
            fps = max(dequelist)
            # 批量获取结果
            allocated = get_allocated_memory.get_result()
            total, free, used = get_memory_info.get_result()
            totalcpu, maxcpu = get_total_cpu.get_result()
            allocatedcpu = get_allocated_cpu.get_result()
            png = get_png.get_result()

            # 批量收回线程
            get_allocated_memory.join()
            get_memory_info.join()
            get_total_cpu.join()
            get_allocated_cpu.join()
            get_png.join()
            get_fps.join()
            for q in threadlist:
                q.join()
            if maxcpu == '':
                maxcpu = '100%'
            nowtime = time.localtime()
            inputtime = str(time.strftime('%H:%M:%S', nowtime))
            if storage_by_excel:
                templist = ["'" + inputtime, total, allocated, used, free, totalcpu + '/' + maxcpu, allocatedcpu, fps]
                record_to_excel(sheet, templist, png=png)
            else:
                # todo:因为totalcpu的数值进行了处理但是allocatedcpu却没有进行相同的处理，在报告中就会显示应用占比高于总占比
                templist = [inputtime, total, allocated, used, free,
                        format(float(totalcpu.split("%")[0]) / float(maxcpu.split("%")[0]), ".2f"),
                            format(float(allocatedcpu.split("%")[0]) / float(maxcpu.split("%")[0]), ".2f"), fps,png]
                record_to_json(jsonfilepath, templist)

    except Exception as e:
        print(sample.get_momentdevices() + traceback.format_exc())


class mythread(threading.Thread):
    def __init__(self, func, args=()):
        super(mythread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        threading.Thread.join(self)  # 等待线程执行完毕
        try:
            return self.result
        except Exception as e:
            print(traceback.format_exc())
            return None


def editreport(path, storage_by_excelavglist, avglist="", maxlist="", minlist="",  wb="", jsonfilepath=""):
    # 读取报告
    temp = open(path, 'r+', encoding='UTF-8')
    fr = temp.read()
    temp.close()

    # 拼接css样式
    fr_prev, fr_next = gethtmlcontent(fr, "</style>", True, 1)
    css = open(csspath, "r+", encoding='UTF-8')
    css_str = css.read()
    css.close()
    fr = fr_prev + "\n" + css_str + "\n" + fr_next

    # 拼接头部按钮
    fr_prev, fr_next = gethtmlcontent(fr, "<div", False, 3)
    header = open(headerpath, "r+", encoding='UTF-8')
    header_str = header.read()
    header.close()
    fr = fr_prev + "\n" + header_str + "\n" + fr_next

    # 添加功能测试标签
    fr_prev, fr_next = gethtmlcontent(fr, "class=", False, 8)
    fr = fr_prev + 'id="functionReport" ' + fr_next

    # 拼接页面主题
    fr_prev, fr_next = gethtmlcontent(fr, "<script", False, 1)
    performance = open(htmlpath, "r+", encoding='UTF-8')
    performance_str = performance.read()
    performance.close()
    fr = fr_prev + "\n" + performance_str + "\n" + fr_next

    # 拼接js
    fr_prev, fr_next = gethtmlcontent(fr, "</body>", True, 1)
    js = open(jspath, "r+", encoding='UTF-8')
    js_str = js.read()
    js.close()
    fr = fr_prev + "\n" + js_str + "\n" + fr_next

    # 嵌入性能测试结果
    if storage_by_excelavglist:
        sheet = wb.sheets("Sheet1")
        Time_series = get_json(sheet, "Time")
        TotalMemory = get_json(sheet, "TotalMemory(MB)")
        AllocatedMemory = get_json(sheet, "AllocatedMemory(MB)")
        UsedMemory = get_json(sheet, "UsedMemory(MB)")
        FreeMemory = get_json(sheet, "FreeMemory(MB)")
        TotalCPU = get_json(sheet, "TotalCPU")
        AllocatedCPU = get_json(sheet, "AllocatedCPU")
        FPS = get_json(sheet, "FPS")
        PNGdata = eval(get_json(sheet, "PNGAddress"))
        temp = []
        for key in PNGdata:
            for value in PNGdata[key]:
                PNGdata[key] = value.split("platform")[1]
                temp.append(PNGdata[key])
        PNG = str({"PNGAddress": temp})
        Max_AllocatedMemory = maxlist[2]
        Min_AllocatedMemory = minlist[2]
        Avg_AllocatedMemory = avglist[2]
        Max_AllocatedCPU = maxlist[6]
        Min_AllocatedCPU = minlist[6]
        Avg_AllocatedCPU = avglist[6]
        Max_FPS = maxlist[7]
        Min_FPS = minlist[7]
        Avg_FPS = avglist[7]
        data_count = {"Max_AllocatedMemory": [Max_AllocatedMemory], "Min_AllocatedMemory": [Min_AllocatedMemory],
                      "Avg_AllocatedMemory": [Avg_AllocatedMemory], "Max_AllocatedCPU": [Max_AllocatedCPU],
                      "Min_AllocatedCPU": [Min_AllocatedCPU], "Avg_AllocatedCPU": [Avg_AllocatedCPU], "Max_FPS": [Max_FPS],
                      "Min_FPS": [Min_FPS], "Avg_FPS": [Avg_FPS]}
        data_count = "\n" + "var data_count=" + json.dumps(data_count)
    else:
        jsondata = open(jsonfilepath, "r+", encoding='UTF-8')
        jsondata = json.load(jsondata)
        Time_series = json.dumps({"Time": jsondata["Time_series"]})
        TotalMemory = json.dumps({"TotalMemory(MB)": jsondata["TotalMemory"]})
        AllocatedMemory = json.dumps({"AllocatedMemory(MB)": jsondata["AllocatedMemory"]})
        UsedMemory = json.dumps({"UsedMemory(MB)": jsondata["UsedMemory"]})
        FreeMemory = json.dumps({"FreeMemory(MB)": jsondata["FreeMemory"]})
        TotalCPU = json.dumps({"TotalCPU": jsondata["TotalCPU"]})
        AllocatedCPU = json.dumps({"AllocatedCPU": jsondata["AllocatedCPU"]})
        FPS = json.dumps({"FPS": jsondata["FPS"]})
        PNG = json.dumps({"PNGAddress": jsondata["PNGAddress"]})

        PNGdata = eval(json.dumps({"PNGAddress": jsondata["PNGAddress"]}))
        temp = []
        for key in PNGdata:
            for value in PNGdata[key]:
                PNGdata[key] = value.split("platform")[1]
                temp.append(PNGdata[key])
        PNG = str({"PNGAddress": temp})
        data_count = json.dumps(jsondata["data_count"])
        data_count = data_count[1:-1]
        data_count = "\n" + "var data_count=" + data_count

    data_series = Time_series + "\n" + "var TotalMemory=" + TotalMemory + "\n" + "var AllocatedMemory=" + \
                  AllocatedMemory + "\n" + "var UsedMemory=" + UsedMemory + "\n" + "var FreeMemory=" \
                  + FreeMemory + "\n" + "var TotalCPU=" + TotalCPU + "\n" + "var AllocatedCPU=" + AllocatedCPU + "\n" + \
                  "var FPS=" + FPS + "\n" + "var PNG=" + PNG + "\n"
    fr_prev, fr_next = gethtmlcontent(fr, "// tag data", False, 1)
    fr = fr_prev + data_series + "\n" + data_count + "\n" + fr_next


    # 写入文件
    newPath = path.replace(".html", ".html")
    f = open(newPath, "w", encoding="UTF-8")
    f.write(fr)
    f.close()
    return newPath



# 获取需要插入性能图表的节点
def gethtmlcontent(content, tag, reverse=False, round_num=1):
    fr_index = ''
    if reverse:
        fr_index = content.rfind(tag)
    else:
        fr_index = content.find(tag)
    for i in range(1, round_num):
        if reverse:
            fr_index = content.rfind(tag, 0, fr_index)
        else:
            fr_index = content.find(tag, fr_index + 1)
    fr_prev = content[0:fr_index]
    fr_next = content[fr_index:len(content)]
    return fr_prev, fr_next
