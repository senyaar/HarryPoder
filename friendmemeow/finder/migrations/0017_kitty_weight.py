# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0016_auto_20141110_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitty',
            name='weight',
            field=models.IntegerField(default=5),
            preserve_default=True,
        ),
    ]
