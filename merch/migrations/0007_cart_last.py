# Generated by Django 5.0.2 on 2024-05-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0006_cart_adress_alter_cartitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='last',
            field=models.BooleanField(default=False, verbose_name='Последняя'),
        ),
    ]
