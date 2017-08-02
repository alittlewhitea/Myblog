Myblog
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
