from django.shortcuts import render, render_to_response
from app.models import User, Sport, Event, Party, Prediction
from django.views.generic import TemplateView, View, ListView
from django.http import HttpResponse
import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.template import RequestContext, loader
import requests
from NCAABBallScraper import Scraper, ScheduleScraper
from app.models import Sport, Team, Event, User, Party, Prediction


months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'
months = months.split()
def monthGetter(month, months):
    i=1
    for m in months:
	if month == m:
	    return i
	else: i += 1

class updateNcaaMensBasketball(View):
    sport = Sport.objects.get_or_create(sport = 'Ncaa Mens Basketball')[0]
    sport.save()
    scraper = Scraper()
    scraper.parse()
    schedScraper = ScheduleScraper(scraper.teams)
    results = schedScraper.results
    for key in results:
	thisTeam = key
	team = Team.objects.get_or_create(teamName = thisTeam, sport = sport)[0]
	team.save()
	thisTeamSched = results[thisTeam]['schedule']
	for event in thisTeamSched:
	    eventDate = event[0]
	    if eventDate[5:8] == 'Nov' or 'Dec':
		eventYear = '2014'
	    else:
		eventYear = '2015'
	    eventMonth = monthGetter(eventDate[5:8], months)
	    eventDay = eventDate[9:]
	    eventDate = '-'.join((eventYear,str(eventMonth), eventDay))
	    event  = Event.objects.get_or_create(sportID = sport, eventName = event[1], eventDate = eventDate)[0]
	    event.save()
	    try:
	        team.event_set.get(event = event)   
	    except:
		team.event.add(event.id)
	    team.save()
	
if     
