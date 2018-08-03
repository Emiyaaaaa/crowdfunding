#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xadmin
# from .models import VerifyRecord,Banner
from xadmin.plugins.auth import UserAdmin
from xadmin import views
from crispy_forms.layout import Fieldset
from xadmin.layout import Main, Row, Side
from django.utils.translation import ugettext as _
from .models import UserMessage

#以下代码为后台管理系统的主题，logo配置代码

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True
xadmin.site.register(views.BaseAdminView,BaseSetting)


class GlobalSettings(object):
    site_title='童心圆后台管理系统'
    site_footer='童心圆'
    menu_style='accordion'


class VerifyRecordAdmin(object):
    list_display = ['code', 'email_or_mobile', 'send_type', 'send_time']      #显示列表
    search_fields = ['code', 'email_or_mobile', 'send_type']      #搜索
    list_filter = ['code', 'email_or_mobile', 'send_type', 'send_time']



class UserMessageAdmin(object):
    pass


xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.unregister(UserMessage)
xadmin.site.register(UserMessage,UserMessageAdmin)
