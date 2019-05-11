# # # '''
# # # 如何去连接数据库
# # # pip install pymysql
# # # 仅限于mysql 如果是其他数据库就需要其他的数据库模块
# # # 需要安装第三方模块
# # # mysql的默认端口是3306
# # # '''
import pymysql

host="test.lemonban.com"           #这个是主机地址 可以写域名也可以写ip+端口号
user="test"                        #用户名
password="test"
port=3306
my_connect=pymysql.connect(host=host,user=user,password=password,port=port)#连接
cursor=my_connect.cursor()        #新建立一个查询界面类似于打开一个查询窗框输入sql一样

# cursor=my_connect.cursor(pymysql.cursors.DictCursor) #创建一个类似字典的游标
#如果是secety * from biao 需要查询多个列的时候 变成字典类型结果就会变成
#{“mobiphon”:"376714574","pwd":"123456","lond_id":"2023} 把数据库的字段名变成key把里面的值变成了V

sql="SELECT LeaveAmount from future.member where MobilePhone=15810447878"
# sql="select * from future.member"

cursor.execute(sql)                #运行sql
# my_connect.commit()
result=cursor.fetchone()        #查询结果  上面的sql查询只会查询出一条语句 就可以用这个 一条放在元祖里面
# result=cursor.fetchall()               #返回全部的数据
result=result[0]
print(result)
# print(type(result))
#
# # print(result.value)
#
# cursor.close()               #关闭查询的表 类似于sql里面有一个你需要写sql的地方关闭的时候它会提示你是否需要保存
#                               #所以他先关闭查询的表
#
# my_connect.close()           #关闭上面的后 再关闭整个mysql
# # # #
# # # #
# # # #
# # # # #case.data.find("mobilprj")>-1     判断那个地方是否需要变成随机数
# # # # # case.data=case.data.replace("mobilprj",str(数据库取出来的值))
# # # #
# # # # #case.data.has_key("user") 判断字典是是否有这个key
# # # #
# # # # #case.data.haskey("user") and case.data["mobliepion"]=="normal_user"
# # # #
# # # # #  if "mobfeng" in case.data.keys and case.data["mobliepion"]=="normal_user"
# # # #
# # # # #  if case.data.__contains__("mobilephone") and case.data["mobliepion"]=="normal_user"
# # #
# # # import re
# # # from configparser import ConfigParser
# # # #             #.什么都能匹配但是只能匹配一次   *匹配多次     ？最多匹配一次
# # # #    #.*?  什么都匹配但只能一次  匹配多次  匹配到一次就停止
# # # # d=re.findall(p,data)  #无论你的正则是什么 他会匹配到全部能匹配到的并且返回
# # # # print(d)              #"@(.*?)@"  ()就是代表一个正则表达式组的开始和结束 用@来做索引
# # # #                       #  如果没有括号匹配的结果是@'123456'@ 用过好阔进里面的就会得到'123456'
# # # #         #取出组内的数值 拿到参数中的key
# # # # # config.get("url",asd)  #从里面的里面取出来  查找配置文件里面的值
# # #
# # #
# # # data='{"mobilephone":"@random@","pwd":"@123456@"}'
# # # p="@(.*?)@"
# # # c=re.search(p,data)
# # # print(c)
# # # asd=c.group(1)
# # # print(asd)
# # #
# # # config = ConfigParser()
# # # config.read(r"C:\Users\Administrator\PycharmProjects\python_15\WEEK\OL.conf", enco·ding="utf-8")
# # # dsa=config.get("data",asd)  #使用withe循环在data下面写不同的[a] [b] [c]然后通过group出来的值 进行判断
# # # data_new=re.sub(p,dsa,data,count=1) #count查找替换的次数
# # # print(data_new)
# # # # data_name=re.sub(p,dsa,data)
# # # # print(data_name)
# #
# # #withe循环 最后修改了data的值 然后再次循环的时候就是data的值被修改了 然后重新循环这样group(1)
# # #每次取到的值 都是正确的了 最后都修改正则无法抓到值 然后就返回None最后withe循环就停止了
# #
# #set类型需要查询 学习
# #
# import requests
# # class asd:
# #
# #     a=1
# #
# #     def __init__(self,dsaa):
# #         self.dsaa=dsaa
# #
# # # setattr(asd,"age",2)      #给类增加一个类属性
# # # print(type(asd))
# # # print(hasattr(asd,"age")) #判断类是否有这个属性有返回T没有返回F
# # p=asd(123)
# # setattr(p,"dance",True)   #给实例化对象设置属性 刚才那个是给类设置的 如果之前有这个值就会覆盖之前的
# # # print(p.dance)             #这样就有了
# # #virtualenv    virtualenvwrapper-win  pipenv     pip的方式可以安装
# #
# # delattr(asd,"a")       #删除实例或者类属性
# # getattr(asd,"a")       #获取类属性  如果没获取到就报错
# # # getattr(p,"dance")     #获取实例属性 如果没获取到就报错
# # #
# a={"1":"sda"}
#
# print(a.values())