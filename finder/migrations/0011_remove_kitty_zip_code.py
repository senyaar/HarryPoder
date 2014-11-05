# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0010_auto_20141104_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitty',
            name='zip_code',
        ),
    ]
