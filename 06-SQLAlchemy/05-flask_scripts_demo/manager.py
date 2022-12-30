# -- coding: utf-8 --
# @Time : 2022/12/28 16:14
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : manager.py
# @Software: PyCharm

from flask_script import Manager
from app import app, BackendUser, db
from db_script import db_manager


manager = Manager(app)
manager.add_command("db", db_manager)
# python manage.py db init

@manager.command
def greet():
    print("你好")

# python manager.py add_user -u zhiliao -a 18
# @manager.option("-u", "--username", dest="username")
# @manager.option("-a", "--age", dest="age")
# def add_user(username, age):
#     print("您输入的用户名是：%s, 年龄：%s".format(username, age))

@manager.option("-u", "--username", dest="username")
@manager.option("-e", "--email", dest="email")
def add_user(username, email):
    user = BackendUser(username=username, email=email)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()

