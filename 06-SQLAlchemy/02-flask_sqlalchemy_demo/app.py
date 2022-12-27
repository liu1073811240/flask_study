from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from flask_migrate import Migrate
from sqlalchemy.orm import backref

app = Flask(__name__)

HOSTNAME = '127.0.0.1'  # 主机名
PROT = '3306'
DATABASE = 'flask_sqlalchemy_demo'
USERNAME = 'root'
PASSWORD = 'hui0202'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PROT, db=DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UserModel(db.Model):
    __tablename__ = 'user_model'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<User(username: %s)>" % self.username


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey("user_model.id"))
    author = db.relationship("User", backref="articles")


db.drop_all()
db.create_all()

# user = User(username='zhiliao')
# article = Article(title='title one')
# article.author = user
# db.session.add(article)
# db.session.commit()

# users = User.query.all()
# users = User.query.order_by(User.id.desc()).all()
# print(users)

# user = User.query.filter(User.username=='zhiliao1').first()  # 查询出值
# print(user)
# user.username = 'zhiliao1'
# db.session.delete(user)
# db.session.commit()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


