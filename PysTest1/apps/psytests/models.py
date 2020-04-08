# -*- encoding: utf-8 -*-
from datetime import datetime

from django.db import models

from multiselectfield import MultiSelectField
import sys
import importlib

from users.models import UserProfile

importlib.reload(sys)
if sys.getdefaultencoding() != "utf-8":
    importlib.reload(sys)
    sys.setdefaultencoding("utf-8")



class EvalQuestion(models.Model):
    #eval = models.ForeignKey(MentalEvaluation, on_delete=models.CASCADE, verbose_name=u"对应测评")
    q_id = models.IntegerField(auto_created=True, verbose_name=u"问题id")
    q_desc = models.CharField(max_length=3000, verbose_name=u"问题描述")
    reverse_scoring = models.BooleanField(default=False, choices=((False, u"正向"), (True, u"反向")), verbose_name=u"反向计分")
    dimension = models.IntegerField(default=1, verbose_name=u"维度",
                                    choices=((1, u"一"), (2, u"二"), (3, u"三")))

    class Meta:
        ordering = ['q_id']
        verbose_name = u"测评问题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.q_desc[:10] + "..."



class Options(models.Model):
    o_id = models.IntegerField(auto_created=True, verbose_name=u"选项id")
    o_desc = models.CharField(max_length=3000, verbose_name=u"选项描述")
    question = models.ManyToManyField(EvalQuestion, verbose_name=u'对应问题')

    class Meta:
        #  ordering = ['o_id']
        verbose_name = u"选项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.o_desc

class MentalEvaluation(models.Model):
    eval_id = models.CharField(max_length=200, primary_key=True)
    eval_type = models.CharField(choices=(("type1", u"成长"),
                                          ("type2", u"情感"),
                                          ("type3", u"人际关系")), max_length=100)
    title = models.CharField(max_length=100, unique=True)
    intro = models.TextField()
    price = models.CharField(max_length=20)
    created_on = models.CharField(max_length=200)
    is_online = models.CharField(max_length=30, choices=(("online", u"在线"),
                                                         ("offline", u"离线"),
                                                         ("inprogress", u"完善中")))
    avatar = models.CharField(max_length=200)    #location of avatar in frontend
    nums_eval = models.IntegerField()    #user_count
    state = models.IntegerField()
    ques_num = models.IntegerField()
    report = models.IntegerField()
    reverse_scoring = models.BooleanField(default=False, choices=((False, u"正向"), (True, u"反向")),
                                          verbose_name=u"反向计分")
    eval_dimension = models.IntegerField(default=1, verbose_name=u"问题维度",
                                         choices=((1, u"一"), (2, u"二"), (3, u"三")))

    questions = models.ManyToManyField(Options, verbose_name=u"对应问题")

    class Meta:
        ordering = ['eval_id']
        verbose_name = u"心理测评"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title




class UserEvaluation(models.Model):
    #mentalEvaluation = models.ManyToManyField(MentalEvaluation)
    user_id = models.CharField(max_length=200, verbose_name=u"用户id")
    eval_id = models.CharField(max_length=200, verbose_name=u"测评id")
    eval_score = models.IntegerField(verbose_name=u"测评分数")
    user_count = models.IntegerField()
    eval_result = models.CharField(max_length=100, verbose_name=u"测评结果")
    created_on = models.CharField(max_length=200, verbose_name=u"添加时间")
    PAYMENT_SIZE = (
        ('paid', u"已付款"),
        ('not paid', u"未付款"),
    )
    payment_status = models.CharField(max_length=20, choices=PAYMENT_SIZE, verbose_name=u"付款状态")

    class Meta:
        verbose_name = u"用户测评信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户测评信息"


class UserReviewForEvaluation(models.Model):
    # user - user_review many to many relationship
    eval_id = models.CharField(max_length=200, verbose_name=u"测评id")
    user_id = models.CharField(max_length=200, verbose_name=u"用户id")
    review = models.TextField(verbose_name=u"评价")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户评价"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户评价"

class UserEvalQuestionInfo(models.Model):    #user choice on evals
    eval_id = models.ForeignKey(MentalEvaluation, on_delete=models.CASCADE, verbose_name=u"测评id")
    user_id = models.ForeignKey(UserEvaluation, max_length=200, on_delete=models.CASCADE, verbose_name=u"用户id")
    q_id = models.ForeignKey(EvalQuestion, auto_created=True, on_delete=models.CASCADE, verbose_name=u"问题id")
    o_id = models.ForeignKey(Options, auto_created=True, on_delete=models.CASCADE, verbose_name=u"选项id")   #o_id in Options table

    class Meta:
        ordering = ['user_id']
        verbose_name = u"用户id"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户测评选项"





