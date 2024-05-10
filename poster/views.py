from django.shortcuts import render
from .models import Poster
from django.contrib.auth.decorators import login_required


def poster(request):
    queryset = Poster.objects.order_by('id')
    data = {
        "title": 'Афиша',
        'showprofile': True,
        'now': 'poster',
        'poster': [[obj.id, obj.city, obj.address, obj.date] for obj in queryset],
        'city': set(obj.city for obj in queryset),
    }
    return render(request, 'poster/poster.html', data)

@login_required
def poster_by_id(request, page_id):
    queryset = Poster.objects.filter(id=page_id)
    data = {
        "title": 'Афиша',
        'id': page_id,
        'now': 'poster',
        'showprofile': True,
        'poster': [[obj.id, obj.city, obj.address, obj.date] for obj in queryset],
    }
    return render(request, 'poster/posterbyid.html', data)

@login_required
def poster_code(request, page_id):
    queryset = Poster.objects.filter(id=page_id)
    data = {
        'id': page_id,
        "title": 'Афиша',
        'now': 'poster',
        'showprofile': True,
        'poster': [[obj.id, obj.city, obj.address, obj.date] for obj in queryset],
    }
    return render(request, 'poster/postercode.html', data)

@login_required
def poster_done(request, page_id):
    queryset = Poster.objects.filter(id=page_id)
    data = {
        'id': page_id,
        "title": 'Афиша',
        'now': 'poster',
        'showprofile': True,
        'poster': [[obj.id, obj.city, obj.address, obj.date] for obj in queryset],
    }
    return render(request, 'poster/posterdone.html', data)