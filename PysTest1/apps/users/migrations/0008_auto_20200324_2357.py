# Generated by Django 2.0 on 2020-03-24 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200323_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='nick_name',
            new_name='nickname',
        ),
    ]
