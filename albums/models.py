from email.policy import default
from django.db import models

class Albums(models.Model):
    title = models.CharField("Название", max_length=30)
    photo = models.ImageField("Фотография", upload_to='albums/static/albums/')
    link = models.CharField("Ссылка на альбом", max_length=200, blank=True)
    date = models.IntegerField("Год создания", default=2024)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Альбом"
        verbose_name_plural="Альбомы"