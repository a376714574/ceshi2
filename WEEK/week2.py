'''
装饰器
装饰器在不修改功能代码的前提下 可以扩展新功能比如data
在不修改原来代码和调用方式 增加新的需求

实现装饰器
可以做函数 必报函数
也可以通过类 类装饰器

闭包函数
    函数内部嵌套函数
    内层函数的返回值是内层函数的函数名
    内层的函数对外层的函数有一个非全局变量的引用

面试题 装饰器问题
请举例两种装饰器的实现方法    闭包函数  类中定义__call__方法
装饰器可以装饰类和函数吗      可以
类可以当装饰器吗             可以
如何实现通用装饰器            传参使用不定长参数
可以同时被多个装饰器装饰吗     可以
装饰器有什么用                不更改代码的基础上 新增加功能
扩展如何用类来实现装饰器

装饰器应用场景 可以在外城的函数计算函数时间 运行次数
路由传参 插入日志 实现缓存处理 权限校验 在函数外层套上的代码校验的代码比如是否登陆之类的
# '''
#
# def add(a): #外层函数的第一个参数类型为函数 如果是类的装饰器第一个参数就是类
#     def asd():
#         print("装饰器扩展")  #在装饰器内部进行调用外部参数 因为他是函数需要这么调用
#         a()                #就算有全局变量 这个a也是引用add()函数里面的a
#     return asd
# #满足上面的条件后 装饰器 就完成了
#
#
# @add               #@add的意思就是 add(aaaa) 因为add的第一个参数是函数所以需要传进去
# def aaaa():          #@add相当于调用它 但是调用它 需要一个参数 会把aaaa传禁区
#     print("aaaa")
#
# aaaa()                    # 运行结果是 装饰器扩散 然后是 aaaaa
# #装饰器原理 @装饰器的时候 会自动调用装饰器函数 然后把被装饰的函数当作参数传进去
# #装饰器的返回值 被原来被装饰的函数名接收
#
# # 被调用的函数 因为被装饰的函数指向的是asd 那么此时就是直接调用asd 而asd里面的又掉用a() a()实际上就是被装饰的函数
#
# def func(fu):
#     def func_01(a,b):
#         print("11")    #二. 会进入这里此时上面的a和b被传入了11和22
#         fu(a,b)        #三。接下来a和b会传参进入这里
#     return func_01
#
# @func
# def asd(a,b):
#     print(a,b)         #因为fu实际上就是asd所以这个时候fu a和b的值 会传入 asd里面这样就完成了一次完整的装饰器传输
#
# asd(11,22)        #一.这里虽然是调用asd但是asd被func装饰所以回家纳入func里面


def func(fu):
    def func_01(*a):
        print("11")    #二. 会进入这里此时上面的a和b被传入了11和22
        fu(*a)        #三。接下来a和b会传参进入这里
    return func_01

@func
def asd(*a):       #在这里也可以先定数量比如 def asd(a,b,c) 就可以固定参数数量
    print(a)
asd(11,22,33,44,55)        #一.这里虽然是调用asd但是asd被func装饰所以回家纳入func里面
#可以传多个参数