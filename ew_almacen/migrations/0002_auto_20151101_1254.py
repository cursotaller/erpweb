# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ew_almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categoria',
            },
        ),
        migrations.AddField(
            model_name='insumo',
            name='created_at',
            field=models.DateTimeField(default='2015-11-01', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insumo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default='2015-11-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insumo',
            name='categoria',
            field=models.ForeignKey(null=True, blank=True, to='ew_almacen.Categoria'),
        ),
    ]
