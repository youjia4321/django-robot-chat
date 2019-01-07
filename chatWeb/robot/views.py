from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
import requests
import json
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from robot.models import Chat, Users
from robot.forms import LoginForm, RegisterForm, registerForm
from django.contrib.auth import login, logout
# 验证码需要导入的模块
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

# 创建验证码
def captcha():
    # 验证码，第一次请求
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha
 

def jarge_captcha(captchaStr, captchaHashkey):
    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey) 
            # 如果验证码匹配
            if get_captcha.response == captchaStr.lower():  
                return True
        except:
            return False
    else:
        return False

def refresh_captcha(request):
    return HttpResponse(json.dumps(captcha()), content_type='application/json')

def get_response(info):
        # 调用图灵机器人API
        url = 'http://www.tuling123.com/openapi/api?key=(your robot key)&info=' + info
        res = requests.get(url)
        res.encoding = 'utf-8'
        jd = json.loads(res.text)
        return jd['text']


class Index(View):
    def get(self, request):
        # print('app robot 中的 index视图')
        # raise ValueError("呵呵")
        # return HttpResponse("O98K")
        if request.user.username == '':
            # print(request.user.username+"#######")
            return render(request, 'login.html', {})
        return render(request, 'index.html', {})

    def render(self):
        print("in index/render")
        return HttpResponse("O98K")

    def post(self, request):
        comment = request.POST.get('comment', '')
        recevie = get_response(comment)
        chat1 = Chat(chat_comment=comment)
        chat2 = Chat(chat_comment=recevie)
        chat1.save()
        chat2.save()
        return render(request, 'index.html', {'comment': comment, 'recevie': recevie})


def record(request):
    if request.user.username == '':
        # print(request.user.username+"#######")
        return render(request, 'login.html', {})
    all_chats = Chat.objects.all()
    return render(request, 'record.html', {'all_chats': all_chats})


def check(username=None, password=None):
    try:
        user = Users.objects.get(Q(username=username) | Q(email=username))
        if user.check_password(password):
            return user
    except Exception as e:
        return None


class Login(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = check(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {'msg': "用户不存在或密码错误"})
        else:
            return render(request, 'login.html', {'login_form': login_form})

def logoutView(request):
    logout(request)
    return render(request, 'login.html', {})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form, 'captcha': captcha})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            data = register_form.cleaned_data
            if Users.objects.filter(email=data['email']):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已存在', 'captcha': captcha})
            if Users.objects.filter(username=data['username']):
                return render(request, 'register.html', {'msg': '此用户名已被使用', 'captcha': captcha})
            captchaHashkey = request.POST.get('hashkey', '')
            if jarge_captcha(data['captcha'], captchaHashkey):
                register_form.cleaned_data['password'] = make_password(register_form.cleaned_data['password'])
                Users.objects.create(**register_form.cleaned_data)
                return render(request, 'login.html', {'msg': "注册成功,请登录..."})
            else:
                return render(request, 'register.html', {'msg': "验证码错误"})
        else:
            return render(request, 'register.html', {'register_form': register_form, 'captcha': captcha})
