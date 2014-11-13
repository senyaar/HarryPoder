# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitty',
            name='location',
            field=models.IntegerField(default=92122),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='kitty',
            name='age',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='kitty',
            name='gender',
            field=models.CharField(max_length=1),
        ),
    ]
