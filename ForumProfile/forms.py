from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class SignUpForm(UserCreationForm):
    avatar = models.ImageField(upload_to='ForumProfile/static/profile/', default='ForumProfile/static/profile/avatar.jpg', blank=True, null=True)
    purchase_count = models.IntegerField(default=0)
    message_count = models.IntegerField(default=0)
    registration_date = models.DateTimeField(default=timezone.now)

    class Meta:
        model = User
        fields = ['username', 'avatar', 'purchase_count', 'message_count', 'email', 'password1', 'password2', 'registration_date']


from .models import Profile

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']