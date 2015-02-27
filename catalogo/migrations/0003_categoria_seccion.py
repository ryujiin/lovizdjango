# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_producto_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='seccion',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'genero', b'Genero'), (b'categoria', b'Categoria'), (b'estilo', b'Estilo')]),
            preserve_default=True,
        ),
    ]
