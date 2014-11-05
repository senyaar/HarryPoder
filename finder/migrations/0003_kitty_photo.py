# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import finder.models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0002_auto_20141103_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitty',
            name='photo',
            field=models.FileField(default=2, upload_to=finder.models.get_upload_file_name),
            preserve_default=False,
        ),
    ]
