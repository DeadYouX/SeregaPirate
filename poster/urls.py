from django.urls import path
from . import views

urlpatterns = [
    path('', views.poster, name="poster"),
    path('<int:page_id>/', views.poster_by_id, name='posterbyid'),
    path('<int:page_id>/code/', views.poster_code, name='postercode'),
    path('<int:page_id>/done/', views.poster_done, name='posterdone'),
]