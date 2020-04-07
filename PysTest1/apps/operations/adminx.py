# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2/23/20'

from django import forms
from django.forms import CheckboxSelectMultiple

import xadmin
from operations.models import UserPay, PopUp, UserEvaluation, UserReviewForEvaluation
from users.models import UserProfile


class UserEvaluationAdmin(object):
    list_display = ('eval', 'eval_user', 'eval_score', 'created_on', 'payment_status')
    search_fields = ('eval', 'eval_user', 'eval_score', 'created_on', 'payment_status')
    list_filter = ('eval', 'eval_user', 'eval_score', 'created_on', 'payment_status')


xadmin.site.register(UserEvaluation, UserEvaluationAdmin)


class UserReviewForEvaluationAdmin(object):
    list_display = ('review_user', 'review_eval', 'review', 'created_on')
    search_fields = ('review_user', 'review_eval', 'review', 'created_on')
    list_filter = ('review_user', 'review_eval', 'review', 'created_on')


xadmin.site.register(UserReviewForEvaluation, UserReviewForEvaluationAdmin)


class TargetUserForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                           queryset=UserProfile.objects.all())

    class Meta:
        model = PopUp
        fields = '__all__'


class PopUpAdmin(object):
    list_display = ('title', 'image', 'url', 'status', 'add_time', 'target_user')
    search_fields = ('title', 'image', 'url', 'status', 'add_time', 'target_user')
    list_filter = ('title', 'image', 'url', 'status', 'add_time', 'target_user')
    form = TargetUserForm


xadmin.site.register(PopUp, PopUpAdmin)


class UserPayAdmin(object):
    list_display = ('payment_user', 'amount', 'payment_type', 'add_time')
    search_fields = ('payment_user', 'amount', 'payment_type', 'add_time')
    list_filter = ('payment_user', 'amount', 'payment_type', 'add_time')


xadmin.site.register(UserPay, UserPayAdmin)
