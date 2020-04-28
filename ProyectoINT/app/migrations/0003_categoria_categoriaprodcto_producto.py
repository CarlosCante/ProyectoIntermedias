# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200428_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaProdcto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('idProducto', models.CharField(max_length=150)),
                ('idCategoria', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('SKU', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CodigoBarras', models.CharField(max_length=150)),
                ('Nombre', models.CharField(max_length=150)),
                ('Descripcion', models.CharField(max_length=150)),
                ('Precio', models.FloatField()),
            ],
        ),
    ]
