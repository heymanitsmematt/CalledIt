
from app.models import *

ncs = Team.objects.all().filter(teamName = 'NC State')
for t in ncs:
    t.altTeamName = 'North Carolina'
    t.save()

ncse = Event.objects.all().filter(teamName = 'NC State')
for t in ncse:
    t.altTeamName = 'North Carolina'
    t.save()


