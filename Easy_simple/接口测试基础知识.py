'''
接口测试基础概念

web页面
由html css js组成 他们都存在服务器里面 每次页面加载都会请求服务器 然后服务器在把信息发送回来 所以网络差就会加载的慢

通过抓包抓到登陆的网址和字段名 如果加密还需要知道是什么加密
jmeret(java写的),Fiddler,soapui,loadrunner
在线的一些插件都可以做接口测试 firefox httprequester 都可以做接口测试
用工具去做接口测试的时候实际上是模拟客户端发起一次请求

测试金字塔：越往下投入越多 单元测试的稳定性和保证了产品质量
UI层    手动测试       上
服务层   接口测试       中
单元     白盒测试       下
越往下越难薪资越高

接口测试:
登陆 充值 记时 金币所有有请求服务器和服务器响应的行为 都需要进行接口测试
测试正确和异常的情况 比如登陆的正确 密码错误 充值的成功 失败 账户余额不足 游戏金币的 金币不足 是否充值
测试就是测试输入不同的情况 然后查看服务器的返回值 登陆还有长度过短 不能有中文之类的具体设计看接口设计文档
缺少用户名 缺少密码等等 还有注册 我们需要 接口测试 自动化测试 数据库测试 数据库性能(慢查询 缓存)
不只是验证请求和响应 除了断言结果外 还需要去数据库判断正确 会达到初级dba(初级数据库管理员)
如果后端返回值是正确的 但是前端页面显示错误 比如后端返回缺少密码 前端却显示缺少用户名或者登陆失败就是要反应的问题
服务器异常可能是你传参都是争取的 但是在数据存储或者其他原因的过程中 导致了程序内部的错误 这个时候就是程序的bug了

HTTP协议

请求类型 get post(登陆更多的使用post) update head option   put请求修改 delder请求删除
http不加密传输 https加密传输
API 应用程序可编程接口
www.baidu.com---->叫做域名   百度原本是一个IP加上端口但是比较难记所以发明了域名

域名     =     ip  +  端口号
www.baidu.com=192.168.0.1:8080
测试充值的时候 有一种方法发送请求 但是不要登陆 会返回抱歉请先登录

TCP/IP
DNS解析 就是把域名解析成IP然后根据IP再去请求
HTTP协议

响应头header
Referrer政策 他会限制一些操作
Accept Encoding 会有一些编码和压缩信息
Accept Language 支持的语言
Connection 连接状态
Cookie HTTP无状态 不会记录信息 Cookie会弹出的 比如淘宝看了手机 转天在登陆就会发现满屏手机信息这种感觉
            我第一次请求一个网址 会给我们派发一个类似会员卡的东西  浏览器会自动保存cookie信息 前提是浏览器允许保存
              Cookie会保存一个目标网站 Cookie值 cookie类型 但是cookie是由时间限制的 默认是关了浏览器再打开就没了
                但是也有可能不是这样 第二次请求的时候 浏览器会自动带给你cookie值浏览器会自动带上
Host：域名地址    一个域名地址（一个接口地址是域名地址拼起来的）
User Agent 用户代理 我用 win64位 火狐浏览器 如果是安卓这里就是安卓什么什么 苹果什么什么 类似于你的一个标识
              如果服务器不允许火狐浏览器 可以利用fiddler修改这个信息变成谷歌的 在爬虫里面用的很多

HTTP请求的 三次握手和四次挥手
GET和POST有什么区别
安全性
https://api.gtshja.com?contest=你最近好吗

get请求会把内容放到了请求头里面去了网址上面就有 可以包含请求参
本来应该放到请求体里面的 但是放到请求头里面了 好处是方便 缺点是隐私安全
https://home.firefoxchina.cm/?from=extra_start
https://home.firefoxchina.cm/?from=extra_start&pwd=123   如果有多个参数会用&分开&pwd=123

POST 他会把信息放到体里面作为参数发过去比较安全
res=requests.post(url,date,verfy=False)  web请求方式有get post还有许多其他种类的
                                           verfy=False不验证 发起一个http请求绕过安全校验不然还要装证书


请求体 就是信息内容
请求头user-agent content type
请求体params
响应状态码  HTTP协议规定的响应码 比如200 404
响应内容  {"stjiaa":"200"}响应内容是服务器人员从后台发过来的 认为规定的

用户通过UI输入用户名和密码 www,baidu.com   但是浏览器并不是用这个网址去访问服务器的
                                         他会请求服务器的接口地址 api.baidu.com/login
                                            通过接口地址就到了后端

UI--->接口地址--->后端 这样的一个顺序
-----------------------------------------------------------------------------------------
数据库部分:
MySQL 关系型数据库管理系统
使用标准化sql语言进行操作
体积小 速度快 成本低
开源 免费 中小型网站首选
可以维护多个数据库
数据库里面可以设置必填和非必填的字段 如果数据库有改动接口测试的时候需要验证数据库
比如注册 充值等
每个表里面都会有一个主键 类似id一样的东西他是自增长的每增加一条会自动增加

数据类型:
int整数范围   -2147483648~2147483648

字符串型      char(n) n个字符 最多255 自定义长度
             varchar(n) 可变长度 最多65535

时间和日期     date 日期  例：2016-08-22
             time 时间  例: 18：40：37
             datetime 日期时间  例：2016-08-22 18：40：37
             timestamp

浮点型        float(m,d) 单精度浮点 32bit  m代表总长度 d代表小数位长度  比如99.99 那么这写float(4,2)
             double(m,d)  双精度浮点 64bit  m代表总数 d代表小数位
             区别 双精度类型能表示小数点精准度更高


sql语句:
sql语句不区分大小写

创建一个表 然后填写字段名和字段类型
CREATE TABLE saber(
  id int(11),
  user_name varchar(20),
  phone char(11),
  pwd VARCHAR(40)
  );

create database lemon;                      创建一个名叫lemon的库
show databases;                             查看所有的数据库


查询
select * from nember limit 3                 limit 3   只显示前3条记录
select * from nember;                       查询nember表里面的所有内容
select id,phone from nember where id=2; 只显示id等于2 nember表里面的id phone字段
SELECT * from `user`,nember;
user      有五条数据
nember    有五条数据
结果查处了25个 是因为这两张表做了乘法5*5=25 所以有很多数据是错误的

SELECT * from `user` as u,nember as n where u.id=n.id
把user取个别名叫做u    nember 叫做n
当u的id和n的id相等的时候显示这一条数据

SELECT * from `user` as u join nember as n on u.id=n.id;       和上面的一样
SELECT * from `user` as u inner join nember as n on u.id=n.id; 内链接  结果和上面一样
SELECT * from `user` as u cross join nember as n on u.id=n.id; 结果一样

左连接 left join
SELECT * from `user` as u left join nember as n on u.id=n.id;
以左边为主 如果左边和右边id=1那么全部显示 如果做左边有id=2 右边并没有id=2 那么右边会变成空
                                                     saber 1 12 null null null 这样的感觉

SELECT * from `user` as u left join nember as n on u.id=n.id where phone is not null;
                                                                和上面一抹一样这里判断为空不显示
右连接 右连接和左连接一模一样就是反过来


增加:
insert into saber values(1,'21',21)         添加一行数据
insert into 表 values(写对应的值)
insert into saber(id,user_name,phone) values(3,'21','21')  如果并不像添加全部的字段值那么输入像添加的id
insert into saber(id,user_name,phone) values(3,'21','21'), 一次性输入多行
                                            ('21','21','21'),
                                            (4,'21','21'),
                                            (5,'21','21'),
                                            (6,'21','21')

删除:
delete from saber;             删除整个表
delete from saber where id=1;  删除id字段等于1的
truncate table saber;          清空表记录
drop table saber               删除表


修改
update nember set id=1,user_name='2'; 把所有的id变成1 所有的user_name变成2
update nember set pwd=MD5('2');       一次性把所有的密码都修改成MD5加密但是全部都变成2的加密
update nember set pwd='321',phone='ewqq' where id=2; 会把id等于2的字段pwd和phone全部修改
update nember set pwd=MD5('123456');        把这个字段通过MD5加密

'''

class Boss:

    money=0
    product="肥皂"
    people={}

    def people_r(self,peop):
        pop = input("请输入要增加人员的姓名")
        print("您拥有的人员为",pop)

    def product_r(self):
        TF=input("是要卖出商品 Y/N")
        if TF == "Y":
            self.money+=10
            print("您所拥有的金钱数量为",self.money)
        else:
            print("您所拥有的金钱数量为",self.money)

Boss().people_r("张三")

Boss().product_r()

class Employee:
      EX=300
      Boss_money=10000

      def pop_mo(self):
          a=0
          while a<13 and self.EX<=500:
                a+1
                self.EX+=50
                ALL_mo=self.Ex*10
          Bos s()