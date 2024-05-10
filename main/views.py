from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        "title": 'Главная страница',
        'showprofile': False,
    }
    return render(request, 'main/index.html', data)

def bio(request):
    data = {
        "title": 'Биография',
        'showprofile': True,
        'now': 'bio',
    }
    return render(request, 'main/bio.html', data)

def contacts(request):
    data = {
        "title": 'Контакты',
        'showprofile': True,
        'now': 'contacts',
    }
    return render(request, 'main/contacts.html', data)

def policy(request):
    data = {
        "title": 'Политика конфиденциальности',
        'showprofile': False,
        'now': 'policy',
    }
    return render(request, 'main/privacy-policy.html', data)

def conditions(request):
    data = {
        "title": 'Условия и положения',
        'showprofile': False,
        'now': 'conditions',
    }
    return render(request, 'main/conditions.html', data)