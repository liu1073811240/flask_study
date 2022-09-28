# -- coding: utf-8 --
# @Time : 2022/9/19 17:18
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 10-ORM层外键和一对多关系.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, INT, Float, \
    Boolean, DECIMAL, Enum, DateTime, Date, Time, String, Text, func, and_, or_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship



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

    # articles = relationship("Article")

    def __repr__(self):
        return "<User(username:%s)>" % self.username


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)

    # RESTRICT：父表数据被删除，会阻止删除。默认就是这一项。
    # NO ACTION：在MySQL中，同RESTRICT。
    # CASCADE：级联删除。
    # SET NULL：父表数据被删除，子表数据会设置为NULL。
    # uid = Column(Integer, ForeignKey("user.id"))
    # uid = Column(Integer, ForeignKey("user.id", ondelete="RESTRICT"))
    # uid = Column(Integer, ForeignKey("user.id", ondelete="NO ACTION"))
    # uid = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    uid = Column(Integer, ForeignKey("user.id", ondelete="SET NULL"))

    author = relationship("User", backref="articles")

    def __repr__(self):
        return "<Article(title:%s,content=%s)>" % (self.title, self.content)


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='zhiliao')
# session.add(user)
# session.commit()
#
# article = Article(title='abc', content='123', uid=1)
# session.add(article)
# session.commit()

article = session.query(Article).first()
uid = article.uid
print(article)
user = session.query(User).get(uid)
print(user)

article = session.query(Article).first()
print(article.author.username)

user = session.query(User).first()
print(user.articles)
