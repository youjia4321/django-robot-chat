from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', min_length=1, error_messages={'required': '请填写用户名', 'max_length':'用户名过长', 'min_length': '用户名过短'})
    password = forms.CharField(label='密码', min_length=6, max_length=20, error_messages={'required': '请填写用密码','max_length':'密码过长', 'min_length': '密码过短'})

