# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0004_auto_20141129_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='image',
            field=models.FileField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
