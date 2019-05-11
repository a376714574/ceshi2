'''
:param auth: (optional)    他是做认证有一些接口需要认证 有一些这个信息放到这个里面

:param timeout: (optional) 等待多久服务端返回时间 500秒内服务器必须返回 超过就抛出timeout
:type timeout:             是你请求超时 还是 返回超时type和timeout组合使用

:param allow_redirects: (optional) 是否允许重定向 GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
:type allow_redirects: bool

:param proxies: (optional) 代理 手机抓包需要代理 字典形式

:param stream: (optional) 抓一个html网页把他从网页端保存到文件里面 已流的形式返回回来

:param verify: (optional)  http和https https(certificate多了一个认证过程) 但是没有这个证书还是需要请求
                                     https  就用这个我是http请求改成F就默认不需要请求了(不想传证书)
:param cert: (optional)   (如何需要传证书的话verify设置成为T 然后这里传参数) ssl客户端证书文件(.pem)的路径
                                             如果是元祖("cert","key")证书找开发要或者浏览器下载保存到本地
:return: :class:`Response <Response>` object
:rtype: requests.Response

requests.put()   requests.delete()  requests.head()    requests.options()
请求方式扩展

请求头部信息的制作和使用
headers={"content-type":"application/json","User-Agent":"Mozilla/5.0"}#制作header信息
login_cookies = requests.post(url,data,headers=headers)
使用头部信息后 用户认证信息就不会生效了 如果设置了auth=参数,"。netrc"的设置就无效了
如果被重新定向带别的主机 授权的header就会被删除 代理授权header会被URL中提供的代理身份覆盖掉
进一步来说requests不会因为制定了header就改变自己的行为 只不过在最后的请求中把所有的header的信息传递进去而已

使用requests方法后，会返回一个response对象，其存储了服务器响应的内容
login_cookies.raw      返回原始相应体
login_cookies.content  会已字节的方式响应体 目前看来只有中文部分被字节化了
login_cookies.headers  返回响应头 若不存在则返回None

login_cookies.encoding="IOS-8859-1"   requests默认的编码格式是utf-8 可以修改的
login_cookies.encoding                会返回requests的编码格式

req.url  通过打印输出url 这个时候的url已经被正确编码
字典里面值为 None的都不会添加到url里面
a={"123":"V","321321":["32131","321321"]} 字典的另一种表达方式 一个key可以有多个V

Requests 中也有一个内置的 JSON 解码器，
r.json()   如果 JSON 解码失败 就会抛出一个异常
成功调用 r.json() 并**不**意味着响应的成功。有的服务器会在失败的响应中包含一个 JSON
对象（比如 HTTP 500 的错误细节）。这种 JSON 会被解码返回

a=(("1","2"),("1","4")) 也可以向data传输一个元祖列表
在表单中多个元素使用同一个key尤其管用

requests.post(url,json.dumps(payload)) 这里可以进行对dict进行编码
requests.post(url,json=payload)还可以用json直接传参  然后它会被自动编码 这是2.4.2版的新家功能

a=requests.post(url,stream=True)        stream可以让文件已流的形式传输进来 这样不是一大块的内存占用而是一点一点的
a = requests.post(url,json=payload)     变成json格式

files={'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
可以显示设置文件名 文件类型 和请求头
files={"file":open("get.text","rb")} 发送一个文件普通发送
a=requests.post(url,files=files)
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')} 可以发送作为文件来接受的字符串
建议使用二进制接收文件 因为requests有可能会发送发送字节

a.raise_for_status())如果返回值是200那么结果就是None 但如果4XX客户端错误或者5XX服务器响应错误 可以通过它来
抛出异常

a.headers可以查看响应头
a.headers["Access-Control-Allow-Origin"]) 请求响应头的时候可以协商key来取固定v的值
dict(a="123") 强制转换字典方式

r=requests.post(url,allow_redirects=False)   貌似这样就可以重新定向了比如把http重新定向成为https
r.url                              allow_redirects=False禁止重新定向
r.status_code
r.history

超时
你可以告诉requests在经过timeout参数设定的秒数后停止等待响应 基本上都用这一参数 不然你的程序可能会永远失去响应
requests.post(url,timeout=0.1) 单位是秒
准确的说是从发起时间开始计算 0.1秒内若是没有接收到服务器返回的信息就抛出异常

https://github.com/                                        post请求
https://github.com/?mobilephone=15810447878&pwd=123456     get请求(字典里面的值如果为None那个键值对就不会进入url地址里)
r.url使用这个方法可以看的出来post请求比较安全了也能看得出来get和post的区别
r.url可以看得出来url已经被requests正确编码了

r.content以字节的方式去访问请求 响应体 这是对于非文本文件的请求
requests会自动解码gzip和deflate传输编码和相应数据

r.json帮助你处理json数据 json解码器 如果解码失败会抛出异常
调用json成功并不意味着相应成功 有些服务器会在失败的相应中返回一个包含json对象的信息
如果要检查请求成功请使用 r.raise_for_status()或r.status_code

如果想要保存服务器的原始套接字响应
可以使用r.raw 但是要在请求时设置requests.get('https://api.github.com/events', stream=True)
服务器原始嵌0套响应
<urllib3.response.HTTPResponse object at 0x0000000003EE7208>不知道是做什么的和fiddler的raw不一样
requests.post(url, data=json.dumps(data)) json.dumps(data) 会对字典进行编码还可以使用json直接传递

                  可以修改文件名                         请求头                  类型
file={"file":("123.text",open("get.text","rb"),'application/vnd.ms-excel', {'Expires': '0'})}
r=requests.get(url,files=file)        传输文件

'''
