from django.shortcuts import render
from .models import Albums

def albums(request):
    queryset = Albums.objects.order_by('-date')
    data = {
        "title": 'Альбомы',
        'showprofile': True,
        'now': 'albums',
        'albums': [[obj.id, obj.title, str(obj.photo.url).replace('/albums/static/', ''), obj.date, obj.link] for obj in queryset],
        'dates': set(obj.date for obj in queryset),
    }

    return render(request, 'albums/albums.html', data)


def album_by_id(request, page_id):
    queryset = Albums.objects.filter(id=page_id)
    before_id, next_id = 0, 0
    ids = [obj['id'] for obj in Albums.objects.values('id')]
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
        'now': 'albums',
        'showprofile': True,
        'albums': [[obj.id, obj.title, str(obj.photo.url).replace('/albums/static/', ''), obj.date, obj.link] for obj in queryset],
        'dates': set(obj.date for obj in queryset),
        }
    return render(request, 'albums/albumsbyid.html', data)