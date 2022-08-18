# -- coding: utf-8 --
# @Time : 2022/7/21 17:24
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-连接数据库.py
# @Software: PyCharm

from sqlalchemy import create_engine

HOSTNAME = '127.0.0.1'  # 主机名
PROT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'hui0202'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PROT, db=DATABASE)

engine = create_engine(DB_URI)

# 判断是否连接成功
conn = engine.connect()
result = conn.execute('select 1')
print(result.fetchone())

# 先进入终端：MySQL 8.0 Command Line Client
# 再来执行这段程序


class Person(object):
    name = 'xx'
    age = 18
    country = 'xx'


# Person类 -> 数据库中的一张表
# Person类中的属性 -> 数据库中的一张表字段
# Person类的一个对象 -> 数据库中表的一条数据

