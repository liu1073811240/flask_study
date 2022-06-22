from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # 模板自动加载

@app.route('/')
def index():  # put application's code here
    context = {
        'position': -9,
        # 'signature': None,
        'signature': '<script>alert("hello")</script>',
        'persons': ['zhiliao', 'ketang'],
        'age': "18",
        'article': 'hello zhiliao hello world',
        'create_time':  datetime(2022, 4, 13, 16, 40, 0),
    }

    return render_template('index.html', **context)

# 注册cut过滤器
@app.template_filter('cut')
def cut(value):
    value = value.replace("hello", '')
    return value

# 自定义处理时间的过滤器
@app.template_filter('handle_time')
def hand_time(time):
    if isinstance(time, datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()  # 发表文章间隔 时间
        # print(timestamp)
        if timestamp < 60:
            return '刚刚'
        elif 60 <= timestamp < 60*60:
            minutes = timestamp / 60
            return "%s分钟前" % int(minutes)
        elif 60*60 <= timestamp < 60*60*24:
            hours = timestamp / (60*60)
            return '%s小时前' % int(hours)
        elif 60*60*24 <= timestamp < 60*60*24*30:
            days = timestamp / (60*60*24)
            return "%s天前" % int(days)
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time


if __name__ == '__main__':
    app.run(debug=True)
