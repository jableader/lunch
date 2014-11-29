# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0002_order_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='canteen',
            field=models.ForeignKey(default='', to='lunch.Canteen'),
            preserve_default=False,
        ),
    ]
