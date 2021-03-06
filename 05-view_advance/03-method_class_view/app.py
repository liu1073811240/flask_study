from flask import Flask, views, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# 基于调度方法的类视图
class LoginView(views.MethodView):
    def __render(self, error=None):  # 私有方法
        return render_template('login.html', error=error)

    def get(self):
        return self.__render()

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhiliao' and password == '111111':
            return '登录成功'
        else:
            return self.__render(error='用户名或密码错误')


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))

if __name__ == '__main__':
    app.run()
