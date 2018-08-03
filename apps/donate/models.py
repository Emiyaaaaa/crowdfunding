from django.db import models
from userinfo.models import UserMessage
from DjangoUeditor.models import UEditorField
# Create your models here.


class project(models.Model):
    '''
    众筹项目
    '''
    user_name = models.ForeignKey(UserMessage,default=None,on_delete=models.CASCADE,verbose_name='发起人用户名')
    proj_class = models.CharField(max_length=50,verbose_name="项目类别")
    project_id = models.AutoField(verbose_name="项目id",primary_key=True)
    name = models.CharField(max_length=30,verbose_name="项目名称")
    introduce = UEditorField('项目简介',width=1200,height=600, toolbars='full', imagePath='text_images/', filePath='text_files/',
                        upload_settings={'imageMaxSize': 1204000,
                            'videoPathFormat': "text_video/%(basename)s_%(datetime)s.%(extname)s",
                                         'scrawlPathFormat':"text_scrawl/%(basename)s_%(datetime)s.%(extname)s"})
    action = models.TextField(verbose_name="具体行动")
    befor_image = models.ImageField(upload_to='img',verbose_name='首页项目图片')
    later_image = models.ImageField(upload_to='img', verbose_name='进入后项目图片')
    target_money = models.FloatField(verbose_name='目标金额')
    now_money = models.FloatField(verbose_name='已筹金额')
    people_num = models.IntegerField(verbose_name='帮助人数')
    see_num = models.IntegerField(verbose_name="浏览人数")
    time_begin = models.DateField(verbose_name="开始时间")
    time_out = models.DateField(verbose_name="结束时间")
    state = models.IntegerField(choices=((0,'审核中'),(1,'通过'),(2,'未通过')),verbose_name='状态')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True,verbose_name='最后修改时间')
    is_display = models.IntegerField(choices=((0,'展示在首页'),(1,'不展示')),default=1,verbose_name='是否展示')
    is_delete = models.IntegerField(choices=((0,'已删除'),(1,'未删除')),default=1)

    class Meta:
        verbose_name = '众筹项目'
    def __str__(self):
        return self.name


class prj_development(models.Model):
    """
    项目进程信息
    """
    prj_development_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(project,on_delete=models.CASCADE,verbose_name="项目名称")
    title = models.CharField(max_length=40,verbose_name='进程题目')
    introduce = models.TextField(verbose_name='进程简介')
    image = models.ImageField(upload_to='img',max_length=1024,verbose_name="图片")
    year = models.CharField(max_length=10,verbose_name='进程发生年份')
    date = models.CharField(max_length=30,verbose_name="进程发生月日")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')

    class Meta:
        verbose_name = '众筹项目进程'

    def __str__(self):
        return self.title

class Donation_log(models.Model):
    Donation_log_id = models.AutoField(primary_key=True,verbose_name='流水id')
    Donation_name = models.ForeignKey(UserMessage,default=None,on_delete=models.CASCADE,verbose_name='捐助人姓名')
    project = models.ForeignKey(project,default=None,on_delete=models.CASCADE,verbose_name='捐助项目名称')
    donate_money = models.FloatField(verbose_name='捐助金额')
    donate_at = models.DateTimeField(auto_now_add=True, verbose_name='捐助时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')

    class Meta:
        verbose_name = '捐助流水'

    def __str__(self):
        return str(self.Donation_log_id)









