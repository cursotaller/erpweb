# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=60)),
                ('detalle', models.TextField()),
                ('precio', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Insumos',
                'verbose_name': 'Insumo',
            },
        ),
    ]
