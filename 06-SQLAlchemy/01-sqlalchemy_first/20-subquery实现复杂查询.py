# -- coding: utf-8 --
# @Time : 2022/12/15 16:07
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 20-subquery实现复杂查询.py
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
    city = Column(String(50), nullable=False)
    age = Column(Integer, default=0)

    def __repr__(self):
        return "<User(username: %s)>" % self.username


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username='李A', city="长沙", age=18)
# user2 = User(username='王B', city="长沙", age=18)
# user3 = User(username='赵C', city="北京", age=18)
# user4 = User(username='张D', city="长沙", age=20)
#
# session.add_all([user1, user2, user3, user4])
# session.commit()

# 婚恋
# 寻找和李A这个人在同一个城市，并且是同年龄的人。
# user = session.query(User).filter(User.username == '李A').first()
# users = session.query(User).filter(User.city == user.city, User.age == user.age).all()
# print(users)

stmt = session.query(User.city.label("city"), User.age.label("age")).filter(User.username == '李A').subquery()
result = session.query(User).filter(User.city == stmt.c.city, User.age == stmt.c.age).all()
print(result)

