# -- coding: utf-8 --
# @Time : 2023/1/6 17:23
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : forms.py
# @Software: PyCharm
from wtforms import Form, FileField, StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class UploadForm(Form):
    avatar = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'])])

    desc = StringField(validators=[InputRequired()])




