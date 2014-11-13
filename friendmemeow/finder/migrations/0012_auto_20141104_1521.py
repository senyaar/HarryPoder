# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0011_remove_kitty_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelter',
            name='email',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='phone',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
    ]
