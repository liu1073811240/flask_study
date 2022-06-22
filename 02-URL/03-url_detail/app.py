from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')  # 没有指定请求方法，默认使用GET请求。
def hello_world():  # put application's code here
    return 'Hello World!'

# 在定义url的时候, 一定要记得在后面加斜杠
# 1. 如果不加斜杠，浏览器可能访问不到。搜索引擎会将不讲斜杠和加了斜杠的视为两个url，那么就会给搜索引擎召唤造成误解。
@app.route('/list/', methods=['POST'])
def my_list():
    return 'list'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return 'success'

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=9000)
    app.run()
