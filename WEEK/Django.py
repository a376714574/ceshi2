'''
Django框架

Django是一个开放元代的Web应用框架 由Python写成  劳伦斯出版集团一些新闻网站CMS软件 2005年7月BSD许可证
docs.djangoproject.com/en/2.2 官网

pip install django 需要安装第三方模块

MVT 模型(负责与数据库交互) 视图(前端信息接收处理然后返回)  T(渲染模板 返回HTML页面)

豆瓣网站是python开发的

Django会自动帮你创建初期的文件夹和文件的框架
需要进入到你想要创建的目录下
C:\Users\Administrator\PycharmProjects\python_15\Django>
然后执行命令
django-admin startproject news就会自动创建了

settings.py 这里面放的是配置文件
urls.py     匹配路径
wsgi.py     上线中使用 部署线上的环境

看到29分了
'''
import django