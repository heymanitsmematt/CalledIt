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
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('division', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventName', models.CharField(max_length=200)),
                ('altTeamName', models.CharField(max_length=100)),
                ('eventDescription', models.CharField(max_length=500, null=True)),
                ('eventDate', models.DateField(null=True)),
                ('odds', models.CharField(max_length=500, null=True)),
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
                ('predictionDate', models.DateField(auto_now_add=True)),
                ('score', models.IntegerField(null=True)),
                ('notes', models.CharField(max_length=500, null=True)),
                ('eventID', models.ForeignKey(to='app.Event')),
                ('userID', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(to='app.Party')),
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
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teamName', models.CharField(max_length=100)),
                ('altTeamName', models.CharField(max_length=100)),
                ('event', models.ManyToManyField(to='app.Event', null=True)),
                ('predictions', models.ForeignKey(to='app.Prediction', null=True)),
                ('sport', models.ForeignKey(to='app.Sport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tournamentName', models.CharField(max_length=100)),
                ('tournamentSport', models.ForeignKey(to='app.Sport', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.BigIntegerField(null=True)),
                ('friends', models.ForeignKey(to='app.UserProfile', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='sportID',
            field=models.ForeignKey(to='app.Sport'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='division',
            name='teamID',
            field=models.ManyToManyField(default=b'NULL', to='app.Team', null=True),
            preserve_default=True,
        ),
    ]
