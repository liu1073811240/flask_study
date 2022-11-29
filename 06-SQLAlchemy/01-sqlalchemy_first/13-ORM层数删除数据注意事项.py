# -- coding: utf-8 --
# @Time : 2022/11/4 17:18
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 13-ORM层数删除数据注意事项.py
# @Software: PyCharm

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


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)

    uid = Column(Integer, ForeignKey("user.id"), nullable=False)
    author = relationship("User", backref='articles')


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='zhiliao')
# article = Article(title='hello world')
# article.author = user
# session.add(article)
# session.commit()


user = session.query(User).first()
session.delete(user)
session.commit()


