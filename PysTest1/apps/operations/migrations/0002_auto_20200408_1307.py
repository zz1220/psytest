# Generated by Django 2.0 on 2020-04-08 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('psytests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreviewforevaluation',
            name='review_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评价用户'),
        ),
        migrations.AddField(
            model_name='userpay',
            name='payment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户付款'),
        ),
        migrations.AddField(
            model_name='userevaluation',
            name='eval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psytests.MentalEvaluation', verbose_name='测评ID'),
        ),
        migrations.AddField(
            model_name='userevaluation',
            name='eval_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户ID'),
        ),
        migrations.AddField(
            model_name='popup',
            name='target_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='弹窗用户'),
        ),
    ]
