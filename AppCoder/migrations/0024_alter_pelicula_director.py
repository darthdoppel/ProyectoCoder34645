# Generated by Django 4.1.5 on 2023-01-13 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0023_pelicula_cast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pelishechasdirectores', to='AppCoder.director'),
        ),
    ]
