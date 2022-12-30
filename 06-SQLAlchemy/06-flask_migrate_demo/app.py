from flask import Flask
from exts import db
import config
# 需要把映射到数据库中的模型导入到manage.py文件中。
from models import User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/profile/")
def profile():
    pass

if __name__ == '__main__':
    app.run()
