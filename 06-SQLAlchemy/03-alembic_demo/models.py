# -- coding: utf-8 --
# @Time : 2022/12/19 17:57
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : models.py
# @Software: PyCharm

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = '127.0.0.1'  # 主机名
PROT = '3306'
DATABASE = 'alembic_demo'
USERNAME = 'root'
PASSWORD = 'hui0202'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PROT, db=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    age = Column(Integer, default=0)
    country = Column(String(50))
    persons = Column(String(5000))


# Base.metadata.drop_all()
# Base.metadata.create_all()


# ORM -> 迁移脚本 -> 迁移到数据库中
# alembic init alembic # (修改alembic.init配置文件 )
# alembic revision --autogenerate -m "first commit"
# alembic upgrade head

# 更新数据库
# alembic revision --autogenerate -m "first commit"   
# alembic upgrade head      
