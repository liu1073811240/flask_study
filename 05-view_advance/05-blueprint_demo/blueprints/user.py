# -- coding: utf-8 --
# @Time : 2022/7/11 19:53
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : user.py
# @Software: PyCharm

from flask import Blueprint


user_bp = Blueprint('user', __name__)

# 个人中心的url与视图函数
@user_bp.route('/profile/')
def profile():
    return '个人中心页面'


@user_bp.route('/settings/')
def settings():
    return '个人设置页面'

