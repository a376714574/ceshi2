# # import requests
# #
# # sess=requests.sessions.session()
# #
# #
# # url="http://test.lemonban.com/futureloan/mvc/api/member/login"
# # data={"mobilephone":"15810447878","pwd":"123456"}
# # qqq=sess.post(url,data)
# # print(qqq.text)
# # # url="http://test.lemonban.com/futureloan/mvc/api/member/withdraw"
# # # url="http://test.lemonban.com/futureloan/mvc/api/member/list"
# # url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan"
# # # data={"mobilephone":"15810447878","pwd":"123456","":""}
# # data={"memberId":"1007","password":"123456","loanId":"2006","amount":"1000"}
# # req=sess.post(url,data)
# # print(req.text)
# #
# # sess.close()
# #
# # if req.json()["msg"] == "加标成功":  #req.json()["msg"] 她像是正则一样可以取出值来做断言
# #
# #     sql="select id from future.loan where memberid = 1008 order by id desc limit 1"#取到loan_id
# #     #需要安装jdk8 以上  需要先安装jkensi1
# #
# #     #try:
# #         # v=config.get("data",g)
# #     # except configparser.NoOptionError as e 如果配置文件里面没有loanid就会抛出异常
# #     #   if hasattr(Context,g)
# #     #   getattr(Context,g) 如果配置文件没有就从这里取出
# #
# #     #   注册成功需要判断数据库 是否有这条记录  充值成功也要判断数据库是否增加了余额=原来的钱+充值的钱
# #     #取现也是 不单单只是和返回值判断 也要和数据库进行查询然后判断
#
#
# import logging
#
# def get_log():
#
#     logger=logging.getLogger()              #收集器
#     logger.setLevel("DEBUG")
#
#
#     # console_handler=logging.StreamHandler() #输出器
#     # console_handler.setLevel("DEBUG")
#     # console_handler
#
#     #把日志级别 放入配置文件里面变成可配置的
#     file_handler=logging.FileHandler("case.log",encoding="utf-8")  # 将收集到的信息放到文件里面
#     file_handler.setLevel("DEBUG")                 #INFO级别以上的会输入到文件里面去
#
#
#     fmt="%(asctime)s-%(name)s-%(+++levelname)s-%(message)s-%(filename)s-%(lineno)d"
#     formatter=logging.Formatter(fmt=fmt)        #确定使用格式
#     file_handler.setFormatter(formatter)        #拼接
#
#     logger.addHandler(file_handler)       #输出输入拼接
#
#     return logger
#
# logging=get_log()
# logging.info("测试开始了")
# logging.error("测试报错了")
# logging.debug("测试数据")
# logging.info("测试结束了")
#

# view-tool windows-termina py界面的控制台

#可以把你安装所有的第三方模块导出到一个txt里面去 然后用pip install -r requr.txt这样就可以一次性全部安装
#在新建项目的时候 可以用virtlenv来管理不同项目的第三方模块 正常安装的第三方模块都是在python37下面
#但是通过virtlev就可以管理不同项目的第三方模块了
#gitlab和github两个托管平台

#jenkins 21：30继续看

#jenkins 可以跑脚本 定时跑  打包    实时监控任务 遇到一场可以发送邮件 平台集成服务
