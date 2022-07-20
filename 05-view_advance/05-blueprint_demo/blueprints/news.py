# -- coding: utf-8 --
# @Time : 2022/7/11 19:55
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : news.py
# @Software: PyCharm

from flask import Blueprint, render_template, url_for

# 指定模板文件路径，还可以指定静态文件的查找路径。
news_bp = Blueprint('news', __name__, url_prefix='/news', template_folder='zhiliao', static_folder='zhiliao_static')


@news_bp.route('/list/')
def news_list():
    print(url_for('news.new_detail'))
    return render_template('news_list.html')


@news_bp.route('/detail/')
def new_detail():
    return '新闻详情页面'

