from flask import Flask, render_template

app = Flask(__name__)
app.config.update({'DEBUG': True, 'TEMPLATES_AUTO_RELOAD': True})


@app.route('/')
def index():  # put application's code here
    context = {
        'username': 'zhiliao',
        'age': 17,
    }

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
