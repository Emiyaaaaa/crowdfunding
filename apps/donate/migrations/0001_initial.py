# Generated by Django 2.0.3 on 2018-07-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prj_development',
            fields=[
                ('prj_development_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40, verbose_name='进程题目')),
                ('introduce', models.TextField(verbose_name='进程简介')),
                ('image', models.CharField(max_length=1024, verbose_name='图片')),
                ('time', models.DateTimeField(verbose_name='进程发生时间')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('proj_class', models.CharField(max_length=20, verbose_name='项目类别')),
                ('project_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='项目id')),
                ('name', models.CharField(max_length=30, verbose_name='项目名称')),
                ('introduce', models.TextField(verbose_name='项目简介')),
                ('action', models.TextField(verbose_name='具体行动')),
                ('befor_image', models.CharField(max_length=1024, verbose_name='首页项目图片')),
                ('later_image', models.CharField(max_length=1024, verbose_name='进入后项目图片')),
                ('target_money', models.IntegerField(verbose_name='目标金额')),
                ('now_money', models.IntegerField(verbose_name='已筹金额')),
                ('people_num', models.IntegerField(verbose_name='帮助人数')),
                ('see_num', models.IntegerField(verbose_name='浏览人数')),
                ('time_begin', models.DateTimeField(verbose_name='开始时间')),
                ('time_out', models.DateTimeField(verbose_name='结束时间')),
                ('state', models.IntegerField(choices=[('审核中', 0), ('通过', 1), ('未通过', 2)], verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
        ),
        migrations.AddField(
            model_name='prj_development',
            name='name',
            field=models.ForeignKey(on_delete='CASCADE', to='donate.project', verbose_name='项目名称'),
        ),
    ]