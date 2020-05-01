# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ASIG_CATEGORIA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='ASIG_PRODUCTO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cantidad', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ASIG_ROL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='BODEGA',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CATEGORIA_PRODUCTO',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CLIENTE',
            fields=[
                ('dpi', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('nit', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LISTA_PRODUCTO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cantidad', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LOG_ACT_INVENTARIO',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cantidad_antigua', models.BigIntegerField()),
                ('cantidad_nueva', models.BigIntegerField()),
                ('motivo', models.CharField(max_length=150)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ORDEN_VENTA',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha_facturacion', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('estado', models.CharField(max_length=150)),
                ('cliente_dpi', models.ForeignKey(to='app.CLIENTE')),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCTO',
            fields=[
                ('sku', models.BigIntegerField(primary_key=True, serialize=False)),
                ('codigo_barras', models.CharField(max_length=150)),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ROL',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SEDE',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('alias', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('departamento', models.CharField(max_length=150)),
                ('municipio', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='USUARIO',
            fields=[
                ('dpi', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=60)),
                ('correo', models.CharField(max_length=150)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='sede',
            name='encargado_dpi',
            field=models.ForeignKey(to='app.USUARIO'),
        ),
        migrations.AddField(
            model_name='orden_venta',
            name='repartidor_dpi',
            field=models.ForeignKey(related_name='repartidor_dpi', to='app.USUARIO'),
        ),
        migrations.AddField(
            model_name='orden_venta',
            name='vendedor_dpi',
            field=models.ForeignKey(related_name='vendedor_dpi', to='app.USUARIO'),
        ),
        migrations.AddField(
            model_name='log_act_inventario',
            name='usuario_dpi',
            field=models.ForeignKey(to='app.USUARIO'),
        ),
        migrations.AddField(
            model_name='lista_producto',
            name='orden_venta_id',
            field=models.ForeignKey(to='app.ORDEN_VENTA'),
        ),
        migrations.AddField(
            model_name='lista_producto',
            name='producto_sku',
            field=models.ForeignKey(to='app.PRODUCTO'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='sede_id',
            field=models.ForeignKey(to='app.SEDE'),
        ),
        migrations.AddField(
            model_name='bodega',
            name='encargado_dpi',
            field=models.ForeignKey(to='app.USUARIO'),
        ),
        migrations.AddField(
            model_name='bodega',
            name='sede_id',
            field=models.ForeignKey(to='app.SEDE'),
        ),
        migrations.AddField(
            model_name='asig_rol',
            name='rol_id',
            field=models.ForeignKey(to='app.ROL'),
        ),
        migrations.AddField(
            model_name='asig_rol',
            name='usuario_dpi',
            field=models.ForeignKey(to='app.USUARIO'),
        ),
        migrations.AddField(
            model_name='asig_producto',
            name='bodega_id',
            field=models.ForeignKey(to='app.BODEGA'),
        ),
        migrations.AddField(
            model_name='asig_producto',
            name='producto_sku',
            field=models.ForeignKey(to='app.PRODUCTO'),
        ),
        migrations.AddField(
            model_name='asig_categoria',
            name='categoria_id',
            field=models.ForeignKey(to='app.CATEGORIA_PRODUCTO'),
        ),
        migrations.AddField(
            model_name='asig_categoria',
            name='product_sku',
            field=models.ForeignKey(to='app.PRODUCTO'),
        ),
    ]
