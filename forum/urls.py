from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name="forum"),
    path('<int:page_id>/', views.forum_by_id, name='forumbyid'),
]