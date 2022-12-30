# -- coding: utf-8 --
# @Time : 2022/12/27 17:57
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : config.py
# @Software: PyCharm


HOSTNAME = '127.0.0.1'  # 主机名
PROT = '3306'
DATABASE = 'flask_alembic_demo'
USERNAME = 'root'
PASSWORD = 'hui0202'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PROT, db=DATABASE)


SQLALCHEMY_DATABASE_URI = DB_URI

