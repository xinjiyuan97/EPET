
"""
Title: 用户个人信息处理（网页）
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
    username = fields.CharField( # 学号，下同
        required = True,
        min_length = 8,
        max_length = 8,
        widget = widgets.TextInput(attrs = {'name':'name', 'placeholder': '学号', 'readonly': 'readonly'}),
    )
    
    name = fields.CharField( # 姓名，下同
        required = True,
        max_length = 40,   
        error_messages = {'required': '姓名不能为空'},
    )
    
    email = fields.EmailField( # 邮箱
        required = True,
        widget = widgets.TextInput(attrs = {'placeholder': '请输入邮箱'}),
        strip = True,
        error_messages = {'required': '邮箱不能为空',
                        'invalid':'请输入正确的邮箱格式'},
    )
    
    mPhone = fields.CharField( # 手机号
        required = False,
        max_length = 11,
        min_length = 11,
        widget = widgets.TextInput(attrs = {'placeholder': '请输入手机号'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_count = UserInfo.objects.filter(email = email).count() #从数据库中查找是否用户已经存在
        if email_count:
            raise ValidationError('该邮箱已经注册！')
        return email    

class LogInForm(forms.Form):
    username = fields.CharField(
        required = True,
        widget = widgets.TextInput(attrs = {'name':'name', 'placeholder': '学号'}),
        min_length = 8,
        max_length = 8,
        error_messages = {'required': '学号不能为空'},
    )

    password = fields.CharField(
        widget = widgets.PasswordInput(attrs = {'name': 'password','placeholder': '请输入密码'}),
        required = True,
        min_length = 6,
        max_length = 20,
        strip = True,
        error_messages = {'required': '密码不能为空!',}
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = auth.authenticate(username = username, password = password) 
        
        if not user:
            raise ValidationError('用户名或密码不正确')

class SignUpForm(forms.Form):
    username = fields.CharField(
        required = True,
        widget = widgets.TextInput(attrs = {'name':'name', 'placeholder': '学号'}),
        min_length = 8,
        max_length = 8,
        error_messages = {'required': '学号不能为空',
                          'min_length': '请输入正确的学号',
                          'max_length': '请输入正确的学号'},
        validators = [RegexValidator(r'((\d{8}))', '请输入正确的学号')],
    )

    password = fields.CharField(
        widget = widgets.PasswordInput(attrs = {'name': 'password','placeholder': '请输入密码'}),
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
        widget = widgets.PasswordInput(attrs = {'name': 'password','placeholder': '再次输入密码'}),
        required = True,
        min_length = 6,
        max_length = 20,
        strip = True,
        
        error_messages = {'required': '请再次输入密码',}
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = User.objects.filter(username = username).count()
        if users:
            raise ValidationError('用户已经存在！')
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