from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('user/<str:nickname>/', views.profile_by_nick, name="profile_by_nick"),
    path('registration/', views.reg, name="reg"),
    path('reset/', views.forgotpass, name="forgot"),
    path('reset/code/', views.forgotcode, name="forgotcode"),
    path('reset/newpassword/', views.forgotnewpass, name="forgotnewpass"),
    path('password_change/done/', views.password_done, name="password-done"),
    path('avatar_change/done/', views.avatar_done, name="avatar_done")
]