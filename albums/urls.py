from django.urls import path
from . import views

urlpatterns = [
    path('', views.albums, name="albums"),
    path('<int:page_id>/', views.album_by_id, name='albumbyid'),
]