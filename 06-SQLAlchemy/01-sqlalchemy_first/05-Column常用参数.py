# -- coding: utf-8 --
# @Time : 2022/8/17 18:03
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 05-Column常用参数.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, INT, Float, \
    Boolean, DECIMAL, Enum, DateTime, Date, Time, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import date, datetime, time

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
    create_time = Column(DateTime, default=datetime.now)  # 默认填写当前的时间
    read_count = Column(Integer)

    # title = Column(String(50), nullable=False)  # 设置为False不能为空，否则报错

    telephone = Column(String(11), unique=True)


Base.metadata.drop_all()
Base.metadata.create_all()


article1 = Article(telephone='12345678987')
article2 = Article(telephone='12345678927')
# article.create_time = datetime.now()
# article1.title = 'abc'

# session.add(article1)
session.add_all([article1, article2])
session.commit()

