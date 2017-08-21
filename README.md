# Myblog 设计前准备
虚拟环境下使用Virtualenv    pip install virtualenv  
进入指定目录虚拟环境 virtualenv 文件夹路径<br>
激活 文件夹Scriptsactivate<br>
安装Django
创建Django项目  django-admin start-project projectname<br>
修改语言和时间
把英文改为中文
LANGUAGE_CODE = 'zh-hans'
把国际时区改为中国时区
TIME_ZONE = 'AsiaShanghai'<br>
运行 python manage.py runserver<br>
进入到manage.py文件所在位置创建应用<br>
python manage.py startapp appname<br>
使用postgresql
pip install psycopg2<br>
修改settings.py文件中database中的<br>
```Python
DATABASES = {
    'default' {
        'ENGINE''django.db.backends.postgresql_psycopg2',
        'PASSWORD' '...',
       'HOST' '127.0.0.1',
    }
```
```python
python manage.py shell<br>
 from  django.db import connection<br>
 cursor = connection.cursor //Python
```

# 数据库设计
 文章有文章的ID、标题、正文、分类和标签等一系列属性
首先model中定义了三张表，分别是文章（Post）、分类（Category）以及标签（Tag）<br>
作者是从 
```python
django.contrib.auth.models
``` 
导入的<br>
### 理解ForeignKey 和 ManyToManyField。 ###
ForeignKey 表明一种一对多的关联关系,比如这里我们的文章和分类的关系，一篇文章只能对应一个分类，而一个分类下可以有多篇文章<br>
ManyToManyField 表明一种多对多的关联关系，比如这里的文章和标签，一篇文章可以有多个标签，而一个标签下也可以有多篇文章
### 迁移数据库 ###
```python
python manage.py makemigrations 和 python manage.py migrate 命令
```
### 查看log ###
```python
python manage.py sqlmigrate blog 0001
```
# Django处理http请求 #
### 绑定URL ###
app目录新建urls.py文件并写入
```python
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
r'^$' 的模式正是匹配一个空字符串（这个正则表达式的意思是以空字符串开头且以空字符串结尾），于是二者匹配，Django 便会调用其对应的 views.index 函数。
### 编写视图函数 ###
```python
myblog/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("欢迎访问我的博客首页！")
```
### 配置项目URL ###
```python
blogproject/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'', include('myblog.urls')),
]
```
### 使用模板 ###
project下新建templates文件夹，templates文件夹下新建myblog文件夹，myblog下新建index.html,写入模板代码<br>
在setting.py下找到TEMPLATES<br>
```python
'DIRS': [],
```
变更为
```python
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```
# 修改首页视图函数 #
修改myblog/views.py视图为
```python
from django.shortcuts import render
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
```
新建文件夹myblog/static/myblog/css和js，下载博客模板,替换其中的templates/index.html<br>
```
<link rel="stylesheet" href="css/bootstrap.min.css">替换为
<link rel="stylesheet" href="{% static 'blog/css/bootstrap.min.css' %}">
```
# 后台Admin相关 #
```python
python manage.py createsuperuser
```
### 后台注册admin ###
```python
from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# 把新增的 PostAdmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
```
# 随手笔记 #