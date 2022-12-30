# -- coding: utf-8 --
# @Time : 2022/12/29 17:31
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : models.py
# @Software: PyCharm

from exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)

