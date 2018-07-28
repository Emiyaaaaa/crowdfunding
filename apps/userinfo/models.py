from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser  # 继承原有字段
# Create your models here.

class UserMessage(AbstractUser):
    user_id = models.IntegerField(max_length=20, verbose_name=u'用户id',primary_key=True, db_column='FId')
    user_name = models.CharField(max_length=30, verbose_name=u'用户名',null=False)
    user_password = models.CharField(max_length=14, verbose_name=u'密码',null=False)
    user_realname = models.CharField(max_length=12, verbose_name=u'真实姓名',null=False)
    user_nickname = models.CharField(max_length=10, verbose_name=u'昵称', null=True)
    user_email = models.CharField(max_length=30, verbose_name=u'邮箱', null=False)
    user_id_card_number = models.CharField(max_length=15 ,verbose_name=u'身份证号', null=False)
    user_mobile = models.CharField(max_length=11, verbose_name= u'联系电话',null=False)
    user_qq = models.CharField(max_length=12, verbose_name= u'联系QQ',null=False)
    user_home_address = models.CharField(max_length=100, verbose_name=u"家庭住址", null=False)
    user_company_name = models.CharField(max_length=100, verbose_name=u"单位名称", null=False)
    user_gender = models.CharField(max_length=10, choices=(("male", u'男'), ("female", u'女')), default='male')
    user_hand_portrait = models.ImageField(max_length=100,verbose_name=u'头像',upload_to='image/%Y/%m', default=u"image/default.png", null=True)
    user_signature = models.CharField(default='', verbose_name=u'个性签名', max_length=80, null=True)
    created_at = models.IntegerField(max_length=20, verbose_name=u'创建时间',null=False)
    update_at = models.IntegerField(max_length=20, verbose_name=u'更新时间',null=False,default=datetime.now)
