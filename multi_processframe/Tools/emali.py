# -*- encoding=utf8 -*-
__author__ = "Lee.li"
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import os

def email(reportname,report_Path):
    SENDER = 'xiaomingli@123u.com'
    PASSWORD = 'AQ2jNu4dnf2mCgZx'
    RECEIVERS = ['xiaomingli@123u.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    mailtitle = '龙之谷海外版本自动化测试报告'

    htmlfile = report_Path + '\\' + reportname
    print(htmlfile)


report_Path = os.path.join(os.getcwd(), "Report")
reportname = '123.thml'
email(reportname,report_Path)


