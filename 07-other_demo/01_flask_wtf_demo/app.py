from flask import Flask, request, render_template
from forms import RegisterForm, LoginForm, SettingsForm


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            return "success"
        else:
            print(form.errors)
            return "fail"


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "success"
        else:
            print(form.errors)
            return "fail"


@app.route('/settings/', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        form = SettingsForm()
        return render_template('settings.html', form=form)
    else:
        form = SettingsForm(request.form)


from uuid import uuid4
print(uuid4())

if __name__ == '__main__':
    app.run(debug=True)
