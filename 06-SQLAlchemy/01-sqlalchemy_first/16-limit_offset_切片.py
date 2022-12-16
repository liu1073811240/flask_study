# -- coding: utf-8 --
# @Time : 2022/12/2 16:18
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 16-limit_offset_切片.py
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

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "<Article(title: %s)>" % self.title


"""
limit：可以限制每次查询的时候只查询几条数据。
offset：可以限制查找数据的时候过滤掉前面多少条。
切片：可以对Query对象使用切片操作，来获取想要的数据。

"""

# Base.metadata.drop_all()
# Base.metadata.create_all()
# for x in range(100):
#     title = "title %s" % x
#     article = Article(title=title)
#     session.add(article)
# session.commit()

# articles = session.query(Article).all()
# articles = session.query(Article).limit(10).all()
# articles = session.query(Article).offset(10).limit(10).all()  # 过滤掉前面十条数据、只取后面10条数据。
# articles = session.query(Article).order_by(Article.id.desc()).limit(10).all()

from sqlalchemy.orm.query import Query
# articles = session.query(Article).order_by(Article.id.desc()).slice(0, 10).all()
articles = session.query(Article).order_by(Article.id.desc())[0:10]
print(articles)

