"""txy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf import settings
from userinfo.views import RegisterView,ModifyMessageView
from django.conf.urls.static import static
from django.views.static import serve
import xadmin
from django.contrib import admin
import django.views.static
# from django.urls import path
from django.conf.urls import url,include
from donate.views import CrowdFundingDisplay,Donate,Personal
from donate.views import PersonalCenter
import xadmin

from django.conf.urls import url
from donate import views
from django.views.generic import TemplateView

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('admin/', admin.site.urls),
    url('oncedonate/',Donate.as_view()),
    url('crowdfunding/',CrowdFundingDisplay.as_view(),name='crowdfunding'),
    # path('oncedonate/?project_id=(d+)&charset=utf-8&out_trade_no=(.*?)',donateLog.as_view())
    url('personal/',Personal.as_view()),
    #path
    #url(r'^xadmin/', xadmin.site.urls),
    # url('^crowdfunding', LoginView.as_view(),name='login'),
    # url('^login/$', LoginView.as_view(), name="login"),
    url('^regist/$', RegisterView.as_view(),name='regist'),
    # url(r'personalcenter',ModifyMessageView.as_view(),name='personalcenter'),

    url('personalcenter/',PersonalCenter.as_view(),name='personalcenter'),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'news/',include('news.urls'),name = 'news'),
    url(r'media/(?P<path>.*)$',django.views.static.serve, {'document_root': './media'})
]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
# urlpatterns += staticfiles_urlpatterns()