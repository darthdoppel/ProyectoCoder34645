# Generated by Django 4.1.5 on 2023-01-14 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_delete_perfil'),
        ('Mensajeria', '0007_alter_mensaje_fecha_alter_mensaje_leido'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.avatar'),
        ),
    ]
