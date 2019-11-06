# -*- coding: utf-8 -*-
__author__ = "Lee.le"
import sys, time
import hashlib
import difflib
import os
from multiprocessing import Pool,Queue

_print = print


def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)


def read_file(filename):
    """
    读取文件
    :param filename:
    :return:
    """
    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            return f.readlines()
    except IOError:
        print(f"ERROR: 没有找到文件:{filename}或读取文件失败！")
        sys.exit(1)


def compare_file(file_old, file_new):
    """
    对比两个文件的差异
    :param file_old: 第一个文件
    :param file_new: 第二个文件
    :return:
    """
    name = file_old.split('\\')[-1]
    path = os.path.abspath(os.getcwd())
    out_file = f'{path}\\result\\{name}.html'
    print(f'开始对比-------{name}')
    file1_content = read_file(file_old)
    file2_content = read_file(file_new)
    d = difflib.HtmlDiff()
    result = d.make_file(file1_content, file2_content)
    with open(out_file, 'w', encoding='UTF-8') as f:
        f.writelines(result)
    print(f'完成对比-------{name}')


def file_check(path, i):
    """
    文件筛选
    :param path: 路径
    :param i: 路径标识，用于区分两个文件的返回内容
    :return:
    """
    dir_list = os.listdir(path)  # 返回包含目录中文件名的列表
    temp_old = []  # 定义一个列表，用来存储文件路径
    temp_new = []
    for file in range(len(dir_list)):
        if '.txt.meta' not in dir_list[file]:
            if i == 0:
                temp_old.append(dir_list[file])
            elif i == 1:
                temp_new.append(dir_list[file])
    if i == 0:
        return temp_old
    elif i == 1:
        return temp_new


def md5_check(file_old, file_new):
    """
    md5检查，过滤没有变动的文件
    :param file_old: 第一个文件
    :param file_new: 第二个文件
    :return:
    """
    name = file_old.split('\\')[-1]
    fp1 = open(file_old, 'rb')
    contents = fp1.read()
    fp1.close()
    old_md5 = hashlib.md5(contents).hexdigest()
    fp2 = open(file_new, 'rb')
    contents = fp2.read()
    fp2.close()
    new_md5 = hashlib.md5(contents).hexdigest()
    if old_md5 == new_md5:
        # print(f'文件{name}没有变化')
        return False
    else:
        return True


def remain_file(old, report_html):
    """
    检测生成测试报告的数量和对比文件的数量一致说明已经全部检测完毕
    :param old: 全部待对比的文件
    :param report_html: 已经生成的测试报告
    :return:
    """
    tempcount = []  # 定义一个空的全部表报告列表
    for i in range(len(old)):
        tempcount.append(old[i].replace('.txt', '.txt.html'))
    while True:
        time.sleep(60)
        path = os.path.abspath(os.getcwd())
        out_file = f'{path}\\result'
        report_list = os.listdir(out_file)  # 这个是已经生成的报告
        temp_list = report_list + report_html  # 这个是不需要对比和生成的报告的拼接列表
        for x in temp_list:
            if x in tempcount:
                tempcount.remove(x)
        if len(tempcount) == 0:
            break
        else:
            print(f"还有---【{len(tempcount)}】---个表格没有对比出结果，表格如下")
            filecount = []
            for y in tempcount:
                filecount.append(y.split('.')[0])
            print(filecount)


if __name__ == '__main__':
    path = os.path.abspath(os.getcwd())
    file_path = [f'{path}\\old', f'{path}\\new']
    old = file_check(file_path[0], 0)
    print(f"一共{len(old)}个文件需要对比,文件对比开始...")
    report_html = []
    p = Pool(9)
    for i in range(len(old)):
        file_old = file_path[0] + f'\\{old[i]}'
        file_new = file_path[1] + f'\\{old[i]}'
        results = md5_check(file_old, file_new)
        if results:
            p.apply_async(compare_file, args=(file_old, file_new, ))
        else:
            report_html.append(file_old.split('\\')[-1].replace('.txt', '.txt.html'))
    remain_file(old, report_html)
    p.close()
    p.join()
    print('文件对比结束!')
    print(time.asctime(time.localtime()))


