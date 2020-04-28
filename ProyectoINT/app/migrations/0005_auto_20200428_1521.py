# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200428_1428'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoriaProdcto',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='CodigoBarras',
            new_name='codigoBarras',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Precio',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='SKU',
            new_name='sku',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ManyToManyField(db_column='id', to='app.Categoria'),
        ),
    ]
