# Generated by Django 5.0.2 on 2024-04-28 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ForumProfile', '0004_alter_profile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('photo', models.ImageField(upload_to='merch/static/merch/', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена')),
                ('currency', models.CharField(choices=[('₽', 'RUB'), ('€', 'EUR'), ('$', 'USD')], max_length=3, verbose_name='Валюта')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('now', models.BooleanField(default=True, verbose_name='Текущая')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='ForumProfile.profile')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=2, verbose_name='Размер')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='merch.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merch.product')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
    ]
