# -- coding: utf-8 --
# @Time : 2022/12/13 17:47
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 18-group_by和having字句.py
# @Software: PyCharm

from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, INT, Float, \
    Boolean, DECIMAL, Enum, DateTime, Date, Time, String, Text, func, and_, or_, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

HOSTNAME = '127.0.0.1'  # 主机名
PROT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'hui0202'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PROT, db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    age = Column(Integer, default=0)
    gender = Column(Enum("male", "female", "secret"), default="male")


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username='张三', age=17, gender='male')
# user2 = User(username='李四', age=17, gender='male')
# user3 = User(username='王五', age=18, gender='female')
# user4 = User(username='张伟', age=19, gender='female')
# user5 = User(username='知了', age=20, gender='secret')
#
# session.add_all([user1, user2, user3, user4, user5])
# session.commit()

# 每个年龄的人数
# from sqlalchemy.orm.query import Query
# result = session.query(User.age, func.count(User.id)).group_by(User.age)
# result = session.query(User.age, func.count(User.id)).group_by(User.age).all()
result = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age < 18)
# result = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age < 18).all()

print(result)



