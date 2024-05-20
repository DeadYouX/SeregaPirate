from tabnanny import verbose
from django.db import models

class Photos(models.Model):
    # Поле id создается автоматически, как первичный ключ

    # Поле для хранения фотографии
    photo = models.ImageField("Фотография", upload_to='photos/static/photos/')

    def __str__(self):
        return '{}'.format(str(self.photo).replace('photos/static/', ''))

    class Meta:
        verbose_name="Фотография"
        verbose_name_plural="Фотографии"