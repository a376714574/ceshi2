#to发送人   msg信息内容   attachments附件(可以有一个可以有很多个)    subject标题

import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

class MyMail:


    email_servers={"163.com":{"smtp":{"host":"smtp.163.com","port":25,"ssl_port":465}}
                   # "qq.com":巴拉巴拉 可以支持多种邮箱格式
                   }

    def parse_mail(self,mailname):

       server_name=mailname.split("@")

       #这里为1的情况就是切割失败没有@符号所以如果输入错误 切割失败只有一个元素那就是格式错误
       if len(server_name) == 1:
           raise TypeError("格式错误")

       #如果他的邮箱是wang@qiang@qq.com 如果取1取值结果就是wang如果是-1就是wang@qiang这样是对的
       server_name = server_name[-1]

       #传进来的邮箱不在email_servers的所有key里面可以写多个比如163.com比如qq.com也就是说不支持这种邮箱就告诉他
       if server_name not in list(self.email_servers.keys()):
           raise NameError("不支持这种邮箱格式")

       #经过上面的重重判断就可以到达下面了
       server=self.email_servers.get(server_name,"")