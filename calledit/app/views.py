from django.shortcuts import render
from django.http import HttpResponse
import simplejson
from django.core import serializers
from django.template import RequestContext, loader
from django.views.generic import ListView, View, TemplateView, FormView
from models import User, Sport, Team, Event, Party, Prediction
from api.NCAABBallScraper import Scraper, ScheduleScraper

months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'
months = months.split()
def monthGetter(month, months):
    i=1
    for m in months:
	if month == m:
	    return i
	else: i += 1

class Main(View):
     model = User
     '''
     def get_context_data(self, **kwargs):
        context = super(Main, self).get_context_data(**kwargs)
	context['sport'] = Sport.objects.all()
	context['event'] = Event.objects.all()
	context['party'] = Party.objects.all()
	context['prediction'] = Prediction.objects.all()
    '''
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
	
