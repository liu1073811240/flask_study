from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/list/')
def article_list():
    return 'article list'

# http://127.0.0.1:5000/p/文章1/
@app.route('/p/<article_id>/')
def article_detail(article_id):
    return '您请求的文章是：%s' % article_id

# http://127.0.0.1:5000/article/1.0/aa/
@app.route('/article/<path:test>/')
def test_article(test):
    return 'test article: %s' % test

# http://127.0.0.1:5000/u/ae16ef69-bee0-453c-95db-1c2c3156f8bf
@app.route('/u/<uuid:user_id>/')
def user_detail(user_id):
    return '用户个人中心页面：%s' % user_id

# import uuid
# print(uuid.uuid4())
# uuid数据类型只能接收符合uuid的字符串。uuid是一个唯一的字符串,一般可以用来做表的主键

# /blog/<id>/
# /usr/<id>/
# http://127.0.0.1:5000/user/1/
@app.route('/<any(blog, user):url_path>/<id>/')
def detail(url_path, id):
    if url_path == 'blog':
        return '博客详情：%s' % id
    else:
        return '用户详情：%s' % id

# 通过问号的形式传递参数
# http://127.0.0.1:5000/d/?wd=python
# http://127.0.0.1:5000/d/?wd=python&ie=utf-8
@app.route('/d/')
def d():
    wd = request.args.get('wd')
    ie = request.args.get('ie')
    print('id:', ie)
    return '您通过查询字符串的方式传递的参数是：%s' % wd


if __name__ == '__main__':
    app.run()
