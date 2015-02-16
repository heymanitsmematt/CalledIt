import requests
import time
import datetime
class Carl:
    def __init__(self, event, pick, amount, carlType):
	'''
		carlType is buy or sell
		pick is binary 0=home 1=away
	'''
	self.amount = amount
	self.carlType = carlType
	self.event = event
	self.odds = event.odds
	self.oddsTotal = (float(self.odds.split(',')[0][-3:]) + float(self.odds.split(',')[1][-3:])) / 100
	self.pick = self.odds.split(',')[pick]

    def moneyline(self):
	self.moneyLine = self.pick[-4:]
	self.ML1 = float(100)/float(self.moneyLine[-3:])
	self.ML2 = float(self.moneyLine[-3:])/float(100)
	if self.carlType == 'buy':
	    if self.moneyLine[0] == '+':
		return self.ML1
	    elif self.moneyLine[0] == '-':
		return self.ML2
	elif self.carlType == 'sell':
	    if self.moneyLine[0] == '+':
		return self.ML2
	    elif self.moneyLine[0] == '-':
		return self.ML1

    def carl(self, bet):
	'''
		bet is value returned from type of bet (eg. self.moneyline())
	'''
	self.dollarBonus = float(self.amount)/float(100)
	if self.dollarBonus > 2:
	    self.dollarBonus = 2
	self.today = datetime.date.today()
	diff = self.event.eventDate - self.today
	if diff.days == 0:
	    d = 1
	else:
	    d = diff.days
	self.timeBonus = 1+(d/float(365))
	if self.timeBonus >2:
	    self.timeBonus == 2
	self.wager = 10 * ((bet/self.oddsTotal)*self.dollarBonus*self.timeBonus)
	return self.wager

