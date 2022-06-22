from flask import Flask,  render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', username='zhiliao')

@app.route('/detail/')
def detail():
    return render_template('course_detail.html', username='zhiliao')


if __name__ == '__main__':
    app.run()
