# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id_bodega', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dpi', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('nit', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('dpi', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=60)),
                ('correo', models.CharField(max_length=150)),
                ('fecha_nacimiento', models.DateField()),
                ('encargado', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='bodega',
            name='encargado',
            field=models.ForeignKey(db_column='dpi', to='app.Usuario'),
        ),
    ]
