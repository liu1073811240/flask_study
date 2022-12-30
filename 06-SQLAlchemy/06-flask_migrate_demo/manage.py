# -- coding: utf-8 --
# @Time : 2022/12/29 17:54
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : manage.py
# @Software: PyCharm

from flask_script import Manager
from app import app
from exts import db
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()


# 终端常用命令
# python manage.py db init    初始化迁移文件

# python manage.py db migrate   将模型的映射添加到文件中

# python manage.py db upgrade    将映射文件真正呢映射到数据库中

