from django.shortcuts import render
from .models import Photos

def photos(request):
    data = {
        "title": 'Фото',
        'showprofile': True,
        'now': 'photos',
        "photos": Photos.objects.all(),
    }
    return render(request, 'photos/photos.html', data)