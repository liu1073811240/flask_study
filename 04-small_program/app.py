from flask import Flask, render_template, request

app = Flask(__name__)

movies = [{'id': '01',
           'thumbnail': 'https://img-blog.csdnimg.cn/097e0c05011e47bcb432ba997c679e29.webp',
           'title': '天才计划',
           'rating': u'7.1',
           'comment_count': 12000,
           'authors': u' 丹尼尔·雷德克里夫 / 丹尼尔·韦伯 / 伊恩·哈特'},
          {'id': '02',
           'thumbnail': 'https://img-blog.csdnimg.cn/7f2c4fbf55a141e4801ebfdac287a934.webp',
           'title': '侏罗纪世界3',
           'rating': u'6.3',
           'comment_count': 14000,
           'authors': u'克里斯·帕拉特 / 布莱丝·达拉斯·霍华德 / 劳拉·邓恩 /'},
          {'id': '03',
           'thumbnail': 'https://img-blog.csdnimg.cn/abcd9473322a423d8a008d0a59005335.webp',
           'title': '云霄之上',
           'rating': u'8.5',
           'comment_count': 16000,
           'authors': u' 陈伟鑫 / 吴嘉辉 / 聂劲权 / 应林坚 / 陈雨泽'},


          ]

tvs = [
       {'id': '04',
        'thumbnail': 'https://img-blog.csdnimg.cn/097e0c05011e47bcb432ba997c679e29.webp',
        'title': '天才计划',
        'rating': u'7.1',
        'comment_count': 12000,
        'authors': u' 丹尼尔·雷德克里夫 / 丹尼尔·韦伯 / 伊恩·哈特'},
       {'id': '05',
        'thumbnail': 'https://img-blog.csdnimg.cn/7f2c4fbf55a141e4801ebfdac287a934.webp',
        'title': '侏罗纪世界3',
        'rating': u'6.3',
        'comment_count': 14000,
        'authors': u'克里斯·帕拉特 / 布莱丝·达拉斯·霍华德 / 劳拉·邓恩 /'},
       {'id': '06',
        'thumbnail': 'https://img-blog.csdnimg.cn/abcd9473322a423d8a008d0a59005335.webp',
        'title': '云霄之上2',
        'rating': u'8.5',
        'comment_count': 16000,
        'authors': u' 陈伟鑫 / 吴嘉辉 / 聂劲权 / 应林坚 / 陈雨泽'},

       ]


@app.route('/')
def hello_world():  # put application's code here
    context = {'movies': movies, 'tvs': tvs}

    return render_template('index.html', **context)


@app.route("/list/")
def item_list():
    category = int(request.args.get('category'))
    items = None
    if category == 1:
        items = movies
    else:
        items = tvs

    return render_template('list.html', items=items)


if __name__ == '__main__':
    app.run()
