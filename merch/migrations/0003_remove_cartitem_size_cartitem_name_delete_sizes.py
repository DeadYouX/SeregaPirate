# Generated by Django 5.0.2 on 2024-04-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0002_sizes_remove_cartitem_size_cartitem_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='size',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='name',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default=1, max_length=2, verbose_name='Размер'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Sizes',
        ),
    ]
