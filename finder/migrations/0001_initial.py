# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitty',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, default='M', null=True)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=200)),
                ('about', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
