# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2/23/20'

import xadmin
from .models import Banner, VIP, Coupon


class BannerAdmin(object):
    list_display = ('title', 'image', 'url', 'index', 'add_time')
    search_fields = ('title', 'image', 'url', 'index', 'add_time')
    list_filter = ('title', 'image', 'url', 'index', 'add_time')


xadmin.site.register(Banner, BannerAdmin)


class VIPAdmin(object):
    list_display = ('vip_type', 'price', 'vip_valid_date')
    search_fields = ('vip_type', 'price', 'vip_valid_date')
    list_filter = ('vip_type', 'price', 'vip_valid_date')


xadmin.site.register(VIP, VIPAdmin)


class CouponAdmin(object):
    list_display = ('coupon_name', 'coupon_type', 'coupon_valid_date',
                    'get_type', 'get_condition', 'add_time', 'available_date')
    search_fields = ('coupon_name', 'coupon_type', 'coupon_valid_date',
                     'get_type', 'get_condition', 'add_time', 'available_date')
    list_filter = ('coupon_name', 'coupon_type', 'coupon_valid_date',
                   'get_type', 'get_condition', 'add_time', 'available_date')


xadmin.site.register(Coupon, CouponAdmin)
