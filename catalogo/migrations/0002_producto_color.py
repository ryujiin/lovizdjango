# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='color',
            field=models.ForeignKey(blank=True, to='catalogo.Color', null=True),
            preserve_default=True,
        ),
    ]
