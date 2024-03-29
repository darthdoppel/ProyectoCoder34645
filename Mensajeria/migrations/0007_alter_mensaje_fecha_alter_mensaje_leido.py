# Generated by Django 4.1.5 on 2023-01-12 02:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mensajeria', '0006_mensaje_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='leido',
            field=models.BooleanField(choices=[(True, 'Leido'), (False, 'No leido')], default=False),
        ),
    ]
