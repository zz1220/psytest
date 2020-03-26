# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '3/12/20'

from datetime import datetime

import users


def user_count():
    total = users.objects.all().count()
    return total


def new_user_count():
    today_user_count = users.objects.filter(register_date=datetime.today).count()
    return today_user_count


