## Myblog
###虚拟环境下使用Virtualenv    pip install virtualenv  
###进入指定目录虚拟环境 virtualenv 文件夹路径
###激活 文件夹/Scripts/activate
###安装Django
###创建Django项目  django-admin start-project #projectname
###修改语言和时间
###把英文改为中文
###LANGUAGE_CODE = 'zh-hans'
###把国际时区改为中国时区
#####TIME_ZONE = 'Asia/Shanghai'
###运行 python manage.py runserver
###进入到manage.py文件所在位置创建应用
###python manage.py startapp appname
###使用postgresql
###pip install psycopg2
###修改settings.py文件中database中的
###DATABASES = {
######    'default': {
######        'ENGINE':'django.db.backends.postgresql_psycopg2',
######        'PASSWORD': '...',
######       'HOST': '127.0.0.1',
######    }
###测试

######python manage.py shell
######>>> from  django.db import connection
######>>> cursor = connection.cursor
