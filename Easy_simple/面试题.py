'''
#给一个列表去除重复的  面试题一定要记得写函数
#就算你会写也一定要写成函数
def asd(a):

    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b

a=[1,2,2,3,45,6,6,7,7]

print(list(set(a))) #去掉重复
利用for去删除也可以
----------------------------------------------------------------

#列表和字符串的互相转换

a=[1,43,5,6]
# b=""
# for i in a:
#     b+=str(i)
# print(b)

print(" ".join(a))


a="asdasd"
b=[]
for c in a:
    b.append(c)
print(b)

a="asdasd"
print(list(a))


a="sfowoeoofwfsf"
print(set(a))

如果面试题问你遇到错误解决过程是什么之类的问题要这么回答
顺序是 看报错 调试每一个小模块 猜测 (GitHub stackoverflow infoq)开源社区 技术社区 这样很好比起说百度要好得多
            断点调试


a=[1]
b=a       b=a的时候 他们指的是同一个对象
c=a[:]    #可以拷贝一个新的对象这种写法 所以他们并不是一个对象
a.append(10)
print(a)   a的结果是[1,10]
print(b)   b的结果我以为是[1]因为上面是赋值操作 之后没有在赋值 看来不是这样的
            b=a那么他就时时刻刻等于a就算a有改变 b也会改变

a=[1]
b=a
print(id(a))
print(id(b))#id是内存地址 如果两个内存地址一样那么证明是同一个对象 改变a b也会被改变但是c不是同一个内存地址
            #所以改变a   c并不一定会被改变

str里面的内容是不可已修改的可以增加 字符串是一种不可变的数据类型
boolean条件判断或者说是逻辑控制
list 有顺序的容器
dict 没有顺序的容器

a={"name":"yuze","tage":"16"}

for c,v in a.items():
    print(c,v)

tuple 经常用于解包 不可变类型

函数
参数
*args **kwargs


def add(a,b=[]):
    b.append(a)
    return b

print(add(1))
print(add(2))
print(add(3,['a']))  #[a]是列表 所以直接传给b了 但是3还是传给了a所以结果就是[a]陷进去 3通过执行append之后才会添加进去


a=1   #0就是空的 1就不是 字符串有内容的话就不是为空  [] {} None 都要判断

if not a: #判断是否为空
    print("1")

函数的作用 提高代码的可读性 封装代码 封装一段可以重复运行的代码

类与对象 是python最核心的
__init__初始化对象
__new__ 创造一个对象
'''