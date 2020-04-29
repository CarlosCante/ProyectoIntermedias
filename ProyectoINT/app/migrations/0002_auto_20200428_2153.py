# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha_facturacion', models.DateField(null=True)),
                ('cliente', models.ForeignKey(to='app.Cliente')),
                ('vendedor', models.ForeignKey(to='app.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Venta_Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cantidad', models.IntegerField()),
                ('id_producto', models.ForeignKey(to='app.Producto')),
                ('id_venta', models.ForeignKey(to='app.Venta')),
            ],
        ),
        migrations.RemoveField(
            model_name='bodega',
            name='id_bodega',
        ),
        migrations.RemoveField(
            model_name='sede',
            name='id_sede',
        ),
        migrations.AddField(
            model_name='bodega',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, default=0, serialize=False, auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sede',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, default=0, serialize=False, auto_created=True),
            preserve_default=False,
        ),
    ]
