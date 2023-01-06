# -- coding: utf-8 --
# @Time : 2023/1/3 15:46
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : forms.py
# @Software: PyCharm

from wtforms import Form, StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import Length, EqualTo, Email, InputRequired, NumberRange, Regexp, URL, UUID, ValidationError


class RegisterForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message='用户名长度需要在3到10之间！')])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(validators=[Length(min=6, max=10), EqualTo("password")])


class LoginForm(Form):
    # email = StringField(validators=[Email()])
    # username = StringField(validators=[InputRequired()])
    # age = IntegerField(validators=[NumberRange(12, 100)])
    # phone = StringField(validators=[Regexp(r'1[38745]\d{9}')])
    # homepage = StringField(validators=[URL()])
    # uuid = StringField(validators=[UUID()])
    captcha = StringField(validators=[Length(4, 4)])

    # 自定义表单验证器
    def validate_captcha(self, field):
        # print(type(field))
        print(field.data)
        if field.data != '1234':
            raise ValidationError("验证码错误！")


class SettingsForm(Form):
    username = StringField("用户名", validators=[InputRequired()])
    age = IntegerField("年龄", validators=[NumberRange(12, 100)])
    remember = BooleanField("记住我")
    tags = SelectField("标签", choices=[('1', 'python'), ('2', 'ios'), ('3', 'java'), ('4', 'C++')])


