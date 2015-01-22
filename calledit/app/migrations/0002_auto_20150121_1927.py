# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teamName', models.CharField(max_length=100)),
                ('Event', models.ManyToManyField(to='app.Event', null=True)),
                ('Sport', models.ForeignKey(to='app.Sport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='prediction',
            name='predictionDate',
            field=models.DateField(default=datetime.date(2015, 1, 21), auto_now_add=True),
            preserve_default=False,
        ),
    ]
