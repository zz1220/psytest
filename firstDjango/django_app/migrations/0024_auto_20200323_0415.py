# Generated by Django 2.2 on 2020-03-23 04:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0023_userevalquestioninfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreviewforevaluation',
            name='id',
            field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userreviewforevaluation',
            name='eval_id',
            field=models.CharField(max_length=200, verbose_name='测评id'),
        ),
    ]
