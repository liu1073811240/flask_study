from flask import Flask, views, url_for, jsonify, render_template

app = Flask(__name__)


# 有几个url需要返回json数据
# 有几个视图，是需要返回相同的变量

class JSONView(views.View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):  # 分发请求
        return jsonify(self.get_data())


class ListView(JSONView):
    def get_data(self):
        return {"username": "zhiliao", 'password': '111111'}


app.add_url_rule('/list/', endpoint='my_list', view_func=ListView.as_view('list'))

class ADSView(views.View):
    def __init__(self):
        super(ADSView, self).__init__()
        self.context = {
            'ads': "几年过节不收礼",
        }

class LoginView(ADSView):
    def dispatch_request(self):
        self.context.update({
            "username": 'zhiliao',
        })
        return render_template('login.html', **self.context)


class RegistView(ADSView):
    def dispatch_request(self):
        return render_template('register.html', **self.context)


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))


# with app.test_request_context():
#     print(url_for('my_list'))


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
