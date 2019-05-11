import unittest

from old.new_1 import Requests_Processing, Requests_Processing1

a=unittest.TestSuite()
a.addTest(unittest.TestLoader().loadTestsFromModule(Requests_Processing))
unittest.TextTestRunner().run(a)

a.addTest(unittest.TestLoader().loadTestsFromModule(Requests_Processing1))
unittest.TextTestRunner().run(a)

#
# #
# # # case.data=case.data.replace("mobilprj",str(数据·库取出来的值))
# #
# # #管理员登陆 管理员创建新的项目 管理员审核通过 投资人登陆 投资人持续的开始测试用例
# #
# # #管理员的账号密码
# import re
#
# inputStr = "hello crifan, nihao crifan";
# replacedStr = re.sub(r"hello (\w+), nihao \1", "crifanli", inputStr);
# print (replacedStr)
