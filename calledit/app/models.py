from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    rating = models.BigIntegerField(null = True)
    friends = models.ForeignKey('self', null=True)

class Sport(models.Model):
    sport = models.CharField(max_length = 50)

    def __unicode__(self):
	return self.sport

class Event(models.Model):
    sportID = models.ForeignKey(Sport)
    eventName = models.CharField(max_length = 200)
    altTeamName = models.CharField(max_length = 100)
    eventDescription = models.CharField(max_length = 500, null=True)
    eventDate = models.DateField(null=True)
    odds = models.CharField(max_length=500, null=True)   
 
    def __unicode__(self):
	return self.eventName

class Party(models.Model):
    Event = models.ForeignKey(Event, null=True)
    partyName = models.CharField(max_length = 50)
    partyDescription = models.CharField(max_length = 200)

    def __unicode__(self):
	return self.partyName

class Tournament(models.Model):
    tournamentName = models.CharField(max_length=100)
    tournamentSport = models.ForeignKey(Sport, null=True)

class Prediction(models.Model):
    eventID = models.ForeignKey(Event)
    predictionDate = models.DateField(auto_now_add=True)
    userID = models.ForeignKey(User)
    winner = models.ForeignKey(Party)
    score = models.IntegerField(null=True)
    notes = models.CharField(max_length=500, null=True)
    
class Team(models.Model):
    teamName = models.CharField(max_length=100)
    altTeamName = models.CharField(max_length=100)
    event = models.ManyToManyField(Event, null=True)
    sport = models.ForeignKey(Sport)
    predictions = models.ForeignKey(Prediction, null=True)

class Division(models.Model):
    teamID = models.ManyToManyField(Team, null=True, default='NULL')
    division = models.CharField(max_length = 100)



