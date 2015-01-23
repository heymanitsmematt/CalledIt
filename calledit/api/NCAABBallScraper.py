import requests
import re

class Scraper:
    def __init__(self):
	self.teamsurl = 'http://espn.go.com/mens-college-basketball/teams'
	self.teamreq = requests.get(self.teamsurl)
	self.raw = self.teamreq.text
    def parse(self):
	self.teams = []
	self.step1 = self.raw[self.raw.find('span-4'):self.raw.find('id="Sponsored"')].split('<h5>')
	for item in self.step1:
	    if item.find('</h5>') != -1:
		thisTeam = item[item.find('>')+1:item.find('</a>')]
		thisTeamURL = item[[m.start() for m in re.finditer(r"teamId", item)][1]-20:]
		thisTeamURL = thisTeamURL[:thisTeamURL.find(">")-1]
		self.teams.append((thisTeam, thisTeamURL))
	 
class ScheduleScraper:
    def __init__(self, teams):
	self.baseURL = 'http://espn.go.com'
	self.results = {}
	self.follies = []
	def hasNumbers(string):
	    return any(char.isdigit() for char in string)
	for team in teams:
	    thisSchedule = []
	    thisURL = self.baseURL + team[1]
	    thisrequest = requests.get(thisURL)
	    thisrequestRaw = thisrequest.text[thisrequest.text.find('<table'):thisrequest.text.find('</table>')].split('<tr')
	    for event in thisrequestRaw:
		try:
		    test = event.split('<td')
		    if hasNumbers(test[1]) == False:
		       raise MyError(event)
		    else:
			event = event.split('<td')
		        thisDate = event[1][1:-5]
		        thisOpponent = event[2]
		        thisOpponent = thisOpponent[thisOpponent.find('team-name'):]
		        thisOpponent = thisOpponent[thisOpponent.find('>')+1:thisOpponent.find('</a>')]
			thisOpponent = thisOpponent[thisOpponent.find('>')+1:]
			thisResult = event[3][event[3].find('game-status')+12:event[3].find('<span')-2]
		        if thisResult.find('<') != -1:
			    thisResult = 'Pending'
			thisScore = event[3][event[3].find('score')+9:event[3].find('</a>')]
		        thisScore = thisScore[thisScore.find('>')+1:]
			if thisScore.find('<') != -1:
			    thisScore = 'Pending'
		        thisSchedule.append((thisDate, thisOpponent, thisResult, thisScore))
		        self.results[team[0]]={'schedule' : thisSchedule}
		except MyError as err:
		    pass
		except Exception as oops:
		    self.follies.append(event)	
		    pass

class MyError(Exception):
    def __init__(self, value):
	self.value = value
    def __str__(self):
	return repr(self.value)

if __name__ == "__name__":
    pass
