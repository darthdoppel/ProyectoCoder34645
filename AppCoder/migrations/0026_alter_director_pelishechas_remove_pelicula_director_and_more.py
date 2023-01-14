# Generated by Django 4.1.5 on 2023-01-14 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0025_alter_pelicula_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='pelishechas',
            field=models.ManyToManyField(related_name='pelishechasdirector', to='AppCoder.pelicula'),
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='director',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='director',
            field=models.ManyToManyField(related_name='pelishechasdirector', to='AppCoder.director'),
        ),
    ]
