# Generated by Django 5.0.2 on 2024-04-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ForumProfile', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='ForumProfile/static/ForumProfile/avatar.jpg', null=True, upload_to='ForumProfile/static/ForumProfile/'),
        ),
    ]
