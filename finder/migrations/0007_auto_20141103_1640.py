# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0006_auto_20141103_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitty',
            name='breed',
            field=models.CharField(max_length=30, choices=[('Un', 'Unknown/Mixed'), ('Ab', 'Abyssinian'), ('AmBob', 'American Bobtail'), ('AmCurl', 'American Curl'), ('AmShort', 'American Shorthair'), ('AmWire', 'American Wirehair'), ('Bal', 'Balinese'), ('Bir', 'Birman'), ('Bom', 'Bombay'), ('BritShort', 'British Shorthair'), ('Burme', 'Burmese'), ('Burmi', 'Burmilla'), ('Chart', 'Chartreux'), ('Chi', 'Chinese Li Hua'), ('Col', 'Colorpoint Shorthair'), ('Corn', 'Cornish Rex'), ('dev', 'Devon Rex'), ('eg', 'Egyptian Mau'), ('eu', 'European Burmese'), ('ex', 'Exotic'), ('h', 'Havana Brown'), ('j', 'Japanese Bobtail'), ('k', 'Korat'), ('l', 'LaPerm'), ('mai', 'Maine Coon Cat'), ('man', 'Manx'), ('n', 'Norwegian Forest Cat'), ('oc', 'Ocicat'), ('ori', 'Oriental'), ('p', 'Persian'), ('raga', 'RagaMuffin'), ('ragd', 'Ragdoll'), ('rb', 'Russian Blue'), ('sco', 'Scottish Fold'), ('sel', 'Selkirk Rex'), ('sia', 'Siamese'), ('sib', 'Siberian'), ('sin', 'Singapura'), ('som', 'Somali'), ('sph', 'Sphynx'), ('ton', 'Tonkinese'), ('turkang', 'Turkish Angora'), ('turkvan', 'Turkish Van')], default='Un'),
        ),
    ]
