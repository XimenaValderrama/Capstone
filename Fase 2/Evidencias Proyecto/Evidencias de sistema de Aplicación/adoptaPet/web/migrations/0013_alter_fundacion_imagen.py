# Generated by Django 5.0.6 on 2024-11-22 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_rename_conf_chip_chip_confirmacion_chip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundacion',
            name='imagen',
            field=models.URLField(),
        ),
    ]
