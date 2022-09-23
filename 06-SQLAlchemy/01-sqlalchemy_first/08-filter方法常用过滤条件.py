# -- coding: utf-8 --
# @Time : 2022/8/29 17:34
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 08-filter方法常用过滤条件.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String, INT, Float, \
    Boolean, DECIMAL, Enum, DateTime, Date, Time, String, Text, func, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
    price = Column(Float, nullable=False)
    context = Column(Text)

    def __repr__(self):
        return "<Article(title:%s)>" % self.title


# 1. equal
# article = session.query(Article).filter(Article.id == 1).first()
# article = session.query(Article).filter(Article.title == "title0").first()

# 2. not equal
# article = session.query(Article).filter(Article.title != "title0").first()
# print(article)

# 3. like  & ilike (不区分大小写)
# articles = session.query(Article).filter(Article.title.like('title%')).all()
# print(articles)

# 4. in
# articles = session.query(Article).filter(Article.title.in_(['title1', 'title2'])).all()
# print(articles)

# 5. not in
# articles = session.query(Article).filter(~Article.title.in_(['title1', 'title2'])).all()
# articles = session.query(Article).filter(Article.title.notin_(['title1', 'title2'])).all()
# print(articles)

# 6. is null
# articles = session.query(Article).filter(Article.context==None).all()
# print(articles)

# 7. is not null
# articles = session.query(Article).filter(Article.context != None).all()
# print(articles)

# 8. and
# articles = session.query(Article).filter(Article.title == 'abc' and Article.context == 'abc').all()
# articles = session.query(Article).filter(Article.title == 'abc', Article.context == 'abc').all()
# print(articles)

# 9. or
articles = session.query(Article).filter(or_(Article.title == 'abc', Article.context == 'abc')).all()
# articles = session.query(Article).filter(or_(Article.title == 'abc', Article.context == 'abc'))
print(articles)

