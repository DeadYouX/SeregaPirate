from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='ForumProfile/static/ForumProfile/', default='ForumProfile/static/ForumProfile/avatar.jpg', blank=True, null=True)
    purchase_count = models.IntegerField(default=0)
    message_count = models.IntegerField(default=0)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name="Профиль"
        verbose_name_plural="Профили"