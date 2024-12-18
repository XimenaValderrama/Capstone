# Generated by Django 5.0.6 on 2024-11-20 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_mascota_tipo_edad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chip',
            old_name='conf_chip',
            new_name='confirmacion_chip',
        ),
        migrations.RenameField(
            model_name='desparasitacion',
            old_name='conf_desparasitacion',
            new_name='confirmacion_desparasitacion',
        ),
        migrations.RenameField(
            model_name='esterilizacion',
            old_name='conf_esterilizacion',
            new_name='confirmacion_esterilizacion',
        ),
        migrations.RenameField(
            model_name='fichamedica',
            old_name='tipo_alimetno',
            new_name='tipo_alimento',
        ),
        migrations.AlterField(
            model_name='fundacion',
            name='imagen',
            field=models.ImageField(upload_to='media/fundaciones/'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(upload_to='media/mascotas/'),
        ),
    ]
