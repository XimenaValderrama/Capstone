# Generated by Django 5.0.6 on 2024-11-23 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_razas_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipomascota',
            name='descripcion',
            field=models.CharField(choices=[('gato', 'Gato'), ('perro', 'Perro')], max_length=50),
        ),
    ]
