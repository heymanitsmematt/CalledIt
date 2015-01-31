from django.utils.decorators import method_decorator
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

class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
	return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)

class GetSportTeams(View):
    def get_context_data(self, **kwargs):
	context = super(GetSportTeams, self).get_context_data(**kwargs)
	qs = super(GetSportTeams, self).get_queryset()
	return context

    def get(self, request, *args, **kwargs):
	if self.request.method == 'GET':
	    self.sport = self.request.GET.get('sport')
	    print "sport = ", self.sport	 
	    self.sport = Sport.objects.get(sport=str(self.sport))
	    self.teams = Team.objects.all().filter(sport=self.sport)
	    self.teams = serializers.serialize('json', self.teams)
	    return HttpResponse(self.teams)	    

class UpdateNCAAMensBasketball(CSRFExemptMixin, View):
    def post(self, request):
	if request.method == 'POST':
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
		    
		    team.event.add(event)
		    team.save()

	return HttpResponse('updated')
