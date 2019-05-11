'''
50-100元之间 会给出百分之10的折扣
大于100会给出百分之20的折扣
询问购买价格 显示出折扣数量和最终价格
input("请输入价格")输入的无论是什么返回的都是字符串
------------------------------------------------------------------
服装折扣题
a=float(input('请输入衣服的价格'))
if a>=50 and a<=100:
     print("最后的价格为",round(a*0.9,2),"您的折扣为10%")
elif a>100:
     print("最后的价格为",round(a*0.8,2),"您的折扣为20%")
else:
    print("您选择的价格不再折扣范围内")

15/5无论结果是什么 类型都是浮点数
18//4无论结果是什么 类型都是整数
------------------------------------------------------------------

a=int(input('请输入衣服的价格')) 对于这个位置有疑问这一以来之只能输入整数 如果换成浮点
if a%3==0 and a%5==0:            结果又全是浮点数
    print("可以被整除")
else:
    print("不可以")
------------------------------------------------------------------
a=int(input('输入一个数字'))
if (a%4==0 and a%100!=0) or a%400==0:
    print("闰年")
else:
    print("不是闰年")
------------------------------------------------------------------
a=input('输入一个数字')
if len(a)%2==1:
   b=int(a)           回文数暂且放置 至少是一个5位数字
   c=str(a)
   for d in c:
    print(c)
# print(len('asd'))
------------------------------------------------------------------
import  random

print(random.random())0-1生成随机小数
print(random.randint(1,9)) 生成随机整数

a=random.randint(1,9)
print("随机出来的数字为",a)
b=int(input("请输入一个数字"))
if a>b:
    print("您输入的数字小了")
elif a<b:
    print("您输入的数字大了")
elif a==b:
    print("您输入的数字正好")
--------------------------------------------------------
登陆功能
user="saber123"
password="asd123"


c=0
while c<=3:
    a = input("请输入用户名")
    b = input("请输入密码")
    c+=1
    if a==user and b==password:
        print("您的密码输入正确 欢迎登陆 加速路由器系统")
    else:
         print("密码输入错误 请再次输入")
print("您输入错误的次数过多请稍后重试")
-----------------------------------------------------------
d=0
for a in range(1,10):
     d=d+a
print(d)
----------------------------------------------------------

c=[]
a=0
for b in range(2):
    age=int(input("请输入你的年龄"))
    sex=input("请输入你的性别")
    if (age>=10 and age<=12) and sex=="f":
       c.insert(b,age)             性别总人数
    else:
       print("对不起您的条件不符合要求")
print(len(c))
-------------------------------------------------------
for a in (1,2,3,4,5):
    print("*"*a)               直角三角形 第一行打一个 第二行两个

for a in range(10):
    b = 0
    print("\n")
    while b<a:           直角三角形
        b+=1
        print("*",end=" ")

for a in range(1,6):
    for b in range(1,6-a):  第二种解法 网上抄的
         print(" ",end=" ")
    print("* "*a)
--------------------------------
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):    等边三角形网上抄的
        print("* ",end="")
    print("")

for a in (1,2,3,4,5):
    print(" "*(5-a),end="") 第二种
    print(" *"*a)
-------------------------------------------------
a=10
for b in range(0,10):
    c=0
    a-=1
    while c<a:             输出99乘法表
        c+=1
        print(c,"*",a,end=',')
    print(end="\n")
-------------------------------------------------

a=[1,232,211,13,53,21,23,4]

for c in range(len(a)-1):
    for b in range(len(a)-1): 冒泡算法 成功 但是这里会有多余执行的问题这里的数字是固定的所以就算最后换一次就解决问题的时候这里也会运行六遍
  # for b in range(len(a)-1-c):需要一个变动值第一次是7之后6 5 4之前的那个一直是6所以会循环多次
        if a[b] > a[b+1]:          c第一次是0 之后的顺序是 1 2 3 4正好符合要求
           a[b],a[b + 1]=a[b+1],a[b]

print(a)
--------------------------------------------
1 2 3 4能组成多少个相互不重复的三位数字分别是什么
--------------------------------------------
人机大战：
三个角色 曹操 张飞 刘备
猜拳电脑随机出一个 你也出一个 最后赢了几局 输了几局 平了几局


----------------------------------------------------------------------
qian="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
hou="zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA9876543210"
上面是定义转换编码

a="dadAsdDa"        这个是要转换的字符串

c=a.maketrans(qian,hou)     用a这个变量调用编码器 然后输入对照编码
b=a.translate(c)            用a调用转换器并且把 规则“c”当作参数放进去
print(b.swapcase())         大小写呼唤并且输出
-------------------------------------------------------------------------
import re

str1 = 'sda236.6asd年1,/月9日/asd1'

pattern = re.compile(r'\d+')
pattern2 = re.compile(r"[\u4e00-\u9fa5]+")
pattern3 = re.compile(r"[a-zA-Z]+")
res = re.findall(pattern, str1)
res2 = re.findall(pattern2, str1)
res3 = re.findall(pattern3, str1)
for i in res:                                标点符号的正则不会写
     print(i,end=",")
print()
for qw in res2:
     print(qw,end=",")
print()
for qw in res3:
     print(qw, end=",")
-------------------------------------------------------------------
url:http://47.107.168.87:8080/futureloan/mvc/api/member/register@mobile:18688773467@pwd:123456
url:http://47.107.168.87:8080/futureloan/mvc/api/member/recharge@mobile:18688773467@amount:1000
请利用上课所学知识，把txt里面的两行内容，写一个函数，返回如下格式的数据：
[{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/register','mobile':'18688773467','pwd':'123456'},
{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','mobile':'18688773467','amount':'1000'}]
没做出来
-------------------------------------------------------------------

class Restaurant:

      def __init__(self,restaurant_name,cooking_type):
           self.a=restaurant_name
           self.b=cooking_type

      def describe_restaurant(self):
           print(self.a,self.b)

      def open_restaurant(self):
           print("饭店正在营业中 请推门就进")
      # def open_restaurant(self):

H=Restaurant("dsaa","sdada")
H.describe_restaurant()
H.open_restaurant()
-------------------------------------------------------------------
class user:
    first_name=1
    last_name=2
    sex="女"
    age="18"

    def describe_user(self):
        print(self.first_name,self.last_name,self.sex,self.age)
    def greet_user(self):
        print("你好欢迎光临 未来之城 请选择您喜欢的机器人")
user().describe_user()
user().greet_user()
----------------------------------------------------------------------
a="ud启5是的212sda"

for b in a:  for循环会把字符串里面每一个内容一个一个传给b
    print(b)             顺序是 u d 启 5......
基本上只能判断数字和英文 没有单独判断中文的 没有单独判断标点符号的
基本上都是用排除法 派出所有可能性留下最后一个肯定是的 比较low的算法我的
正则表达式胜他百倍 可惜无奈没有完全掌握

a="naa大家jd，。12爱12神的箭啊"

zh=[]
zm=[]
num=[]
ty=[]

for b in a:
    if b.isdigit():        判断是否是数字
       num.append(b)
    elif b.isalpha():      判断是否是中文或者是字母
        if b.encode().isalpha():       判断是否是英文字母
           zm.append(b)
        else:                不是的话一定是中文
           zh.append(b)
    else:
        ty.append(b)         不是数字 不是中文 不是字母 一定是标点符号

print("数字",num)
print("字母",zm)
print("中文",zh)
print("表单符号",ty)
--------------------------------大小写转换老师讲解版本----------------------------------

a="sdghjJHGSDJjhHJKhjkHhjGDYT"
d=""
for b in a:
    if b.islower():      islower判断是否是小写
       d += b.upper()    lower转换成为小写 因为if后面需要布尔值这样的写法是正确的
    elif b.isupper():
        d += b.lower()
print(d)
最后就完成了for循环的判断

ASCLL美国标准信息交换表

a="adghjJHGSDJjhHJKhjkHhjGDYT"
d=""
for b in a:
    if b.islower():
       b=b.upper()
       b= chr(155-ord(b))
       d+=b
    elif b.isupper():
        b=b.lower()
        b= chr(219-ord(b))
        d += b
print(d)
利用ASCLL编码来制作镜像

------------------人机大战完成-----------------------

import random
a="张飞"
b="关羽"
c="刘备"

win=0
pip=0
low=0
aaa=0
asd=random.randint(1,3)

while aaa<=10:
    dsa = int(input("请输入数值"))
    aaa += 1
    if   dsa == asd:
            pip+=1
    elif dsa > asd:
            win+=1
    elif dsa < asd:
            low+=1
print("win",win)
print("pip",pip)
print("low",low)
------------------------回文数判断条件写出来了 但是输出不知道怎么办---------

a=12321
b=str(a)
c=0

for H in range(len(b)):
        if b[H]==b[len(b)-(H+1)]:
           pass
# print("是回文数")
        if b[H]!=b[len(b)-(H+1)]:
           pass
print("不是回文数")
--------------------------还差一个所有数字一共有多少中不重复-----------------------
'''
