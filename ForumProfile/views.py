from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def auth(request):
    data = {
        "title": 'Вход',
        'showprofile': False,
    }
    return render(request, 'ForumProfile/auth.html', data)

def reg(request):
    all_errors = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/profile/')
        else:
            for field, errors in form.errors.items():
                err = ''
                for error in errors:
                    err += error + "\n"
                all_errors[field] = err
    else:
        form = UserCreationForm()
    data = {
        "title": 'Регистрация',
        'showprofile': False,
        'form': form,
        'errors': all_errors,
    }
    return render(request, 'ForumProfile/reg.html', data)

def regcode(request):
    data = {
        "title": 'Регистрация',
        'showprofile': False,
    }
    return render(request, 'ForumProfile/regcode.html', data)

def forgotpass(request):
    data = {
        "title": 'Восстановление пароля',
        'showprofile': False,
    }
    return render(request, 'ForumProfile/forgot.html', data)

def forgotcode(request):
    data = {
        "title": 'Восстановление пароля',
        'showprofile': False,
    }
    return render(request, 'ForumProfile/forgotcode.html', data)

def forgotnewpass(request):
    data = {
        "title": 'Восстановление пароля',
        'showprofile': False,
    }
    return render(request, 'ForumProfile/forgotnewpass.html', data)

from .models import Profile
@login_required
def profile(request):
    if request.user.is_authenticated:
        user = Profile.objects.get_or_create(user=request.user)[0]
        data = {
            "title": 'Профиль',
            'showprofile': False,
            'show_settings':True,
            'finded': True,
            'user_profile': {
                'username': user.user.username,
                'avatar': f'{str(user.avatar).replace('ForumProfile/static/', '')}',
                'email': request.user.email,
                'purchase_count': user.purchase_count,
                'message_count': user.message_count,
                'registration_date': user.registration_date.date(),
            },
        }
        return render(request, 'ForumProfile/profile.html', data)
    
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def settings(request):
    all_errors = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'save_option' in request.POST:
                save_option = request.POST['save_option']
                if save_option == 'password':
                    form = PasswordChangeForm(request.user, request.POST)
                    if form.is_valid():
                        user = form.save()
                        update_session_auth_hash(request, user)
                        return redirect('password_change_done')
                    else:
                        for field, errors in form.errors.items():
                            err = ''
                            for error in errors:
                                err += error + "\n"
                            all_errors[field] = err
                if save_option == 'avatar':
                    if request.FILES:
                        user = Profile.objects.get(user=request.user)
                        user.avatar = request.FILES['file_upload']
                        user.save()
                        update_session_auth_hash(request, user)
                        return redirect('avatar_done')
                    else:
                        return redirect('password_change')
        
        user = Profile.objects.get_or_create(user=request.user)[0]
        data = {
            "title": 'Профиль',
            'showprofile': False,
            'errors': all_errors,
            'user_profile': {
                'avatar': f'{str(user.avatar).replace('ForumProfile/static/', '')}',
                'email': request.user.email,
                'purchase_count': user.purchase_count,
                'message_count': user.message_count,
                'registration_date': user.registration_date.date(),
            },
        }
        return render(request, 'ForumProfile/profile-settings.html', data)

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
def login(request):
    all_errors = {}
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
        else:
            for field, errors in form.errors.items():
                err = ''
                for error in errors:
                    err += error + "\n"
                if field == "__all__":
                    field = 'all'
                all_errors[field] = err
    else:
        form = AuthenticationForm()
    data = {
            "title": 'Вход',
            'showprofile': False,
            'errors': all_errors,
        }
    return render(request, 'registration/login.html', data)

from django.shortcuts import redirect
@login_required
def password_change_done(request):
    if request.user.is_authenticated:
        return redirect('password-done')

@login_required 
def password_done(request):
    if request.user.is_authenticated:
        user = Profile.objects.get_or_create(user=request.user)[0]
        data = {
            "title": 'Профиль',
            'showprofile': False,
            'success': "Ваш пароль был успешно изменён.",
            'user_profile': {
                'avatar': f'{str(user.avatar).replace('ForumProfile/static/', '')}',
                'email': request.user.email,
                'purchase_count': user.purchase_count,
                'message_count': user.message_count,
                'registration_date': user.registration_date.date(),
            },
        }
        return render(request, 'ForumProfile/profile-done.html', data)

@login_required   
def avatar_done(request):
    if request.user.is_authenticated:
        user = Profile.objects.get_or_create(user=request.user)[0]
        data = {
            "title": 'Профиль',
            'showprofile': False,
            'success': "Ваше фото был успешно изменено.",
            'user_profile': {
                'avatar': f'{str(user.avatar).replace('ForumProfile/static/', '')}',
                'email': request.user.email,
                'purchase_count': user.purchase_count,
                'message_count': user.message_count,
                'registration_date': user.registration_date.date(),
            },
        }
        return render(request, 'ForumProfile/profile-done.html', data)
    

def profile_by_nick(request, nickname):
    try:
        user = Profile.objects.get(user__username=nickname)
        data = {
            "title": 'Профиль',
            'showprofile': False,
            'show_settings':False,
            'finded': True,
            'user_profile': {
                'username': user.user.username,
                'avatar': f'{str(user.avatar).replace('ForumProfile/static/', '')}',
                'email': user.user.email,
                'purchase_count': user.purchase_count,
                'message_count': user.message_count,
                'registration_date': user.registration_date.date(),
            },
        }
        return render(request, 'ForumProfile/profile.html', data)
    except:
        data = {
            "title": 'Профиль',
            'showprofile': False,
            'show_settings':False,
            'finded': False,
        }
        return render(request, 'ForumProfile/profile.html', data)
    