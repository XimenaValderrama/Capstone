# Generated by Django 5.0.6 on 2024-10-20 02:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_ciudad_provincia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComunaMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DescripcionMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_fisica', models.TextField()),
                ('desc_personalidad', models.TextField()),
                ('desc_adicional', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EstadoMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(choices=[('pendiente', 'Pendiente'), ('adoptado', 'Adoptado'), ('en_adopcion', 'En adopcion'), ('perdido', 'Perdido'), ('encontrado', 'Encontrado')], default='pendiente', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FichaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_medica', models.DateField()),
                ('prox_consulta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Fundacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('desc_fundacion', models.TextField()),
                ('imagen', models.ImageField(upload_to='fundaciones/')),
                ('url_fundacion', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='GeneroMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(choices=[('macho', 'Macho'), ('hembra', 'Hembra')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaisMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProvinciaMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Razas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAlimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCirugia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='perfilusuario',
            name='direccion_usuario',
        ),
        migrations.AddField(
            model_name='direccionusuario',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.perfilusuario'),
        ),
        migrations.AddField(
            model_name='formularioadopcion',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.perfilusuario'),
        ),
        migrations.CreateModel(
            name='DireccionMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.comunamascota')),
            ],
        ),
        migrations.CreateModel(
            name='Esteriliacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conf_esterilizacion', models.BooleanField(default='False')),
                ('fecha_esterilizacion', models.DateField()),
                ('lugar_esterilizacion', models.CharField(max_length=50)),
                ('ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.fichamedica')),
            ],
        ),
        migrations.CreateModel(
            name='Desparacitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conf_desparacitacion', models.BooleanField(default='False')),
                ('fecha_desparacitacion', models.DateField()),
                ('ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.fichamedica')),
            ],
        ),
        migrations.CreateModel(
            name='Chip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conf_chip', models.BooleanField(default='False')),
                ('fecha_colocacion', models.DateField()),
                ('lugar_colocacion', models.CharField(max_length=50)),
                ('ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.fichamedica')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='mascotas/')),
                ('descripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.descripcionmascota')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.direccionmascota')),
                ('estado_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.estadomascota')),
                ('fundacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.fundacion')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.generomascota')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.perfilusuario')),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.razas')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.tipomascota')),
            ],
        ),
        migrations.AddField(
            model_name='fichamedica',
            name='mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.mascota'),
        ),
        migrations.AddField(
            model_name='formularioadopcion',
            name='mascota',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.mascota'),
        ),
        migrations.AddField(
            model_name='comunamascota',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.provinciamascota'),
        ),
        migrations.CreateModel(
            name='RegionMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.paismascota')),
            ],
        ),
        migrations.AddField(
            model_name='provinciamascota',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.regionmascota'),
        ),
        migrations.AddField(
            model_name='fichamedica',
            name='tipo_alimetno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.tipoalimento'),
        ),
        migrations.CreateModel(
            name='Cirugia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_cirugia', models.DateField()),
                ('ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.fichamedica')),
                ('tipo_cirugia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.tipocirugia')),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_vacuna', models.DateField()),
                ('ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.fichamedica')),
            ],
        ),
        migrations.CreateModel(
            name='Veterinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('ficha_medica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.fichamedica')),
            ],
        ),
    ]
