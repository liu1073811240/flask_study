from flask import Flask, request, views

from functools import wraps

app = Flask(__name__)


def login_required(func):
    @wraps(func)  # 防止先前的变量丢失
    def wrapper(*args, **kwargs):
        # /setting/?username=xxx
        username = request.args.get('username')
        if username and username == 'zhiliao':
            return func(*args, **kwargs)
        else:
            return '请先登录'

    return wrapper


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# http://127.0.0.1:5000/settings/?username=zhiliao
@app.route('/settings/')
@login_required
def settings():
    return '这是设置界面'

# login_required(app.route('setttings/')(settings))
# app.route('setttings/')(login_required)(settings)


# 在类视图添加装饰器
class ProfileView(views.View):
    decorators = [login_required]

    def dispatch_request(self):
        return '这是个人中心界面'


app.add_url_rule('/profile/', view_func=ProfileView.as_view('profile'))  # 调用视图函数


if __name__ == '__main__':
    app.run()
