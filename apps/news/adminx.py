import xadmin
from .models import News
class NewsAdmin(object):
    style_fields = {'text': 'ueditor'}
xadmin.site.register(News, NewsAdmin)