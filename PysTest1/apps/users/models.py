# -*- encoding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    # 微信开发
    #openid = models.CharField(verbose_name=u"微信 openid", max_length=32, default='')
    #nickname = models.CharField(verbose_name=u"微信昵称", max_length=256, default='')
    nickname = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    #wsex = models.CharField(verbose_name=u"微信性别", max_length=3, default='')
    #province = models.CharField(verbose_name=u"微信省份", max_length=50, default='')
    #city = models.CharField(verbose_name=u"微信城市", max_length=50, default='')
    #country = models.CharField(verbose_name=u"微信国家", max_length=50, default='')
    #headimgurl = models.CharField(verbose_name=u"微信头像", max_length=200, default='')
    register_date = models.DateField(verbose_name=u'注册日期', default=datetime.now)
    is_vip = models.BooleanField(verbose_name=u"会员状态",default=False)
    #privilege = models.CharField(verbose_name=u"微信权限", max_length=3, default='')
    #unionid = models.CharField(verbose_name=u"微信 unionid", max_length=32, default='')
    #refresh_token = models.CharField(verbose_name=u"微信 refresh_token", max_length=512, default='')
    #refresh_token_time = models.IntegerField(default=0)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname
