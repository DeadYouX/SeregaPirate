from email.policy import default
from django.db import models

class News(models.Model):
    title = models.CharField("Название", max_length=100)
    desc = models.CharField("Описание", max_length=200)
    text = models.TextField("Текст новости", max_length=1000)
    photo = models.ImageField("Фотография", upload_to='news/static/news/', blank=True, default='None')
    date = models.DateField("Дата создания")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Новость"
        verbose_name_plural="Новости"