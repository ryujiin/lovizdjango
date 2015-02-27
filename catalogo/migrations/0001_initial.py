# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import catalogo.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
                ('full_name', models.CharField(max_length=255, editable=False, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=120, editable=False)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(max_length=250, null=True, upload_to=b'categorias', blank=True)),
                ('padre', models.ForeignKey(blank=True, to='catalogo.Categoria', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True, editable=False, max_length=120, blank=True, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120, null=True, blank=True)),
                ('full_name', models.CharField(max_length=120, unique=True, null=True, editable=False, blank=True)),
                ('slug', models.CharField(unique=True, max_length=120, editable=False)),
                ('activo', models.BooleanField(default=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('detalles', models.TextField(null=True, blank=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('video', models.CharField(max_length=120, null=True, blank=True)),
                ('categorias', models.ManyToManyField(related_name='categorias_producto', null=True, to='catalogo.Categoria', blank=True)),
                ('marca', models.ForeignKey(blank=True, to='catalogo.Marca', null=True)),
                ('parientes', models.ManyToManyField(related_name='parientes_rel_+', null=True, to='catalogo.Producto', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductoImagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(upload_to=catalogo.models.url_imagen_pr)),
                ('orden', models.PositiveIntegerField(default=0)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('producto', models.ForeignKey(related_name='imagenes_producto', to='catalogo.Producto')),
            ],
            options={
                'ordering': ['orden'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductoVariacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio_minorista', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('oferta', models.PositiveIntegerField(default=0)),
                ('producto', models.ForeignKey(related_name='variaciones', to='catalogo.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True, editable=False, max_length=120, blank=True, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productovariacion',
            name='talla',
            field=models.ForeignKey(to='catalogo.Talla'),
            preserve_default=True,
        ),
    ]
