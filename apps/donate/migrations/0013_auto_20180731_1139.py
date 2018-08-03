# Generated by Django 2.0.3 on 2018-07-31 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donate', '0012_auto_20180731_1128'),
    ]

    operations = [

        migrations.AddField(
            model_name='project',
            name='is_display',
            field=models.IntegerField(choices=[(0, '展示在首页'), (1, '不展示')], default=1, verbose_name='是否展示'),
        ),


    ]