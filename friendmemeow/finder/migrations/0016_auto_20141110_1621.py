# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0015_auto_20141110_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitty',
            name='photo_garrett',
        ),
        migrations.AlterField(
            model_name='kitty',
            name='photo',
            field=models.ImageField(upload_to='', null=True),
        ),
    ]
