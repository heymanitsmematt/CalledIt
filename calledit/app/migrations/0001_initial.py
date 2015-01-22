# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventName', models.CharField(max_length=200)),
                ('eventDescription', models.CharField(max_length=500, null=True)),
                ('eventDate', models.DateField(null=True)),
                ('odds', models.BigIntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('partyName', models.CharField(max_length=50)),
                ('partyDescription', models.CharField(max_length=200)),
                ('Event', models.ForeignKey(to='app.Event', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(null=True)),
                ('notes', models.CharField(max_length=500, null=True)),
                ('eventID', models.ForeignKey(to='app.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sport', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.BigIntegerField(null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='prediction',
            name='userID',
            field=models.ForeignKey(to='app.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prediction',
            name='winner',
            field=models.ForeignKey(to='app.Party'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='sportID',
            field=models.ForeignKey(to='app.Sport'),
            preserve_default=True,
        ),
    ]
