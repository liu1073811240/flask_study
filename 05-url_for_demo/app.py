from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # print(url_for('my_list', page=1))  # /list/1

    # return url_for('my_list', page=1, count=2)
    return url_for('login', next='/')


@app.route('/login/')
def login():
    return 'login'


@app.route('/list/<page>/')
def my_list(page):
    return 'my list'

@app.route('/detail/<id>/')
def detail():
    return 'detail'

if __name__ == '__main__':
    app.run()
