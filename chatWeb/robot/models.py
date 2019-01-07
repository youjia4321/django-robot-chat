from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Users(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='用户昵称', default='')
    gender = models.CharField(max_length=6, choices=(('男', '男'), ('女', '女')), default='female', verbose_name='性别')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    captcha = models.CharField(max_length=100, default='', verbose_name='验证码') # 注册时输入的验证码

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Chat(models.Model):
    chat_comment = models.CharField(max_length=500, verbose_name="聊天内容")
    send_time = models.DateTimeField(default=timezone.now, verbose_name="发送时间")

    class Meta:
        verbose_name = '聊天记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.chat_comment