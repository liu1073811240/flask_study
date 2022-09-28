# -- coding: utf-8 --
# @Time : 2022/8/25 17:15
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 07-query函数可查询的数据.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, INT, Float, \
    Boolean, DECIMAL, Enum, DateTime, Date, Time, String, Text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import date, datetime, time
import random


HOSTNAME = '127.0.0.1'  # 主机名
PROT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'hui0202'


DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PROT, db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

# Session = sessionmaker(engine)
# session = Session()

session = sessionmaker(engine)()

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return "<Article(title:%s)>" % self.title

# Base.metadata.drop_all()
# Base.metadata.create_all()

# for x in range(6):
#     article = Article(title='title%s' % x, price=random.randint(1, 100))
#     session.add(article)
# session.commit()

# 模型对象
articles = session.query(Article).all()
for article in articles:  # 指定查找这个模型中的所有对象
    print(article)  # <Article(title:title0)>

# 模型中的属性
articles = session.query(Article.title, Article.price).all()
print(articles)

# 聚合函数
# result = session.query(func.count(Article.id)).first()  # 计数
# result = session.query(func.avg(Article.price)).first()  # 计算平均值
# result = session.query(func.max(Article.price)).first()  # 计算最大值
result = session.query(func.sum(Article.price)).first()  # 计算求和
print(result)
print(func.sum())


