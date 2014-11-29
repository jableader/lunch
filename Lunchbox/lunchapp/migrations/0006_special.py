# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunchapp', '0005_kid_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specialImage', models.FileField(upload_to=b'')),
                ('item', models.OneToOneField(to='lunchapp.Item')),
                ('menu', models.ForeignKey(to='lunchapp.Menu')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
