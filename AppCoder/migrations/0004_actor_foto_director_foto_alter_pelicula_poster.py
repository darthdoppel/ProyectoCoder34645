# Generated by Django 4.1.5 on 2023-01-08 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_pelicula_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
        migrations.AddField(
            model_name='director',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters'),
        ),
    ]
