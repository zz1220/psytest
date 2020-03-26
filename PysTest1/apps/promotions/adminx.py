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
    list_display = ('VIP_type', 'price')
    search_fields = ('VIP_type', 'price',)
    list_filter = ('VIP_type', 'price',)


xadmin.site.register(VIP, VIPAdmin)


class CouponAdmin(object):
    list_display = ('coupon_name', 'coupon_type', 'use_condition', 'available_date',
                    'get_type', 'get_condition', 'add_time', 'valid_date')
    search_fields = ('coupon_name', 'coupon_type', 'use_condition', 'available_date',
                     'get_type', 'get_condition', 'add_time', 'valid_date')
    list_filter = ('coupon_name', 'coupon_type', 'use_condition', 'available_date',
                   'get_type', 'get_condition', 'add_time', 'valid_date')


xadmin.site.register(Coupon, CouponAdmin)
