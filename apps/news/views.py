from django.shortcuts import render
from .models import *
import time
from donate.views import CrowdFundingDisplay
from userinfo.models import UserMessage

# Create your views here.

# def index(request):
#     publish_news = News.objects.filter(is_publish__icontains='publish')
#     step = 0
#     content = []
#     for news in publish_news:
#         content.append(news)
#         step += 1
#         if step >= 6:
#             break
#
#     for i in content:
#         timeArray = time.strptime(str(i.update_at).split('.')[0], "%Y-%m-%d %H:%M:%S")
#         timeStamp = int(time.mktime(timeArray))
#         i.update_at = timeStamp
#         i.image = '/media/' + str(i.image)
#
#     for i in range(0,len(content)):
#         for j in range(i+1,len(content)):
#             if content[i].created_at <= content[j].created_at:
#                 content[i], content[j] = content[j], content[i]
#
#     return render(request,'crowdfunding.html',{'news':content})

# @csrf_exempt
def news(request,id):
    if request.is_ajax():
        state = request.POST.get('state')
        if state == 'satis':
            Satis.objects.create(news=News.objects.filter(id = id).first())
        if state == 'notverysatid':
            Notverysatid.objects.create(news=News.objects.filter(id = id).first())
        if state == 'nosatis':
            Nosatis.objects.create(news=News.objects.filter(id = id).first())

    publish_news = News.objects.filter(is_publish__icontains='publish')
    try:
        step = 0
        for news in publish_news:
            if str(news.id) == id:
                if step-1 < 0:
                    front_path = ''
                    front_title = ''
                else:
                    front = publish_news[step - 1]
                    front_path = str(front.id)
                    front_title = str(front.title)
                if step+1 >= len(publish_news):
                    next_path = ''
                    next_title = ''
                else:
                    next = publish_news[step+1]
                    next_path = str(next.id)
                    next_title = str(next.title)
                try:
                    username = request.session["username"]
                    return render(request, 'new_catalog.html', {
                                                                'username': username,
                                                                'news_text': news.text,
                                                                'news_title': news.title,
                                                                'news_date': news.update_at,
                                                                'news_source_from': news.source_from,
                                                                'front_news_path': front_path,
                                                                'next_news_path': next_path,
                                                                'front_news_title': front_title,
                                                                'next_news_title': next_title
                                                                })
                except:
                    pass
                return render(request,'news.html',{'news_text':news.text,'news_title':news.title,'news_date':news.update_at,'news_source_from':news.source_from,
                                                  'front_news_path':front_path,'next_news_path':next_path,
                                                   'front_news_title':front_title,'next_news_title':next_title
                                                   })
            else:
                step += 1
                continue
        return news_catalog(request)
    except:
        return CrowdFundingDisplay.get(request)

def news_catalog(request):
    publish_news = News.objects.filter(is_publish__icontains='publish')
    content = []
    for news in publish_news:
        content.append(news)

    for i in content:
        timeArray = time.strptime(str(i.update_at).split('.')[0], "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        i.update_at = timeStamp
        i.image = '/media/' + str(i.image)

    for i in range(0, len(content)):
        for j in range(i + 1, len(content)):
            if content[i].update_at <= content[j].update_at:
                content[i], content[j] = content[j], content[i]
    try:
        username = request.session["username"]
        user_hand_portrait = UserMessage.objects.get(username=username).user_hand_portrait
        return render(request, 'new_catalog.html', {'news':content,
                                                    'username': username,
                                                    'user_hand_portrait': user_hand_portrait})
    except:
        pass

    return render(request,'new_catalog.html',{'news':content})