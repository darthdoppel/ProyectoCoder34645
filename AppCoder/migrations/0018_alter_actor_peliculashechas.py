# Generated by Django 4.1.5 on 2023-01-10 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0017_remove_actor_peliculas_actor_peliculashechas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='peliculashechas',
            field=models.ManyToManyField(related_name='peliculashechas', to='AppCoder.pelicula'),
        ),
    ]