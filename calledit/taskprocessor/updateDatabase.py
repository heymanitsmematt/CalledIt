import requests

class UpdateDatabase(object):
    def __init__(self, league):
	self.league = league
	self.updateReq = requests.post("http://calledit/api/" + league)
	print self.updateReq.text
