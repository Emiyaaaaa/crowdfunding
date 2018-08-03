# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-08-02 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_remove_usermessage_user_nickname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VerifyRecord',
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='user_hand_portrait',
            field=models.ImageField(default='user_hand_portrait/default.png', null=True, upload_to='user_hand_portrait/%Y/%m', verbose_name='头像'),
        ),
    ]