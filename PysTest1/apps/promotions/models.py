from datetime import datetime, timedelta

from django.db import models

from users.models import UserProfile


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", max_length=100, verbose_name=u"轮播图")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class VIP(models.Model):
    VIP_type = models.CharField(choices=(('normal', u"普通会员"), ('advanced', u"高级会员")),
                                default="normal", max_length=100, verbose_name=u"会员类型")
    price = models.IntegerField(verbose_name=u"价格")
    valid_date = models.DateTimeField(verbose_name=u"有效期", default=datetime.now() + timedelta(days=30))

    class Meta:
        verbose_name = u'会员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.VIP_type


class Coupon(models.Model):
    coupon_name = models.CharField(max_length=100, verbose_name=u"优惠券")
    coupon_type = models.CharField(choices=(("default", u"默认", ), ("holiday", u"节日"), ("others", u"其他")),
                                   default="default", max_length=20, verbose_name=u"优惠券类型")
    use_condition = models.IntegerField(default=10, verbose_name=u"使用条件")
    available_date = models.DateField(default=datetime.now, verbose_name=u"有效期")
    get_type = models.CharField(choices=(("push", u"推送"), ("pull", u"领取")),
                                default="push", max_length=20, verbose_name=u"获得方式")
    get_condition = models.CharField(choices=(("new_user", u"新用户"), ("non_vip", u"非会员"), ("vip", u"会员")),
                                     default="non_vip", max_length=20, verbose_name=u"获得条件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    valid_date = models.DateField(verbose_name=u"可领取时间")

    class Meta:
        verbose_name = u'优惠券'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.coupon_name
