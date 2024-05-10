# Generated by Django 5.0.2 on 2024-03-08 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='albums/static/albums/', verbose_name='Фотография')),
                ('link', models.CharField(blank=True, max_length=100, verbose_name='Ссылка на альбом')),
                ('date', models.IntegerField(default=2024, verbose_name='Год создания')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
    ]
