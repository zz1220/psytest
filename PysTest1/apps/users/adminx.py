# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2/23/20'
import xadmin
from .models import UserProfile
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


# class UserProfileAdmin(object):
#     list_display = ('o_id', 'o_desc', 'question')
#     search_fields = ('o_id', 'o_desc', 'question')
#     list_filter = ('o_id', 'o_desc', 'question')
#
#
# xadmin.site.register(UserProfile, UserProfileAdmin)
