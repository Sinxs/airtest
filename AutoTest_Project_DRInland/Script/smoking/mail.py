"""
邮箱
"""
# -*- encoding=utf8 -*-
__author__ = "Sinwu"
from multi_processframe.ProjectTools import common
from airtest.core.api import *


def mail(start, devices):
    poco = common.deviceconnect(devices)
    if poco("Back").exists():
        poco("Back").click()  # 点击聊天功能
        sleep(1)
        # 点击世界频道按钮
        poco("tab1").click()
        if poco("Mail").exists():
            # 点击邮箱
            poco("Mail").click()
            if poco("MailName").exists():
                common.printgreen("进入邮箱功能")
                common.printgreen("点击邮件收取")
                poco("sqBtn").click()
                sleep(2)
                if poco("GreyModalDlg(Clone)").child("Bg").exists():
                    common.printgreen("没有可领取的邮件")
                    sleep(1)
                    poco("OK").click()
                if poco("MailDlg(Clone)").offspring("item0").exists():
                    common.printgreen("邮箱有邮件，开始进行删除测试,因为删除是没有反馈的，所以只进行点击测试，拿不到结果")
                    poco("MailDlg(Clone)").offspring("item0").child("sign").click()
                    poco("deletBtn").click()
            else:
                common.printred("没有进入邮箱界面，请检查")
                common.get_screen_shot(start, time.time(), devices, "没有进入邮箱界面")
    return poco("MailName").get_text()  # 邮 件


if __name__ == "__main__":
    start = time.localtime()
    mail(start, "e37c0280")