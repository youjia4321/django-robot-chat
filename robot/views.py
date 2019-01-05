from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
import requests
import json
from django.db.models import Q
from robot.models import Chat, Users
from robot.forms import LoginForm
from django.contrib.auth import login, logout
# Create your views here.


def get_response(info):
        # 调用图灵机器人API
        url = 'http://www.tuling123.com/openapi/api?key=80baea7bc2fb422bbba097909952e90c&info=' + info
        res = requests.get(url)
        res.encoding = 'utf-8'
        jd = json.loads(res.text)
        return jd['text']


class Index(View):
    def get(self, request):
        print('app robot 中的 index视图')
        # raise ValueError("呵呵")
        # return HttpResponse("O98K")
        # if request.user.username == '':
        #     print(request.user.username+"#######")
        #     return render(request, 'login.html', {})
        return render(request, 'index.html', {})

    def render(self):
        print("in index/render")
        return HttpResponse("O98K")

    def post(self, request):
        comment = request.POST.get('comment', '')
        recevie = get_response(comment)
        # print(comment, recevie)
        chat1 = Chat(chat_comment=comment)
        chat2 = Chat(chat_comment=recevie)
        chat1.save()
        chat2.save()
        return render(request, 'index.html', {'comment': comment, 'recevie': recevie})


def record(request):
    # if request.user.username == '':
    #     print(request.user.username+"#######")
    #     return render(request, 'login.html', {})
    all_chats = Chat.objects.all()
    return render(request, 'record.html', {'all_chats': all_chats})


def check(username=None, password=None):
    try:
        user = Users.objects.get(Q(username=username) | Q(email=username))
        if user.check_password(password):
            return user
    except Exception as e:
        return None


# class Login(View):
#     def get(self, request):
#         return render(request, 'login.html', {})

#     def post(self, request):
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             username = request.POST.get('username', '')
#             password = request.POST.get('password', '')
#             user = check(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return render(request, 'index.html', {})
#             else:
#                 return render(request, 'login.html', {'msg': "用户不存在或密码错误"})
#         else:
#             return render(request, 'login.html', {'login_form': login_form})

def logoutView(request):
    logout(request)
    return render(request, 'login.html', {})
