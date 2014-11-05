# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0007_auto_20141103_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitty',
            name='breed',
            field=models.CharField(choices=[('Unknown/Mixed', 'Unknown/Mixed'), ('Abyssinian', 'Abyssinian'), ('American Bobtail', 'American Bobtail'), ('American Curl', 'American Curl'), ('American Shorthair', 'American Shorthair'), ('American Wirehair', 'American Wirehair'), ('Balinese', 'Balinese'), ('Birman', 'Birman'), ('Bombay', 'Bombay'), ('British Shorthair', 'British Shorthair'), ('Burmese', 'Burmese'), ('Burmilla', 'Burmilla'), ('Chartreux', 'Chartreux'), ('Chinese Li Hua', 'Chinese Li Hua'), ('Colorpoint Shorthair', 'Colorpoint Shorthair'), ('Cornish Rex', 'Cornish Rex'), ('Devon Rex', 'Devon Rex'), ('Egyptian Mau', 'Egyptian Mau'), ('European Burmese', 'European Burmese'), ('Exotic', 'Exotic'), ('Havana Brown', 'Havana Brown'), ('Japanese Bobtail', 'Japanese Bobtail'), ('Korat', 'Korat'), ('LaPerm', 'LaPerm'), ('Maine Coon Cat', 'Maine Coon Cat'), ('Manx', 'Manx'), ('Norwegian Forest Cat', 'Norwegian Forest Cat'), ('Ocicat', 'Ocicat'), ('Oriental', 'Oriental'), ('Persian', 'Persian'), ('RagaMuffin', 'RagaMuffin'), ('Ragdoll', 'Ragdoll'), ('Russian Blue', 'Russian Blue'), ('Scottish Fold', 'Scottish Fold'), ('Selkirk Rex', 'Selkirk Rex'), ('Siamese', 'Siamese'), ('Siberian', 'Siberian'), ('Singapura', 'Singapura'), ('Somali', 'Somali'), ('Sphynx', 'Sphynx'), ('Tonkinese', 'Tonkinese'), ('Turkish Angora', 'Turkish Angora'), ('Turkish Van', 'Turkish Van')], default='Un', max_length=30),
        ),
    ]
