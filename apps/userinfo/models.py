from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser  # 继承原有字段
# Create your models here.

class UserMessage(AbstractUser):
    id = models.AutoField(verbose_name=u'用户id',primary_key=True)
    user_realname = models.CharField(max_length=12, verbose_name=u'真实姓名',null=False)
    user_email = models.CharField(max_length=30, verbose_name=u'邮箱', null=False)
    user_id_card_number = models.CharField(max_length=19 ,verbose_name=u'身份证号', null=False)
    user_mobile = models.CharField(max_length=11, verbose_name= u'联系电话',null=False)
    user_qq = models.CharField(max_length=12, verbose_name= u'联系QQ',null=False)
    user_home_address = models.CharField(max_length=100, verbose_name=u"家庭住址", null=False)
    user_company_name = models.CharField(max_length=100, verbose_name=u"单位名称", null=False)
    user_gender = models.CharField(max_length=10, choices=(("male", u'男'), ("female", u'女')), default='male')
    user_hand_portrait = models.ImageField(max_length=100,verbose_name=u'头像',upload_to='user_hand_portrait/%Y/%m', default=u"user_hand_portrait/default.png", null=True)
    user_signature = models.CharField(default='', verbose_name=u'个性签名', max_length=80, null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间',null=False)
    update_at = models.DateTimeField(auto_now= True,verbose_name=u'更新时间',null=False)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

#
#
# class VerifyRecord(models.Model):  # 验证码
#     code = models.CharField(max_length=20, verbose_name='验证码')
#     email_or_mobile = models.CharField(max_length=50, verbose_name='邮箱或手机', default=0)
#     send_type = models.CharField(verbose_name='验证码类型', choices=(
#         ("mobileregister", '手机注册'), ("emailregister", '邮箱注册'), ("mobileforget", '手机找回密码'), ('emailforget', '邮箱找回密码')),
#                                  max_length=20)
#     send_time = models.DateTimeField(verbose_name='发送时间', default=datetime.now)  # now() 程序编译时间 now class实例化时间
#
#     class Meta:
#         verbose_name = '验证码'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return '{0}({1})'.format(self.code, self.email_or_mobile)
