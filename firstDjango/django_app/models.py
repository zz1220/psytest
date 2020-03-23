# encoding=utf-8
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
import sys
import importlib
importlib.reload(sys)
if sys.getdefaultencoding() != "utf-8":
    importlib.reload(sys)
    sys.setdefaultencoding("utf-8")


IS_ONLINE = (
    ("online", "在线"),
    ("offline", "离线"),
    ("inprogress", "完善中")
)

EVAL_TYPE_CHOICE = (
    ("1", u"成长"),
    ("2", u"情感"),
    ("3", u"人际关系")
    )

class MentalEvaluation(models.Model):
    eval_id = models.CharField(max_length=200, primary_key=True, verbose_name=u"测评id")
    eval_type = MultiSelectField(choices=EVAL_TYPE_CHOICE, verbose_name=u"测评类型")
    title = models.CharField(max_length=100, unique=True, verbose_name=u"标题")
    intro = models.TextField(verbose_name=u"一句话简介")
    price = models.FloatField(max_length=20, verbose_name=u"价格")
    discount_price = models.FloatField(max_length=20, verbose_name=u"折扣价格")
    created_on = models.CharField(max_length=200, verbose_name=u"添加时间")
    is_online = models.CharField(max_length=30, choices=IS_ONLINE, verbose_name=u"")
    avatar = models.CharField(max_length=200, verbose_name=u"轮播图")    #location of avatar in frontend
    nums_eval = models.IntegerField(verbose_name=u"测评次数")    #user_count
    state = models.IntegerField(verbose_name=u"测评状态")
    ques_num = models.IntegerField(verbose_name=u"题目数量")

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
    #user_count = models.IntegerField()
    eval_result = models.CharField(max_length=100, verbose_name=u"测评结果")
    created_on = models.CharField(max_length=200, verbose_name=u"添加时间")
    PAYMENT_SIZE = (
        ('paid', u""),
        ('not paid', u""),
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

class EvalQuestion(models.Model):
    eval_id = models.ForeignKey(MentalEvaluation, on_delete=models.CASCADE, verbose_name=u"对应测评")
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
    question = models.ManyToManyField(EvalQuestion, verbose_name=u"对应问题")

    class Meta:
        ordering = ['o_id']
        verbose_name = u"选项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.o_desc[:10] + "..."

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




# Create your models here.
