# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_team_predictions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='Event',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='Sport',
            new_name='sport',
        ),
    ]
