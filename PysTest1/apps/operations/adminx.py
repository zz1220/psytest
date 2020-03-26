# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2/23/20'
import xadmin
from operations.models import UserPay, PopUp


class UserPayAdmin(object):
    list_display = ('payment_user', 'amount', 'payment_type', 'add_time')
    search_fields = ('payment_user', 'amount', 'payment_type', 'add_time')
    list_filter = ('payment_user', 'amount', 'payment_type', 'add_time')


xadmin.site.register(UserPay, UserPayAdmin)


class PopUpAdmin(object):
    list_display = ('title', 'image', 'url', 'status', 'add_time', 'target_user')
    search_fields = ('title', 'image', 'url', 'status', 'add_time', 'target_user')
    list_filter = ('title', 'image', 'url', 'status', 'add_time', 'target_user')


xadmin.site.register(PopUp, PopUpAdmin)
