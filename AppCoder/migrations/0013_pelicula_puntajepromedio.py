# Generated by Django 4.1.5 on 2023-01-09 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0012_alter_actor_foto_alter_director_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='puntajepromedio',
            field=models.FloatField(default=0),
        ),
    ]