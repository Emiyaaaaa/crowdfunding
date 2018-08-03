from django.db import models
from DjangoUeditor.models import UEditorField
# import uuid
# Create your models here.
# @author:Ori

class News(models.Model):
    is_publish = models.CharField(choices=(('publish', '发布'), ('manuscript', '草稿')), verbose_name='新闻状态',
                                  default='manuscript', max_length=10)
    title = models.CharField(max_length=128,verbose_name='新闻标题')
    image = models.ImageField(upload_to='title_images', verbose_name='新闻标题图片')
    source_from = models.CharField(max_length=32,verbose_name='新闻来源')
    general_situation = models.TextField(verbose_name='新闻概况')
    text = UEditorField('新闻内容',width=1200,height=600, toolbars='full', imagePath='text_images/', filePath='text_files/',
                        upload_settings={'imageMaxSize': 1204000,
                            'videoPathFormat': "text_video/%(basename)s_%(datetime)s.%(extname)s",
                                         'scrawlPathFormat':"text_scrawl/%(basename)s_%(datetime)s.%(extname)s"})
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    update_at = models.DateTimeField(auto_now=True,verbose_name='最后修改时间')

    def __unicode__(self):
        return "<题目%s>" % (self.title)

    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = verbose_name

class Satis(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True,verbose_name='最后修改时间')
    class Meta:
        verbose_name = u'被赞：喜欢'
        verbose_name_plural = verbose_name

class Notverysatid(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True,verbose_name='最后修改时间')
    class Meta:
        verbose_name = u'被赞：一般'
        verbose_name_plural = verbose_name

class Nosatis(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True,verbose_name='最后修改时间')
    class Meta:
        verbose_name = u'被赞：不喜欢'
        verbose_name_plural = verbose_name