# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0013_kitty_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitty',
            name='photo',
            field=models.ImageField(default='../images/None/no-img.jpg', upload_to='../images/'),
        ),
    ]
