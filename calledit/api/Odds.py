import requests
import re
from app.models import *
import time
import datetime

class eventOutline:
    def __init__(self, event):
	self.event = event
	self.sportID = event.sportID_id
	self.sport = Sport.objects.all().filter(id=self.sportID)[0]
	if self.sportID ==3:
	    self.sport = 'college-basketball'
	else:
	    self.sport = self.sport.sport
	self.baseURL = 'http://www.vegasinsider.com/'
	self.urlEnd = '/odds/las-vegas/money/'
	self.url = self.baseURL + self.sport + self.urlEnd
	self.request = requests.get(self.url)
	self.request2 = requests.get(self.url + '2/')
	self.requestRaw = self.request.text 
	self.request2Raw = self.request.text

class parseOdds:
    def __init__(self, requestRaw):
	self.raw = requestRaw
	rawTables = [m.start() for m in re.finditer('<table', self.raw)]
	self.raw = self.raw[rawTables[11]:rawTables[12]].split('<tr')
	self.results = {}
	self.errors = {}
	i = 1
	while i < len(self.raw):
	    thisMatchup = self.raw[i]
	    tableTexts = [m.start() for m in re.finditer('tabletext', thisMatchup)]
	    thisHomeTeam = thisMatchup[thisMatchup.find('tabletext')+10:thisMatchup.find('</a>')]
	    try:
	        thisOpponent = thisMatchup[tableTexts[1]+10:]
	        thisOpponent = thisOpponent[:thisOpponent.find('</a>')]	
	        thisGameOdds = thisMatchup[thisMatchup.find('odds'):]
	        thisGameOdds = thisGameOdds[thisGameOdds.find('<br>')+4:thisGameOdds.find('</a>')-8]
	        thisGameOdds = thisGameOdds.split('<br>')
	        self.home = (thisHomeTeam, thisGameOdds[0])
	        self.away = (thisOpponent, thisGameOdds[1])
	        self.results[i] = [self.home, self.away]
	        i += 1
	    except:
		i += 1

    def spit(self):
	return self.results
	
class Matcher:
    def __init__(self, team, odds):
	self.team = team
	#self.events = self.team.event.all().filter(eventDatetime.strftime("%d/%m/%Y"))
	self.odds = odds
        self.event = []

	for game in self.odds.values():
	    for home in game[0]:
		if self.team.teamName == home:
		    for event in self.team.event.all():
			if event.eventName in game[1] or event.altTeamName in game[1]:
			    self.event.append([self.team, self.team.teamName, event, game])
		elif self.team.altTeamName == home:
		    for event in self.team.event.all():
			if event.eventName in game[1] or event.altTeamName in game[1]:
			    self.event.append([self.team, self.team.teamName, event, game])
		else:
		    try:
			if self.team.teamName[:6] == home[:6]:
		    	    for event in self.team.event.all():
				if event.eventName in game[1] or event.altTeamName in game[1]:
			    	    self.event.append([self.team, self.team.teamName, event, game])
		    except: pass


    def match(self):
        if len(self.event)>0:
            for e in self.event:
		diff = e[2].eventDate - datetime.date.today()
		if diff.days < 2:
		    return e
		


