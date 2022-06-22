from flask import Flask, render_template

app = Flask(__name__, template_folder='D:/Downloads/templates')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/list/')
def my_list():
    return render_template('posts/lists.html')


if __name__ == '__main__':
    app.run(debug=True)
