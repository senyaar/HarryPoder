# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import finder.models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0014_auto_20141110_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitty',
            name='photo_garrett',
            field=models.ImageField(null=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='kitty',
            name='photo',
            field=models.FileField(upload_to=finder.models.get_upload_file_name),
        ),
    ]
