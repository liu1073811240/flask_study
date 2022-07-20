from flask import Flask, Blueprint, url_for, render_template
from blueprints import news_bp, user_bp, cms_bp

app = Flask(__name__)

# 访问地址
# jd.com:5000
# cms.jd.com:5000

app.config['SERVER_NAME'] = 'jd.com:5000'
app.register_blueprint(user_bp)
app.register_blueprint(news_bp)
app.register_blueprint(cms_bp)

# 用户模块
# 新闻模块
# 电影模块
# 读书模块

# IP地址是不能有子域名的。
# cms.l27.0.0.1:5000
# localhost也是不能有子域名的。

@app.route('/')
def hello_world():  # put application's code here
    # print(url_for('news.news_list'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
