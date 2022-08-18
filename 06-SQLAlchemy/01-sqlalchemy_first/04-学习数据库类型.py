# -- coding: utf-8 --
# @Time : 2022/8/15 16:38
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 04-学习数据库类型.py
# @Software: PyCharm
from sqlalchemy import create_engine, Column, Integer, String, INT, Float, \
    Boolean, DECIMAL, Enum, DateTime, Date, Time, String, Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum  # 在python3中有


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

class TagEnum(enum.Enum):
    python = "python"
    flask = "flask"
    django = "django"

# 定义表 模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # price = Column(Float)
    price = Column(DECIMAL(10, 4))  # 第一个参数是用来标记这个字段能存储多少个数字，第二个参数表示小数点后有多少位。
    is_delete = Column(Boolean)

    # tag = Column(Enum("python", "flask", "django"))
    tag = Column(Enum(TagEnum))

    # create_time = Column(Date)
    # create_time = Column(DateTime)
    create_time = Column(Time)

    title = Column(String(50))

    # content = Column(Text)
    content = Column(LONGTEXT)

from datetime import date, datetime, time

Base.metadata.drop_all()  # 删除绑定在base上面的 表
Base.metadata.create_all()  # 再重新创建表

# article = Article(tag='python')
# article = Article(tag=TagEnum.python)
# article = Article(create_time=date(2022, 8, 16))
# article = Article(create_time=datetime(2022, 8, 16, 11, 11, 11))
# article = Article(create_time=time(hour=11, minute=11, second=11))
# article = Article(title='abc')
article = Article(content='abc')

session.add(article)
session.commit()
