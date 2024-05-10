from django.db import models

class Poster(models.Model):
    city = models.CharField("Город", max_length=50)
    address = models.CharField("Адрес", max_length=100, blank=True)
    date = models.DateField("Дата проведения")
    
    def __str__(self):
        return self.city

    class Meta:
        verbose_name="Концерт"
        verbose_name_plural="Концерты"