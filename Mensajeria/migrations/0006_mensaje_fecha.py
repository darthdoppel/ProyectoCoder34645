# Generated by Django 4.1.5 on 2023-01-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajeria', '0005_rename_mensaje_mensaje_cuerpo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
