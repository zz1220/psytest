# Generated by Django 2.2 on 2020-02-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_auto_20200221_0512'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mentalevaluation',
            options={},
        ),
        migrations.AlterField(
            model_name='userevaluation',
            name='created_on',
            field=models.CharField(max_length=200),
        ),
    ]
