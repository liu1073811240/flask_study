from flask import Flask, Blueprint
# from blueprints.user import user_bp
# from blueprints.news import news_bp
from blueprints import news_bp, user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(news_bp)

# 用户模块
# 新闻模块
# 电影模块
# 读书模块


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
