# -- coding: utf-8 --
# @Time : 2022/11/23 15:56
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 14-cascade参数.py
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

    # articles = relationship("Article", cascade="save-update,delete")

    # comments = relationship("Comment")

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    uid = Column(Integer, ForeignKey("user.id"))

    author = relationship("User", backref=backref("articles", cascade="save-update,delete,delete-orphan,merge,expunge"),
                          cascade="save-update", single_parent=True)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    uid = Column(Integer, ForeignKey("user.id"))

    author = relationship("User", backref=backref("comments"))

def my_init_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    user = User(username='zhiliao')

    article = Article(title='title one')
    article.author = user

    comment = Comment(content='xxx')
    comment.author = user

    session.add(comment)
    session.add(article)
    session.commit()

def operation():
    # user = session.query(User).first()
    # session.delete(user)
    # user.articles = []
    # session.commit()

    user = User(id=1, username='ketang')
    article = Article(id=2, title='22343422')
    user.articles.append(article)

    session.merge(user)
    session.merge(article)
    session.commit()


if __name__ == '__main__':
    # my_init_db()
    operation()


