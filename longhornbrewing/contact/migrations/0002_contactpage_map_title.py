# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='map_title',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
