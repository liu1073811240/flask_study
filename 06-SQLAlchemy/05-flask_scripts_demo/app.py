from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

ctx = app.app_context()
ctx.push()
# a = current_app
# ctx.pop()

db = SQLAlchemy(app)

class BackendUser(db.Model):
    __tablename__ = 'backend_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

db.drop_all()
db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
