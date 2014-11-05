# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0008_auto_20141103_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitty',
            name='size',
        ),
    ]
