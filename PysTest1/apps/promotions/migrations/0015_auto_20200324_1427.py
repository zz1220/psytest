# Generated by Django 2.0 on 2020-03-24 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0014_auto_20200324_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip',
            name='valid_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 14, 27, 44, 738389), verbose_name='有效期'),
        ),
    ]
