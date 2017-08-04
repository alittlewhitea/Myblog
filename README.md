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
DATABASES = {
    'default' {
        'ENGINE''django.db.backends.postgresql_psycopg2',
        'PASSWORD' '...',
       'HOST' '127.0.0.1',
    }
<br>
测试
<br>
python manage.py shell<br>
 from  django.db import connection<br>
 cursor = connection.cursor

# 数据库设计
 文章有文章的ID、标题、正文、分类和标签等一系列属性
首先model中定义了三张表，分别是文章（Post）、分类（Category）以及标签（Tag）<br>
作者是从 django.contrib.auth.models 导入的<br>
### 理解ForeignKey 和 ManyToManyField。 ###
ForeignKey 表明一种一对多的关联关系,比如这里我们的文章和分类的关系，一篇文章只能对应一个分类，而一个分类下可以有多篇文章<br>
ManyToManyField 表明一种多对多的关联关系，比如这里的文章和标签，一篇文章可以有多个标签，而一个标签下也可以有多篇文章
### 迁移数据库 ###
python manage.py makemigrations 和 python manage.py migrate 命令
### 查看log ###
python manage.py sqlmigrate blog 0001
# Django处理http请求 #