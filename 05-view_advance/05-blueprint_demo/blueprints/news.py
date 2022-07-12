# -- coding: utf-8 --
# @Time : 2022/7/11 19:55
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : news.py
# @Software: PyCharm

from flask import Blueprint

news_bp = Blueprint('news', __name__)

@news_bp.route('/list/')
def news_list():
    return '新闻列表'


@news_bp.route('/detail/')
def new_detail():
    return '新闻详情页面'
