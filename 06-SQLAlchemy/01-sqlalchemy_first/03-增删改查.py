# -- coding: utf-8 --
# @Time : 2022/8/2 20:11
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 03-增删改查.py
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
增删改查
'''

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


class Person(Base):
    __tablename__ = 'person'  # 数据库中的表名

    # 2. 在这个ORM模型中创建一些属性，来跟表中的字段进行一一映射。
    # 这些属性必须是sqlalchemy给我们提供好的数据类型。
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    country = Column(String(50))

    def __str__(self):
        return "<Person(name:%s, age:%s, country:%s)>" % (self.name, self.age, self.country)


# 增
def add_data():
    p = Person(name='zhiliao', age=18, country='china')
    session.add(p)
    session.commit()

# 增
def add_data2():
    p1 = Person(name='zhiliao1', age=19, country='china')
    p2 = Person(name='zhiliao2', age=20, country='china')
    session.add_all([p1, p2])
    session.commit()

# 查
def search_data():
    # all_person = session.query(Person).all()
    # print(all_person)
    # for p in all_person:
    #     print(p)

    # # 过滤条件查找，所有的情况
    # all_person = session.query(Person).filter_by(name='zhiliao').all()
    # all_person = session.query(Person).filter(Person.name == 'zhiliao').all()
    # for x in all_person:
    #     print(x)

    person = session.query(Person).get(10)  # 获取id为多少的数据。
    print(person)
    person = session.query(Person).first()
    print(person)


# 改
def update_data():
    person = session.query(Person).first()
    person.name = 'ketang'
    session.commit()


# 删
def delete_data():
    person = session.query(Person).first()
    session.delete(person)
    session.commit()


if __name__ == '__main__':
    # 添加对象
    # add_data2()

    # 查看对象
    # search_data()

    # 修改对象
    # update_data()
    delete_data()

