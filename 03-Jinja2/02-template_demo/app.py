from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    context = {'username': 'zhiliao',
               'age': '18',
               'country': 'China',
               'children': {
                   'name': 'abc',
                   'height': 180
               }}
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
