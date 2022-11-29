# -- coding: utf-8 --
# @Time : 2022/11/25 17:16
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 15-排序.py
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
    create_time = Column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return "<Article(title:%s, create_time: %s)>" % (self.title, self.create_time)


# Base.metadata.drop_all()
# Base.metadata.create_all()

# article = Article(title='title2')
# session.add(article)
# session.commit()

# 排序操作
# articles = session.query(Article).order_by(Article.create_time).all()  # 以创建时间正排序
# articles = session.query(Article).order_by(Article.create_time.desc()).all()  # 以创建时间负排序
articles = session.query(Article).order_by("create_time").all()
print(articles)


