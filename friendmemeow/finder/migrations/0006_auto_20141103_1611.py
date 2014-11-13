# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0005_auto_20141103_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitty',
            old_name='location',
            new_name='zip_code',
        ),
        migrations.AlterField(
            model_name='kitty',
            name='breed',
            field=models.CharField(default=0, choices=[(0, 'Unknown/Mixed'), (1, 'Abyssinian'), (2, 'American Bobtail'), (3, 'American Curl'), (4, 'American Shorthair'), (5, 'American Wirehair'), (6, 'Balinese'), (7, 'Birman'), (8, 'Bombay'), (9, 'British Shorthair'), (10, 'Burmese'), (11, 'Burmilla'), (12, 'Chartreux'), (13, 'Chinese Li Hua'), (14, 'Colorpoint Shorthair'), (15, 'Cornish Rex'), (16, 'Devon Rex'), (17, 'Egyptian Mau'), (18, 'European Burmese'), (19, 'Exotic'), (20, 'Havana Brown'), (21, 'Japanese Bobtail'), (22, 'Korat'), (23, 'LaPerm'), (24, 'Maine Coon Cat'), (25, 'Manx'), (26, 'Norwegian Forest Cat'), (27, 'Ocicat'), (28, 'Oriental'), (29, 'Persian'), (30, 'RagaMuffin'), (31, 'Ragdoll'), (32, 'Russian Blue'), (33, 'Scottish Fold'), (34, 'Selkirk Rex'), (35, 'Siamese'), (36, 'Siberian'), (37, 'Singapura'), (38, 'Somali'), (39, 'Sphynx'), (40, 'Tonkinese'), (41, 'Turkish Angora'), (42, 'Turkish Van')], max_length=30),
        ),
        migrations.AlterField(
            model_name='kitty',
            name='gender',
            field=models.CharField(default='M', choices=[('F', 'Female'), ('M', 'Male')], max_length=1),
        ),
        migrations.AlterField(
            model_name='kitty',
            name='size',
            field=models.CharField(default='M', choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=10),
        ),
    ]
