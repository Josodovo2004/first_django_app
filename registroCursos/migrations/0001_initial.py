# Generated by Django 5.0.1 on 2024-01-18 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCurso', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAlumno', models.CharField(max_length=50)),
                ('apelidoAlumno', models.CharField(max_length=50)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroCursos.curso')),
            ],
        ),
    ]
