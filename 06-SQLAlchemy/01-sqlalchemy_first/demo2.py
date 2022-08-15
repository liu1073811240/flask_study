# -- coding: utf-8 --
# @Time : 2022/8/2 19:14
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : demo2.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = '127.0.0.1'  # 主机名
PROT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'hui0202'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PROT, db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

# create table person(id int primary key autoincrement,
# name varchar(5), age, int)

# 1. 创建一个ORM模型，这个ORM模型必须继承自sqlalchemy给我们提供的类。
class Person(Base):
    __tablename__ = 'person'  # 数据库中的表名

    # 2. 在这个ORM模型中创建一些属性，来跟表中的字段进行一一映射。
    # 这些属性必须是sqlalchemy给我们提供好的数据类型。
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    country = Column(String(50))

# 3. 将创建好的ORM模型， 映射到数据库中。
Base.metadata.create_all()

# 4. 一旦使用了`Base.metadata.create_all()`
# 将模型映射到数据库中以后，即使改变了模型的字段，也不会重新映射了。
