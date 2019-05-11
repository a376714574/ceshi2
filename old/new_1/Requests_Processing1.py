import re
import unittest

from ddt import ddt, data
from new_1 import os_path
from new_1.excel_rz import excel
from new_1.requests_GP import get_post

from old.new_1.config_rw import formula_re


@ddt
class Requests_Cls(unittest.TestCase):

    ex_rz=excel(excel_name=os_path.live_path, sheet="invest")
    ex_r=ex_rz.excel_read()
    gp = get_post()
    formula_re=formula_re()

    @classmethod
    def setUpClass(cls):                    #类方法不需要有实例对象直接类名。就可以引用了 cls代表的
        cls.gp.sess_open()                   #Requests_Cls这个类
        cls.formula_re.re_start("\OL.conf")

    @data(*ex_r)                          #五个测试用例ddt会生成五个test方法 而每次他都会从
    def test_requests(self,ex_r):           #ddt开始运行所以up和down就变得非常关键self就代表实例本身
        formula="#(.*?)#"
        print(ex_r.data)
        while re.search(formula,ex_r.data):
              ex_r.data=self.formula_re.replace(formula,ex_r.data)
        print(ex_r.data)
        req=self.gp.req_gp(ex_r.mode,ex_r.url,ex_r.data)
        try:
            self.assertIn(str(ex_r.Exq),req)
            self.ex_rz.excel_write(ex_r.id,req,"True")
        except Exception as e:
            self.ex_rz.excel_write(ex_r.id,req,"False")

    @classmethod
    def tearDownClass(cls):
        cls.gp.sess_close()
        cls.formula_re.re_clear()