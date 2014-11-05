# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0004_kitty_posted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitty',
            name='gender',
            field=models.CharField(max_length=1, choices=[('F', 'Female'), ('M', 'Male')]),
        ),
    ]
