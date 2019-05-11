'''
--------------------------------------------------------------------------------
断言
assertEqual(a,b)       判断 a==b  这个是判断是否相等         asserTrue(X)           判断是否是 True
assertNotEqual(a,b)    判断 a!=b                          asserFalse(X)


assertis(a,b)          判断a==b                           assertisNone(x)       是否是为空
assertisNot(a,b)       这个是判断值是不是一个值
用id(a)判断是否在一个内存里                                  assertin(a,b)          a是否在b里面
                                                         assertNotin(a,b)

assertisinstance(a,b)             判断是否为一个对象
assertNotisinstance(a,b)
-------------------------------------------------------------------------------

test_add_01
test_add_02
运行顺序会根据ACLLS码来决定
除非你自己写 1 2或者根据表里面写a b不然即使在上面的也不会先运行
--------------------------------------------------------
import unittest
from Easy_simple.unittest_01.chengxudaima import Mapu

    def test_001(self):
        a=2                             预期值
        res=Mapu().add(1,1)             返回结果/实际值
        self.assertEqual(a,res)         断言
------------------------------------------------------------
ddt:data driver test 数据驱动测试
需要安装ddt模块

import unittest
from ddt import *
from Easy_simple.unittest_01.chengxudaima import Mapu

@ddt                                   #ddt是类的装饰符 必须先装饰类才能使用
class Test(unittest.TestCase):

    @data([1,2,5],[3,4,8])             #data是方法的装饰符 类似于for循环他会遍历所有值给a然后输出
    @unpack                            #切割 他会把data的数据切割
    def test_001(self,a,b,c):         #上面拆成几分下面就要用几个值接收
        aaa=chengxudaima(a,b)           把返回值调出来
        assertEqual(aaa,c)            断言输入实际值和预期值可以用ddt加上for写进配置文件或者ex里面

#unpack 拆分规则 [1,2],[3,4]       a就是1，3
             # [[1,2],[3,4]]     a就是[1,2]
             # [[1,2,5],[3,4,8]] a就是[1,2,5]
             # [1,2,5],[3,4,8]   这样的话就必须有三个参数才可以
             # [1,2,3，1],[13,2,3]  最后会变成四个参数
             #如果类型是字典 那么他的参数名必须是key的名字

'''
import ddt
import unittest
from ddt import data
from ddt import unpack

@ddt                                   #ddt是类的装饰符 必须先装饰类才能使用
class Test(unittest.TestCase):
    def add(self):
        for a in [1,2,3,4]:
            return a

    @data([1,2])             #data是方法的装饰符 类似于for循环他会遍历所有值给a然后输出
    @unpack                            #切割 他会把data的数据切割
    def test_001(self,a):         #上面拆成几分下面就要用几个值接收
          print(a)                       #把返回值调出来
