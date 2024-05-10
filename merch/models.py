from django.db import models
from ForumProfile.models import Profile

class Product(models.Model):
    name = models.CharField("Название", max_length=100)
    color = models.CharField("Цвет", max_length=50)
    photo = models.ImageField("Фото", upload_to='merch/static/merch/')
    price = models.DecimalField("Цена", max_digits=10, decimal_places=0)
    
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]

    def get_size_choices(self):
        return [obj[0] for obj in self.SIZE_CHOICES]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"


class Cart(models.Model):
    user = models.ForeignKey(Profile, related_name='cart', on_delete=models.CASCADE)
    now = models.BooleanField("Текущая", default=True)
    last = models.BooleanField("Последняя", default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    adress = models.TextField("Адрес", max_length=300, default='', blank=True)

    def total_cost(self):
        return sum(item.total_price() for item in self.items.all())

    def total_quantity(self):
        return sum(item.quantity for item in self.items.all()) 

    def __str__(self):
        return f'{self.user}: {self.timestamp.date()}'

    class Meta:
        verbose_name="Корзина"
        verbose_name_plural="Корзины"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    size = models.CharField("Размер", max_length=3, choices=Product.SIZE_CHOICES)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product.name} ({self.quantity}шт.)'

    class Meta:
        verbose_name="Товар в корзине"
        verbose_name_plural="Товары в корзине"

