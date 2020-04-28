# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_categoria_categoriaprodcto_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='SKU',
            field=models.CharField(primary_key=True, max_length=150, serialize=False),
        ),
    ]
