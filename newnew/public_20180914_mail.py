#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/9/14 10:21

import yagmail
#连接服务器
mail = yagmail.SMTP("376714574@qq.com","XXXXXXXXXXX","smtp.qq.com",465)
#准备正文内容
content ='''
好久不见，你还好吗。。
我喜欢你很久了，你喜欢我吗？？
如果你也喜欢我，那么我们十一去旅游吧。
'''
#发送邮件
mail.send(["XXXXXX@qq.com","XXXXX@qq.com","XXXXX@qq.com","XXXXXX@qq.com","XXXXXX@qq.com"],
          "点开你喜欢我，不点开我喜欢你",
          content,
          "D:\\Pychram-Workspace\\Public_AutoTest\\jinmao-1.jpg")

