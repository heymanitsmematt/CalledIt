from app.models import User, Sport, Event, Party, Prediction
from django.views.generic import TemplateView, View, ListView
from django.http import HttpResponse
import simplejson
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.template import RequestContext, loader
import requests
from NCAABBallScraper import Scraper, ScheduleScraper
from ESPNScraper import ESPNScraper, ESPNScheduleScraper
from app.models import Sport, Team, Event, User, Party, Prediction, Division
from api.Odds import eventOutline, parseOdds, Matcher

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

class updateOdds(CSRFExemptMixin, View):
    def post(self, request):
	if request.method == 'POST':
	    ncaas = Team.objects.all().filter(sport_id = 3)
	    event = ncaas[3].event.all()[3]
	    ol = eventOutline(event)
	    odds1 = parseOdds(ol.requestRaw)
	    #odds2 = parseOdds(ol.request2Raw)
	    for team in ncaas:
		m1 = Matcher(team, odds1.spit())
		#m2 = Matcher(team, odds2.spit())
		try:
		    thisEvent = m1.match()[2]
		    thisEvent.odds = str(m1.match()[3][0][0]) +" "+ str(m1.match()[3][0][1]) +","+ str(m1.match()[3][1][0]) +" "+ str(m1.match()[3][1][1])
		    thisEvent.save()	
		    print 'saved m1 ' + m1.match()
		except:
		    try:
			thisEvent = m2.match()[2]
		        thisEvent.odds = str(m2.match()[3][0][0]) +" "+ str(m2.match()[3][0][1]) +","+ str(m2.match()[3][1][0]) +" "+ str(m1.match()[3][1][1])
		        thisEvent.save()
			print 'saved m2 ' + m2.match()
		    except: 
			#print 'noooooajeoiaew'
			pass
	return HttpResponse('success')


class UpdateNBA(CSRFExemptMixin, View):
    def post(self, request):
	if request.method == 'POST':
	    sport = Sport.objects.get_or_create(sport = 'NBA')[0]
	    sport.save()
	    scraper = ESPNScraper('nba')
	    scraper.parse()
	    nbaSS = ESPNScheduleScraper('nba', scraper.results)
	    for div in nbaSS.results:
		thisDivision = Division.objects.get_or_create(division = div)[0]
		thisDivision.save()
		for team in nbaSS.results[div]['teams']:
		    thisTeam = Team.objects.get_or_create(teamName = team, sport=sport)[0]
		    thisTeam.save()
		    thisDivision.teamID.add(thisTeam)
		    for event in nbaSS.results[div]['teams'][team]['schedule']:
		        eventDate = event[0]
		        eventDay = eventDate[8:]
		        if eventDay[0] == 0:
		            pass
			else:
			    eventDay = '0'+eventDay[1]
			eventMonth = monthGetter(eventDate[5:8],months)
			if eventMonth < 4:
			    eventYear = '2015'
			else:
			    eventYear = '2014'
			eventDate = '-'.join((str(eventYear),str(eventMonth), str(eventDay)))
			thisEvent = Event.objects.get_or_create(sportID = sport, eventName = event[1], eventDate=eventDate)[0]
			thisEvent.save()
			thisTeam.event.add(thisEvent)
	return HttpResponse(nbaSS.results)

class UpdateNFL(CSRFExemptMixin, View):
    def post(self, request):
	if request.method == 'POST':
	    sport = Sport.objects.get_or_create(sport = 'NFL')[0]
	    sport.save()
	    scraper = ESPNScraper('nfl')
	    scraper.parse()
	    nflSS = ESPNScheduleScraper('nfl', scraper.results)
	    for div in nflSS.results:
		thisDivision = Division.objects.get_or_create(division = div)[0]
		thisDivision.save()
		for team in nflSS.results[div]['teams']:
		    thisTeam = Team.objects.get_or_create(teamName = team, sport=sport)[0]
		    thisTeam.save()
		    thisDivision.teamID.add(thisTeam)
		    for event in nflSS.results[div]['teams'][team]['schedule']:
		        eventDate = event[0]
		        eventDay = eventDate[8:]
		        if eventDay[0] == 0:
		            pass
			else:
			    eventDay = '0'+eventDay[1]
			eventMonth = monthGetter(eventDate[5:8],months)
			if eventMonth < 4:
			    eventYear = '2015'
			else:
			    eventYear = '2014'
			eventDate = '-'.join((str(eventYear),str(eventMonth), str(eventDay)))
			thisEvent = Event.objects.get_or_create(sportID = sport, eventName = event[1], eventDate=eventDate)[0]
			thisEvent.save()
			thisTeam.event.add(thisEvent)
	return HttpResponse(nflSS.results)

			
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
		    if eventDate[5:8] == 'Nov' or eventDate[5:8] == 'Dec':
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

