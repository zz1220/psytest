# Generated by Django 2.2 on 2020-03-22 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0022_delete_userevalquestioninfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvalQuestionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eval_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.MentalEvaluation', verbose_name='测评id')),
                ('o_id', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to='django_app.Options', verbose_name='选项id')),
                ('q_id', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to='django_app.EvalQuestion', verbose_name='问题id')),
                ('user_id', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='django_app.UserEvaluation', verbose_name='用户id')),
            ],
            options={
                'verbose_name_plural': '用户id',
                'verbose_name': '用户id',
                'ordering': ['user_id'],
            },
        ),
    ]
