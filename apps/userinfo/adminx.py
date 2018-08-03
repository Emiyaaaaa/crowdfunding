#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xadmin
from .models import UserMessage

#以下代码为后台管理系统的主题，logo配置代码

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True


class GlobalSettings(object):
    site_title='童心圆后台管理系统'
    site_footer='童心圆'
    menu_style='accordion'


class UserMessageAdmin(object):
    pass


# xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.unregister(UserMessage)
xadmin.site.register(UserMessage,UserMessageAdmin)
