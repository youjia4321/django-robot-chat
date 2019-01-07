"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from django.urls import include
from robot.views import Index, record, logoutView, RegisterView, Login, refresh_captcha
from .settings import STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    url('captcha', include("captcha.urls")),
    path('refresh_captcha/', refresh_captcha),    # 刷新验证码，ajax
    path('', Index.as_view(), name="index"),
    path('record', record, name="search"),
    path('login', Login.as_view(), name="login"),
    path('logout', logoutView, name="logout"),
    path('register', RegisterView.as_view(), name='register'),
    # path('registerFields',register, name='registerFields'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]
