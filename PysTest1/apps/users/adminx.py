# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2/23/20'

import users
import xadmin
from xadmin.plugins.auth import UserAdmin, User
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _
from .models import UserProfile, UserReport
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    site_title = "酷炫脑后台管理系统"
    site_footer = "CoolBrain"
    menu_style = "accordion"


xadmin.site.register(views.CommAdminView, GlobalSetting)


class UserProfileAdmin(UserAdmin):
    # data_charts = {
    #     "user_count": {'title': u"User Report", "x-field": "register_date", "y-field": "id",
    #                    "order": ("register_date",)},
    # }
    pass


xadmin.site.unregister(User)
xadmin.site.register(UserProfile, UserProfileAdmin)


class UserReportAdmin(object):
    # list_display = ['today_date', "user_today_cnt"]
    # list_per_page = 20
    data_charts = {
        "user_count": {'title': u"User Report", "x-field": "today_date", "y-field": ("user_today_cnt",),
                       "order": ("id",)},
    }


xadmin.site.register(UserReport, UserReportAdmin)
