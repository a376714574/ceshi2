import unittest
from ddt import data,ddt
from new.excel_rw import excel
from new.config import os_path
from new.requests_gp import Req_PG
from new.formula_re import formula_class
import re
from new.mysql_rw import mysql
from new.logs.logger import get_log

@ddt
class HQ(unittest.TestCase):

    excel=excel(os_path.excel_new, "recharge")
    sheet="recharge"
    excel_r=excel.excel_r()
    formula_class=formula_class()
    mysql=mysql()
    gp=Req_PG()
    logger=get_log(__name__)

    @classmethod
    def setUpClass(cls):
        cls.logger.info("测试开始")
        cls.gp.req_open()
        cls.formula_class.formula_open()
        cls.mysql.mysql_connect(host="test.lemonban.com",user="test",password="test",port=3306)


    def sql(self, formula_sql, act):
        object = re.search(formula_sql, act)  # 原本的sql取出值来
        print(object)
        print(object.group(1),"-------------------------")
        print(self.mysql.mysql_sql(object.group(1)))
        return self.mysql.mysql_sql(object.group(1))


    def recharge(self, formula_sql, mode, url, data, act):
        sql_m = self.sql(formula_sql, act)
        try:
            self.req(mode=mode, url=url, data=data)
            print(sql_m + int(eval(data)["amount"]))
            print(self.sql(formula_sql, act))
            print(type(self.sql(formula_sql, act)))
            sql_m + int(eval(data)["amount"]) == self.sql(formula_sql, act)
        except:
            print(sql_m)
            print(self.sql(formula_sql, act))
            sql_m == self.sql(formula_sql, act)

    def bidLoan(self, formula_sql, mode, url, data, act):
        sql_m = self.sql(formula_sql, act)
        try:
            self.req(mode=mode, url=url, data=data)
            print(sql_m + int(eval(data)["amount"]))
            print(self.sql(formula_sql, act))
            print(type(self.sql(formula_sql, act)))
            sql_m - self.sql(formula_sql, act) == int(eval(data)["amount"])
        except:
            print(sql_m)
            print(self.sql(formula_sql, act))
            sql_m == self.sql(formula_sql, act)


    def req(self,mode,url,data):
        req=self.gp.req_pg(mode=mode, url=url, data=data)         #request请求
        print(req.text)

        return req.text

    @data(*excel_r)
    def test_Home(self,excel_r):
        self.logger.info("开始测试{0}".format(excel_r.data))
        print(excel_r.data)
        print(excel_r.act)

        formula="#(.*?)#"
        formula_sql = "&(.*?)&"

        # print(sql_m)

        while re.search(formula,excel_r.data):

              excel_r.data=self.formula_class.formula_intermediate(formula,excel_r.data)

        print(excel_r.data)

        #充值
        if self.sheet=="recharge" and excel_r.url=="/member/recharge":

           self.recharge(formula_sql=formula_sql,mode=excel_r.mode,url=excel_r.url,data=excel_r.data,act=excel_r.act)
        elif self.sheet=="recharge" and excel_r.url=="/member/login":
             self.req(mode=excel_r.mode, url=excel_r.url, data=excel_r.data)

        elif excel_r.url=="/member/bidLoan":
             self.bidLoan(formula_sql=formula_sql,mode=excel_r.mode,url=excel_r.url,data=excel_r.data,act=excel_r.act)

        else:
            try:
                re.search(formula_sql,excel_r.act)
                self.req(mode=excel_r.mode, url=excel_r.url, data=excel_r.data)

                self.assertIn(self.sql(formula_sql,excel_r.act),excel_r.data)
            except:
                 #没有任何特殊符号 没有任何sql的普通请求 登陆这样子的
                 self.logger.error("报错了，{0}".format(excel_r,data))
                 self.assertIn(str(excel_r.exp),self.req(mode=excel_r.mode,url=excel_r.url,data=excel_r.data))


    @classmethod
    def tearDownClass(cls):
        cls.excel.excel_close()
        cls.gp.req_close()
        cls.formula_class.formula_clear()
        cls.mysql.mysql_clear()
        cls.logger.info("测试结束了")

#判断加标成功后查询数据库取出loan_id
#  sql is Not None 取出的sql不为空的时候执行这里不然不执行 可以把断言加进来
#如果需要多条sql语句就可以这么写{"sql1":"select....","sql2":"select...."}