# Generated by Django 4.1.5 on 2023-01-11 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0018_alter_actor_peliculashechas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='peliculashechas',
        ),
    ]