# Generated by Django 4.1.5 on 2023-01-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0011_alter_pelicula_poster_delete_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='foto',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='foto',
            field=models.URLField(blank=True, null=True),
        ),
    ]
