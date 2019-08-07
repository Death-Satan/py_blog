# Djwango2.1+layui
## 环境要求
~~~
本地环境： python3.7,Mysql >=5.6
Python库:Django2.1,Fillow,pymysql  
~~~
## 安装步骤
~~~
修改bbs\settings.py 
ALLOWED_HOSTS = 域名
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库名',
        'USER':'用户名',
        'PASSWORD':"密码",
        'HOST':'mysql服务器地址',
        'PORT':'端口',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",//此处不动
            'charset': 'utf8mb4',
        },
    }
}
项目根目录下打开shell或cmd
python manage.py makemigrations
python manage.py migrate
启动django自带开发服务器
python manage.py runserver 0.0.0.0:80
访问本地localhost
~~~
