from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bio/', views.bio, name='bio'),
    path('contacts/', views.contacts, name='contacts'),
    path('privacy-policy/', views.policy, name='policy'),
    path('conditions/', views.conditions, name='conditions'),
]
