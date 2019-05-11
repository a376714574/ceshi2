 import ssl
from smtplib import SMTP_SSL,SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from enail.a_01 import *
import requests
class MyEmail():

    def __init__(self,mailname,pwd):
        self.mailname=mailname
        server=MyMail().parse_mail(mailname).get("smtp","")
        self.server=SMTP(server.get("host"),server.get("port"))

        #登陆
        self.server.login(mailname,pwd)

    # def mail_msg(self,msg,type="html",subject=""):
    #     msg=MIMEText(msg,type)
    #     msg["Subjet"]=subject
                                         #type可以做写多个类型
    def send_mail(self,to,msg,files=None,type="plain",subject=""):
        total=MIMEMultipart
        total["Subject"]=subject

        #判断files不是为空 然后他是一个列表
        if files and isinstance(files,list):
            for asd in files:
                file = MIMEApplication(open(asd,"rb").read())
                file.add_header("Content-Disposition","attachment",filename=asd)
                total.attach(file)
         return self.server.sendmail(self.mailname,to,total.as_string())