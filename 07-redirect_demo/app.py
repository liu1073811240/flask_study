from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/login/')
def login():
    return '这是登录页面'

@app.route('/profile/')
def profile():
    if request.args.get("name"):
        return "这是个人中心页面"
    else:
        return redirect(url_for('login'))  # 重定向页面


if __name__ == '__main__':
    app.run()
