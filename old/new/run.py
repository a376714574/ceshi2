import unittest
import requests
import json

from new_123 import Requests_Processing

a=unittest.TestSuite()
a.addTest(unittest.TestLoader().loadTestsFromModule(Requests_Processing))
unittest.TextTestRunner().run(a)
# #
# #
# #
# # # case.data=case.data.replace("mobilprj",str(数据库取出来的值))
# #
#
# # s=requests.Session()
# # # s.get("http://httpbin.org/cookies/set/sessioncookie/123456789")
# # # r=s.get("http://httpbin.org/cookies")  #这样会包含一个cookie信息
# # #
# # # print(r.text)
# #
# # r=s.get("http://httpbin.org/cookies",cookies={"jehfmafy":"kjsf"})
# # # print(r.text)  #如果参数化cookies的话他的信息就不会一直被一只保存下去了
# # # ass=s.get("http://httpbin.org/cookies")
# # # print(ass.text) #因为上面参数化了cookies所以这里就不会在存在了
# #
# # # requests可以为https请求验证ssl证书 就像web浏览器一样ssl安政默认是开着的如果验证失败 会抛出SSLError
# #
# # a=requests.get('https://github.com',verify=True)#你可以为 verify 传入 CA_BUNDLE 文件的路径，或者包含可信任 CA 证书文件的文件夹路径：
# # print(a.text)                             #如果 verify 设为文件夹路径，文件夹必须通过 OpenSSL 提供的 c_rehash 工具处理
# #                                            #如果设置成为False也能忽略验证 verify仅应用于主机证书
# #                                             #对于私有证书 也可以传递一个CA_BUNDLE的证书路径给verify
# # s=requests.Session()
# # a=requests.get('https://github.com',cert=('/path/client.cert', '/path/client.key'))
# # s.cert='/path/client.cert'
# #                       #对于客户端证书  可以是单个文件(或者包含密匙和证书)或者一个包含两个文件路径的元祖
# #
# # #CA证书requests默认带了一套他信任的根证书只有requests更新的时候他才会更新 如果一直使用一个版本可能已经太旧了
# # #requests2.4版本后如果系统中安装了certifi包 就会使用这里面的证书这样就可以在不修改代码的情况下更新证书
# #
# #
# # with open('massive-body',"rb") as f:
# #     requests.post('http://some.url/streamed', data=f)
# # #     # requests支持流的传输 强烈建议用流\'的方式大开尤其是过大的数据 如果使用文本模式打开文件可能会有错误
# #
# # def get():
# #     yield "hi"
# #     yield "there"
# # aaa=get()
# #
# # for asd in aaa:
# #     print(asd)
# # #
# # # >>> mylist = [1, 2, 3]
# # # >>> for i in mylist : 这里会遍历所有的值 所以mylist就是一个可迭代的对象
# # # ...    print(i)
# #
# # aaa=(x*x for x in range(5))  #一种特殊的写法 第一次x=0 前面是x*x额就是0 第二次等于1 第三次等于2 人就是1*1 2*2.。。
# # # 他并不会一次性把值放入内存了里面 而是实时的生成 实时的存放 这个叫做生成器
# # for i in aaa:
# #     print(i)
# # for i in aaa:  #只能用一次 这个里就不能在用了如果是列表就随便用了
# #     print(i)
# #
# # def get():
# #     malist=range(3)
# #     for i in malist:
# #         yield i*i
# #
# # aa=get()
# #
# # for asd in aa:
# #     print(asd)
# # print()
#
# # r=requests.get("http://httpbin.org/stream/20",stream=True) #stream=True避免了读取的数据立刻存入内存
# # print(r.text)
# # for line in r.iter_lines():       #流式展示信息 区别在于text会一次性展示全部
# #     if line:                        #而r.iter_lines()会把信息一条一条输出 这样就是流的展现形式
# #         decoded_line=line.decode("utf=8")
# #         print(json.loads(decoded_line))
# #
# #
# # r=requests.get("http://httpbin.org/stream/20",stream=True)
# # print(r.encoding)
# # if r.encoding is None:
# #    r.encoding = "utf-8"       #如果他默认有回退编码 那么就用他的但如果服务器没有提供默认的回退编码
# #
# # for line in r.iter_lines(decode_unicode=True):
# #     if line:                          #iter_lines不保证重进入时候的安全性 多次调用该方法 会导致部分数据丢失
# #         print(json.loads(line))        #如果要在多次调用它就应该生成迭代器对象lines=r.iter_lines()
#
#
#
# # a=c=1           #数值 字符串 的时候a b c会变成一个对象 元祖 列表 字典 set类型即使值一样结果也是两个对象
# # b=1              #is是判断是否是是一个对象 是一个内存地址
# # print(a is b)
# # print(id(a))
# # print(id(b))
#
# # for a in [1,2]:
# #     print(next(a))
# #match(a,b) 字符串索引
# #search()   对字符串的任意位置进行匹配
# #findall()  返回字符串中所有的匹配的字串组成的列表
# #finditer() 返回一个包含了所有的匹配对象的迭代去
#
#
import requests

url="http://test.lemonban.com/futureloan/mvc/api/member/login"

data={"mobilephone":"15814447890","pwd":"123456"}

req=requests.post(url,data)

print(req.text)
