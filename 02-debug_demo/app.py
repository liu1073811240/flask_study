from flask import Flask
import config

app = Flask(__name__)
# app.debug = True
# app.config.update(DEBUG=True)
# print(isinstance(app.config, dict))
app.config.from_object(config)  # 读取config文件里面的所有参数

@app.route('/')
def hello_world():  # put application's code here
    a = 1
    b = 0
    c = a / b

    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
