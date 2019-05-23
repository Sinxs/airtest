# -*- encoding=utf8 -*-
__author__ = "Lee.li"
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import os

def sendemail(report_Name,report_Path):
    SENDER = '827435858@qq.com'
    PASSWORD = 'mjpuxtwhyatgbcga'
    RECEIVERS = ['xiaomingli@123u.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    mailtitle = '龙之谷海外版本自动化测试报告'
    report_Name = f'{report_Name}.html'
    htmlfile = report_Path + '\\' + report_Name # 获取报告路径
    accessory = MIMEApplication(open(htmlfile,'rb').read())
    accessory.add_header('Content-Disposition', 'attachment', filename=report_Name)
    try:
        message  = MIMEMultipart()
        message['From'] = Header("Lee.li",'utf-8')
        message['To'] = Header("123u.com",'utf-8')
        message['Subject'] = Header(mailtitle,'utf-8')
        # 邮件正文内容
        message.attach(MIMEText('''Dar all :
            测试报告已经生成，详情见附件！
            此次报告名称是：'''+report_Name))
        message.attach(accessory)

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(SENDER,PASSWORD)
        server.sendmail(SENDER,RECEIVERS,message.as_string())
        server.quit()
        print("邮件发送成功...")
    except smtplib.SMTPException as e:
        print('邮件发送失败...:', e)  # 打印错误