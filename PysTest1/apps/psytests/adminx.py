# -*- coding:utf-8 -*-
__author__ = '10k'
__date__ = '2/23/20'

from django import forms
from django.forms import CheckboxSelectMultiple

import xadmin
from .models import MentalEvaluation, Options


class OptionsForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(widget=CheckboxSelectMultiple, queryset=Options.objects.all())

    class Meta:
        model = MentalEvaluation
        fields = '__all__'


class MentalEvaluationAdmin(object):
    list_display = ('eval_id', 'eval_type', 'eval_title', 'eval_intro', 'eval_price',
                    'eval_created_on', 'eval_is_online', 'eval_ques_nums', 'reverse_scoring',
                    'eval_dimension', 'questions')
    search_fields = ('eval_id', 'eval_type', 'eval_title', 'eval_intro', 'eval_price',
                     'eval_created_on', 'eval_is_online', 'eval_ques_nums', 'reverse_scoring',
                     'eval_dimension', 'questions')
    list_filter = ('eval_id', 'eval_type', 'eval_title', 'eval_intro', 'eval_price',
                   'eval_created_on', 'eval_is_online', 'eval_ques_nums', 'reverse_scoring',
                   'eval_dimension', 'questions')
    # data_charts = {
    #     "user_count": {'title': u"测评统计", "x-field": 'eval_id', "y-field": "eval_price",
    #                    "order": ('eval_created_on',)},
    # }

    form = OptionsForm


xadmin.site.register(MentalEvaluation, MentalEvaluationAdmin)


# class EvalQuestionAdmin(object):
#     list_display = ('q_id', 'q_desc', 'eval', 'reverse_scoring', 'dimension')
#     search_fields = ('q_id', 'q_desc', 'eval', 'reverse_scoring', 'dimension')
#     list_filter = ('q_id', 'q_desc', 'eval', 'reverse_scoring', 'dimension')
#
#
# xadmin.site.register(EvalQuestion, EvalQuestionAdmin)


class OptionsAdmin(object):
    list_display = ('option_desc', )
    search_fields = ('option_desc', )
    list_filter = ('option_desc', )


xadmin.site.register(Options, OptionsAdmin)

