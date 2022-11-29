# -- coding: utf-8 --
# @Time : 2022/9/28 17:21
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 11-一对一关系映射.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, INT, Float, \
    Boolean, DECIMAL, Enum, DateTime, Date, Time, String, Text, func, and_, or_, ForeignKey
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

    # extend = relationship("UserExtend", uselist=False)

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(Integer, ForeignKey("user.id"))

    # user = relationship("User")
    # user = relationship("User", backref='extend')
    user = relationship("User", backref=backref("extend", uselist=False))  # uselist=False: 设置成一对一的关系

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)

    uid = Column(Integer, ForeignKey("user.id", ondelete="SET NULL"))

    author = relationship("User", backref="articles")

    def __repr__(self):
        return "<Article(title:%s,content=%s)>" % (self.title, self.content)


Base.metadata.drop_all()
Base.metadata.create_all()

user = User(username='zhiliao')
extend1 = UserExtend(school='zhiliao ketang')
user.extend = extend1
# user.extend.append(extend1)

# print(type(user.extend))
print(type(extend1))
session.add(user)
session.commit()

# 1.
# article1 = Article(title='abc1', content='123')
# article2 = Article(title='def', content='456')
#
# user.articles.append(article1)
# user.articles.append(article2)
#
# session.add(user)
# session.commit()

# 2.
# article1 = Article(title='abc2', content='1234')
# article1.author = user
#
# session.add(article1)
# session.commit()

