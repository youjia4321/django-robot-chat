from django import forms
from captcha.fields import CaptchaField
from robot.models import Users

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', min_length=1, error_messages={'required': '请填写用户名', 'max_length':'用户名过长', 'min_length': '用户名过短'})
    password = forms.CharField(label='密码', min_length=6, max_length=20, error_messages={'required': '请填写用密码','max_length':'密码过长', 'min_length': '密码过短'})


class RegisterForm(forms.Form):
    email = forms.EmailField(label='邮箱', min_length=3, error_messages={'required': '请填写电子邮件', 'min_length': '邮箱过短'})
    username = forms.CharField(label='用户名', min_length=1, error_messages={'required': '请填写用户名', 'max_length':'用户名过长', 'min_length': '用户名过短'})
    password = forms.CharField(label='密码', min_length=6, max_length=20, error_messages={'required': '请填写密码','max_length':'密码过长', 'min_length': '密码过短'})
    captcha = forms.CharField(label='验证码',  error_messages={'required': '请填写验证码'})


class registerForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'username', 'password']