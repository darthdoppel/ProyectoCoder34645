# Generated by Django 4.1.5 on 2023-01-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0010_pelicula_descripcion_alter_pelicula_poster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='poster',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
