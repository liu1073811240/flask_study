# -- coding: utf-8 --
# @Time : 2022/12/29 16:34
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : db_script.py
# @Software: PyCharm
from flask_script import Manager

db_manager = Manager()

@db_manager.command
def init():
    print('迁移仓库创建完毕！')

@db_manager.command
def revision():
    print("迁移脚本生成成功")

@db_manager.command
def upgrade():
    print("脚本迁移到数据库成功")


