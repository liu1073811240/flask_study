from flask import Flask
import config


app = Flask(__name__)
# app.config.from_object(config)
app.config.from_pyfile("config.txt", silent=False)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
