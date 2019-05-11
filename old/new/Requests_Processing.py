# from new_123.excel_rz import excel
# from new_123 import os_path
# from new_123.requests_GP import get_post
# from ddt import ddt,data
# from new_123.mysql_r import mysql
# import unittest
#
#
# @ddt
# class Requests_Cls(unittest.TestCase):
#
#     ex_rz=excel(excel_name=os_path.live_path,sheet="register")
#     ex_r=ex_rz.excel_read()
#     gp = get_post()
#     mysql=mysql()
#
#     @classmethod
#     def setUpClass(cls):                    #类方法不需要有实例对象直接类名。就可以引用了 cls代表的
#         cls.gp.sess_open()                   #Requests_Cls这个类
#         cls.mysql.connect()
#
#     @data(*ex_r)                          #五个测试用例ddt会生成五个test方法 而每次他都会从
#     def test_requests(self,ex_r):           #ddt开始运行所以up和down就变得非常关键self就代表实例本身
#         print(ex_r.data)
#         if ex_r.data.find("random")!=-1:
#            new=self.mysql.sql_action("select max(mobilephone) from future.member")
#            print(new[0])
#            new_1=int(new[0])+1
#            ex_r.data=ex_r.data.replace("random",str(new_1))
#            print(ex_r.data)
#         req=self.gp.req_gp(ex_r.mode,ex_r.url,ex_r.data)
#
#         try:
#             self.assertIn(str(ex_r.Exq),req)
#             self.ex_rz.excel_write(ex_r.id,req,"True")
#         except Exception as e:
#             self.ex_rz.excel_write(ex_r.id,req,"False")
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.gp.sess_close()
#         cls.mysql.mysql_close()

data='{"mobilephone":"15810447878","amount":"100"}'

print("amount" in data)