# Generated by Django 4.1.5 on 2023-01-13 00:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0020_actor_pelishechas_director_pelishechas'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='cast',
            field=models.ManyToManyField(related_name='cast', to=settings.AUTH_USER_MODEL),
        ),
    ]
