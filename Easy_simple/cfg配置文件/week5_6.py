'''
.cfg  .conf  .ini .properties都是配置文件
可以在配置文件里面写上字典或者列表 这样在外面写上for就可以一次性使用了 在使用eval还原他

需要安装第三方模块 pip install ConfigParser

from configparser import ConfigParser       #导入模块

a=ConfigParser()                            #创建实例化对象
a.read("week5_6_1.cfg",encoding="utf-8")    #读取详细信息 加上编码
b=a.sections()                              #返回配置文件里面所有的表名
a.get("db","a")                             #取出配置文件中表名叫"db"中的变量a的值
a.get(b[0],"a")                             #取出配置文件中b[0]位置中的变量a的值


a.options(b[0])                      #取出配置文件中b[0]位置的所有变量名
a.options("db")                      #取出配置文件中表名叫"db"的所有变量名
a.getint(b[3],"a")                   #只能取出数字 如果是其他的就会报错
a.getfloat(b[0],"b")                 #只能取出浮点型 如果是int会强制转换成为浮点 如果是其他类型会报错
a.getboolean(b[0],"c")               #只能取出 T F 0 1 空和非空不可以
print(eval(a.get("db","a")))                #默认全部会变成str eval会把他原本的格式取出来
                                            #这个比较好的地方就是即使是str也可以取出来
'''

from configparser import ConfigParser

a=ConfigParser()                            #创建实例化对象
a.read(r"C:\Users\Administrator\PycharmProjects\python_15\Easy_simple\cfg配置文件\week5_6_1.cfg",encoding="utf-8")    #读取详细信息 加上编码
print(a.get("boo","a"))