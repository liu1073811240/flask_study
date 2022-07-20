# -- coding: utf-8 --
# @Time : 2022/7/19 19:32
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : cms.py
# @Software: PyCharm

from flask import Blueprint

cms_bp = Blueprint('cms', __name__, subdomain='cms')  # 子域名


@cms_bp.route('/')
def index():
    return 'cms index page'