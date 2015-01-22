# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150121_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='predictions',
            field=models.ForeignKey(to='app.Prediction', null=True),
            preserve_default=True,
        ),
    ]
