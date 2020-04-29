# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200428_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenTransferencia',
            fields=[
                ('id_transferencia', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(null=True)),
                ('id_bodega', models.ForeignKey(db_column='id_bodega', to='app.Bodega')),
                ('id_cliente', models.ForeignKey(db_column='dpi', to='app.Cliente')),
                ('id_producto', models.ForeignKey(db_column='sku', to='app.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenVenta',
            fields=[
                ('id_venta', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(null=True)),
                ('id_bodega', models.ForeignKey(db_column='id_bodega', to='app.Bodega')),
                ('id_cliente', models.ForeignKey(db_column='dpi', to='app.Cliente')),
                ('id_producto', models.ForeignKey(db_column='sku', to='app.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id_sede', models.BigIntegerField(primary_key=True, serialize=False)),
                ('alias', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('departamento', models.CharField(max_length=150)),
                ('municipio', models.CharField(max_length=150)),
                ('encargado', models.ForeignKey(db_column='dpi', to='app.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='ordenventa',
            name='id_sede',
            field=models.ForeignKey(db_column='id_sede', to='app.Sede'),
        ),
        migrations.AddField(
            model_name='ordentransferencia',
            name='id_sede',
            field=models.ForeignKey(db_column='id_sede', to='app.Sede'),
        ),
    ]
