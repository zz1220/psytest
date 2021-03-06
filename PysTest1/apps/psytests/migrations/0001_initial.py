# Generated by Django 2.0 on 2020-04-08 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvalQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_id', models.IntegerField(auto_created=True, verbose_name='问题id')),
                ('q_desc', models.CharField(max_length=3000, verbose_name='问题描述')),
                ('reverse_scoring', models.BooleanField(choices=[(False, '正向'), (True, '反向')], default=False, verbose_name='反向计分')),
                ('dimension', models.IntegerField(choices=[(1, '一'), (2, '二'), (3, '三')], default=1, verbose_name='维度')),
            ],
            options={
                'verbose_name': '测评问题',
                'verbose_name_plural': '测评问题',
                'ordering': ['q_id'],
            },
        ),
        migrations.CreateModel(
            name='MentalEvaluation',
            fields=[
                ('eval_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('eval_type', models.CharField(choices=[('type1', '成长'), ('type2', '情感'), ('type3', '人际关系')], max_length=100)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('intro', models.TextField()),
                ('price', models.CharField(max_length=20)),
                ('created_on', models.CharField(max_length=200)),
                ('is_online', models.CharField(choices=[('online', '在线'), ('offline', '离线'), ('inprogress', '完善中')], max_length=30)),
                ('avatar', models.CharField(max_length=200)),
                ('nums_eval', models.IntegerField()),
                ('state', models.IntegerField()),
                ('ques_num', models.IntegerField()),
                ('report', models.IntegerField()),
                ('reverse_scoring', models.BooleanField(choices=[(False, '正向'), (True, '反向')], default=False, verbose_name='反向计分')),
                ('eval_dimension', models.IntegerField(choices=[(1, '一'), (2, '二'), (3, '三')], default=1, verbose_name='问题维度')),
            ],
            options={
                'verbose_name': '心理测评',
                'verbose_name_plural': '心理测评',
                'ordering': ['eval_id'],
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_id', models.IntegerField(auto_created=True, verbose_name='选项id')),
                ('o_desc', models.CharField(max_length=3000, verbose_name='选项描述')),
                ('question', models.ManyToManyField(to='psytests.EvalQuestion', verbose_name='对应问题')),
            ],
            options={
                'verbose_name': '选项',
                'verbose_name_plural': '选项',
            },
        ),
        migrations.CreateModel(
            name='UserEvalQuestionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eval_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psytests.MentalEvaluation', verbose_name='测评id')),
                ('o_id', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to='psytests.Options', verbose_name='选项id')),
                ('q_id', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to='psytests.EvalQuestion', verbose_name='问题id')),
            ],
            options={
                'verbose_name': '用户id',
                'verbose_name_plural': '用户id',
                'ordering': ['user_id'],
            },
        ),
        migrations.CreateModel(
            name='UserEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200, verbose_name='用户id')),
                ('eval_id', models.CharField(max_length=200, verbose_name='测评id')),
                ('eval_score', models.IntegerField(verbose_name='测评分数')),
                ('user_count', models.IntegerField()),
                ('eval_result', models.CharField(max_length=100, verbose_name='测评结果')),
                ('created_on', models.CharField(max_length=200, verbose_name='添加时间')),
                ('payment_status', models.CharField(choices=[('paid', '已付款'), ('not paid', '未付款')], max_length=20, verbose_name='付款状态')),
            ],
            options={
                'verbose_name': '用户测评信息',
                'verbose_name_plural': '用户测评信息',
            },
        ),
        migrations.CreateModel(
            name='UserReviewForEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eval_id', models.CharField(max_length=200, verbose_name='测评id')),
                ('user_id', models.CharField(max_length=200, verbose_name='用户id')),
                ('review', models.TextField(verbose_name='评价')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户评价',
                'verbose_name_plural': '用户评价',
            },
        ),
        migrations.AddField(
            model_name='userevalquestioninfo',
            name='user_id',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='psytests.UserEvaluation', verbose_name='用户id'),
        ),
        migrations.AddField(
            model_name='mentalevaluation',
            name='questions',
            field=models.ManyToManyField(to='psytests.Options', verbose_name='对应问题'),
        ),
    ]
