from operator import ne
from django.shortcuts import render
from .models import News
def news(request):
    queryset = News.objects.order_by('-id')
    data = {
        "title": 'Альбомы',
        'showprofile': True,
        'now': 'news',
        'news': [[obj.id, obj.title, obj.desc, obj.text, str(obj.photo.url).replace('/news/static/', ''), obj.date] for obj in queryset],
    }

    return render(request, 'news/news.html', data)

def news_by_id(request, page_id):
    queryset = News.objects.filter(id=page_id)
    before_id, next_id = 0, 0
    ids = [obj['id'] for obj in News.objects.values('id')]
    for i in range(len(ids)):
        if ids[i] == page_id:
            if i==0:
                before_id = ids[len(ids)-1]
            else:
                before_id = ids[i-1]
            if i==len(ids)-1:
                next_id = ids[0]
            else:
                next_id = ids[i+1]
    data = {
        'id': page_id,
        'ids': ids,
        'next_id': next_id,
        'before_id': before_id,
        "title": 'Альбомы',
        'now': 'news',
        'showprofile': True,
        'news': [[obj.id, obj.title, obj.desc, obj.text, str(obj.photo.url).replace('/news/static/', ''), obj.date] for obj in queryset],
    }
    return render(request, 'news/newsbyid.html', data)