from . import views
from django.conf.urls import url,include
from django.urls import path

urlpatterns = [
    path(r'',views.news_catalog),
    url(r'(?P<id>\d+)$',views.news ,name='news')
]