from datetime import datetime

from django.db import models

from promotions.models import VIP
from psytests.models import MentalEvaluation
from users.models import UserProfile


class UserEvaluation(models.Model):
    # mentalEvaluation = models.ManyToManyField(MentalEvaluation, verbose_name=u"用户测评")
    eval_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户ID")
    eval = models.ForeignKey(MentalEvaluation, on_delete=models.CASCADE, verbose_name=u"测评ID")
    eval_score = models.IntegerField(verbose_name=u"测评得分")
    # user_count = models.IntegerField()
    # eval_result = models.CharField(max_length=100)
    created_on = models.DateTimeField(max_length=200, default=datetime.now, verbose_name=u"评价日期")
    payment_status = models.CharField(max_length=20,
                                      choices=(("paid", u"已付款"), ("not paid", u"未付款")),
                                      default="paid")

    class Meta:
        verbose_name = u"用户测评信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户测评信息"


class UserReviewForEvaluation(models.Model):
    # user - user_review many to many relationship
    review_eval = models.ForeignKey(MentalEvaluation, on_delete=models.CASCADE, verbose_name=u"测评")
    review_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"评价用户")
    review = models.TextField(max_length=3000, verbose_name=u"用户评价")
    created_on = models.DateTimeField(default=datetime.now, verbose_name=u"评价日期")

    class Meta:
        verbose_name = u"用户评价"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户评价"


class PopUp(models.Model):
    target_user = models.ManyToManyField(UserProfile, verbose_name=u"弹窗用户")
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="popup/%Y/%m", max_length=100, verbose_name=u"弹窗")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    status = models.IntegerField(choices=((0, "off"), (1, "on")), default=0, verbose_name=u"状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u'弹窗'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title + "弹窗"


class UserPay(models.Model):
    payment_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户付款")
    amount = models.IntegerField(verbose_name=u"付款金额")
    payment_type = models.CharField(choices=(("pay_test", u"测评购买"), ("new_vip", u"会员购买"), ("renew_vip", u"会员续费")),
                                    max_length=30, verbose_name=u"付费类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"购买时间")

    class Meta:
        verbose_name = u'付款信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.payment_user.username
