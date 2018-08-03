# _*_ coding: utf-8 _*_
__author__ = 'zy'
__date__ = '2018/8/1 9:45'

import xadmin
from xadmin import views
from donate.models import *




class BaseSetting():
    enable_themes = True
    use_bootswatch = True



class projectadmin(object):
    list_display = ['user_name','proj_class','project_id','name','introduce','action','befor_image','later_image','target_money',
                    'now_money','people_num','see_num','time_begin','time_out','state','created_at','update_at','is_display','is_delete']
    search_fields = ['user_name','proj_class','project_id','name','is_display','is_delete']
    list_filter = ['user_name','proj_class','project_id','name','is_display','is_delete','target_money']
    style_fields = {'introduce':'ueditor'}

class prj_developmentadmin():
    list_display = ['prj_development_id','name','title','introduce','image','year','date','created_at','update_at']
    search_fields = ['prj_development_id','name','title','date']
    list_filter = ['prj_development_id','name','title','created_at','update_at']

class Donation_logadmin():
    list_display = ['Donation_log_id','Donation_name','project','donate_money','donate_at','created_at','update_at']
    search_fields = ['Donation_log_id','Donation_name','project','donate_at','created_at']
    list_filter = ['Donation_log_id','Donation_name','project','donate_at','created_at']


xadmin.site.register(project,projectadmin)
xadmin.site.register(prj_development,prj_developmentadmin)
xadmin.site.register(Donation_log,Donation_logadmin)
# xadmin.site.unregister(views.BaseAdminView)
# xadmin.site.unregister(views.CommAdminView)
# xadmin.site.register(views.BaseAdminView,BaseSetting)
# xadmin.site.register(views.CommAdminView,GlobalSetting)


