# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0012_auto_20141104_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitty',
            name='status',
            field=models.CharField(choices=[('Need', 'Needs a home'), ('Adopted!', 'Adopted!')], default='Need', max_length=20),
            preserve_default=True,
        ),
    ]
