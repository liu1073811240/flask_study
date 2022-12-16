# -- coding: utf-8 --
# @Time : 2022/12/14 16:40
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 19-join实现复杂查询.py
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

    def __repr__(self):
        return "<User(username: %s)>" % self.username


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    uid = Column(Integer, ForeignKey("user.id"))

    author = relationship("User", backref="articles")

    def __repr__(self):
        return "<Article(title: %s)>" % self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username='zhiliao')
# user2 = User(username='ketang')
#
# for x in range(1):
#     article = Article(title='title %s' % x)
#     article.author = user1
#     session.add(article)
# session.commit()
#
# for x in range(1, 3):
#     article = Article(title='title %s' % x)
#     article.author = user2
#     session.add(article)
# session.commit()

# 找到所有的用户，按照发表的文章数量进行排序
# result = session.query(User.username, func.count(Article.id)).join(Article, User.id==Article.uid).group_by(User.id)\
#     .order_by(func.count(Article.id).desc())
result = session.query(User.username, func.count(Article.id)).join(Article, User.id==Article.uid).group_by(User.id)\
    .order_by(func.count(Article.id).desc()).all()
print(result)


