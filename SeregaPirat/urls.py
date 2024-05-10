from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from ForumProfile import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('photos/', include('photos.urls')),
    path('albums/', include('albums.urls')),
    path('news/', include('news.urls')),
    path('poster/', include('poster.urls')),
    path('profile/', include('ForumProfile.urls')),
    path('forum/', include('forum.urls')),
    path('merch/', include('merch.urls')),
    path('accounts/password_change/done/', views.password_change_done),
    path('accounts/password_change/', views.settings),
    path('accounts/login/', views.login),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
