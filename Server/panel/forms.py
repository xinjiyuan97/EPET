
"""
Title: 用户个人信息设置 & 密码修改（网页）
Author: xinjiyuan97
Date: 2018-3-18
"""

from django.forms import fields, widgets
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import auth
from users.models import UserInfo

class InformationForm(forms.Form):
    # 用户信息表单
    
    
    name = fields.CharField( # 姓名，下同
        required = True,
        max_length = 40,   
        error_messages = {'required': '姓名不能为空'},
        widget = widgets.TextInput(attrs = {'name': 'name',  'readonly': 'readonly', 'class': 'form-control1'})
    )
    
    id = fields.CharField( # 学号，下同
        required = True,
        min_length = 8,
        max_length = 8,
        widget = widgets.TextInput(attrs = {'name':'name', 'readonly': 'readonly', 'class': 'form-control1'}),
    )

    email = fields.EmailField( # 邮箱
        required = True,
        widget = widgets.TextInput(attrs = {'placeholder': '请输入邮箱', 'class': 'form-control1'}),
        strip = True,
        error_messages = {'required': '邮箱不能为空',
                        'invalid':'请输入正确的邮箱格式'},
    )
    
    mPhone = fields.CharField( # 手机号
        required = False,
        max_length = 11,
        min_length = 11,
        widget = widgets.TextInput(attrs = {'placeholder': '请输入手机号', 'class': 'form-control1'})
    )

    school = fields.CharField( # 学院
        required = True,
        max_length = 100,
        min_length = 1,
        widget = widgets.TextInput(attrs = {'placeholder': '请输学院', 'class': 'form-control1'})
    )

    major = fields.CharField( # 专业
        required = True,
        max_length = 100,
        min_length = 1,
        widget = widgets.TextInput(attrs = {'placeholder': '请输专业', 'class': 'form-control1'})
    )



class ChangePwdForm(forms.Form):
    username = fields.CharField( # 学号
        required = True,
        widget = widgets.TextInput(attrs = {'name': 'username','placeholder': '请输入学号', 'class': 'form-control1', 'readonly': 'readonly'}),
        min_length = 8,
        max_length = 8
    )
    oldPassword = fields.CharField(
        required = True,
        widget = widgets.PasswordInput(attrs = {'name': 'password','placeholder': '请输入旧密码', 'class': 'form-control1'}),
        error_messages = {'required': '旧密码不能为空'},
    )

    password = fields.CharField(
        widget = widgets.PasswordInput(attrs = {'name': 'password','placeholder': '请输入新密码', 'class': 'form-control1'}),
        required = True,
        min_length = 6,
        max_length = 20,
        strip = True,
        validators=[
            RegexValidator(r'((?=.*\d))^.{6,12}$', '必须包含数字'),
            RegexValidator(r'((?=.*[a-zA-Z]))^.{6,12}$', '必须包含字母'),
            RegexValidator(r'^.(\S){6,10}$', '密码不能包含空白字符'),
        ],
        error_messages = {'required': '密码不能为空',}
    )

    pwdVerify = fields.CharField(
        widget = widgets.PasswordInput(attrs = {'name': 'password','placeholder': '再次输入密码', 'class': 'form-control1'}),
        required = True,
        min_length = 6,
        max_length = 20,
        strip = True,
        
        error_messages = {'required': '请再次输入密码',}
    )

    def clean_oldPassword(self):
        username = self.cleaned_data.get('username')
        oldPassword = self.cleaned_data.get('oldPassword')
        user = auth.authenticate(username = username, password = oldPassword)
        if user is None:
            
            raise ValidationError('密码错误！')
        return username

    def clean_pwdVerify(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('pwdVerify')
        if password1 and password2:
            if password1 != password2:
                print(password1, password2)
                raise ValidationError('两次密码不匹配！')
        return password2

    # def clean(self):
    #     self._cleanPasswordVerify()