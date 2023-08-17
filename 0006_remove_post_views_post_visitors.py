# Generated by Django 4.2.2 on 2023-08-11 15:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.AddField(
            model_name='post',
            name='visitors',
            field=models.ManyToManyField(blank=True, related_name='visited_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
