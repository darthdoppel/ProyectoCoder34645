# Generated by Django 4.1.5 on 2023-01-10 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0015_delete_resenia'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='peliculas',
            field=models.ManyToManyField(related_name='actores', to='AppCoder.pelicula'),
        ),
    ]
