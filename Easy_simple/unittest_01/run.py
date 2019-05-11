'''
这里是执行测试测试用例的地方
---------------------------第一种方法-----------------------------------------
好处是可以指定运行的方法 缺点是不能全部运行
from unittest_01.ck import Test        第一个方法由于要运行详细的地方 所以需要继承到类
import unittest

a=unittest.TestSuite()
a.addTest(Test("test_001"))
unittest.TextTestRunner().run(a)
--------------------------第二种方法------------------------------------------
可以直接运行ck模块下的所有类所有方法所以需要继承模块
from unittest_01 import ck
import unittest

a=unittest.TestSuite()             创建实例
a.addTest(unittest.TestLoader().loadTestsFromModule(ck)) 把ck模块放进去
unittest.TextTestRunner().run(a)                         运行用例
--------------------------------第三种方法--------------------------------------------
可以加载模块中的某一个类
from unittest_01.ck import *
import unittest

a=unittest.TestSuite()
a.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_01))
unittest.TextTestRunner().run(a)
--------------------------------输出精美的测试报告 方法一unittest----------------------------------------------
这种方法可以把内容保存到text里面
from unittest_01.ck import *
import unittest

with open("test.text","w") as file: 用with语句来控制open

    a=unittest.TestSuite()
    a.addTest(unittest.TestLoader().loadTestsFromTestCase(Test))
    unittest.TextTestRunner(stream=file,verbosity=2).run(a)  选择输入的文件名  和 选择精细程度
--------------------------------输出精美的测试报告 方法二HTML----------------------------------------------
这个方法可以输出到html里面去
from unittest_01.ck import *
import unittest
import HTMLTestRunnerNew

with open("test.html","wb") as file:       wb是文件流
    a=unittest.TestSuite()
    a.addTest(unittest.TestLoader().loadTestsFromTestCase(Test))
    HTMLTestRunnerNew.HTMLTestRunner(stream=file).run(a)

stream=sys.stdout,  verbosity=2,   title=None,  description=None,     tester=None):
输出地点 默认是控制台   详细程度        测试报告名称         描述              测试员是谁
--------------------------setup teardown小知识---------------------------
class Requests_Cls(unittest.TestCase):

    @classmethod
    def setUpClass(cls):                          run()里面如果使用的是一个case一个case运行那么 正常情况下
        print("setup")                                a.addTest(Requests_Cls("test_requests01"))
                                                      a.addTest(Requests_Cls("test_requests02"))
    def test_requests01(self):        如果想要先运行一个函数让他作为前置 然后在运行为 再次运行于给函数然后作为后置
        print("1")                                   可以用setUp作为前置 运行完test后 才会运行tearDown作为后置
                                      但是上面要运行两个test如果使用这个方法 up和down会被加载两次  这个时候
    def test_requests02(self):        就要用上class 第一次执行运行up然后运行test01 第二次不运行up但是之前的效果还在
        print("2")                    直接运行test02当所有的都运行结束后 就会运行down进行关闭就是现在的写法

    @classmethod                      PS：所为运行一次case就是返回一次即使run里面写着运行整个类
    def tearDownClass(cls):               然后test里面会被运行多次 看似只有test被运行 但实际上那个类重新贝
        print("tearDown")                   运行了 所以所有的开头和结尾又会被再次加载 所以需要用到class的装饰器
'''