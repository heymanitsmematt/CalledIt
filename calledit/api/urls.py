from django.conf.urls import patterns
from django.views.generic import TemplateView
from views import UpdateNCAAMensBasketball, GetSportTeams, UpdateNFL, UpdateNBA, updateOdds
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('api/',
    (r'^ncaabball/$', csrf_exempt(UpdateNCAAMensBasketball.as_view())),
    (r'^updateOdds/$', csrf_exempt(updateOdds.as_view())),
    (r'^updateNBA/$', csrf_exempt(UpdateNBA.as_view())),
    (r'^updateNFL/$', csrf_exempt(UpdateNFL.as_view())),
    (r'^getSportTeams/(?P<sport>.*)$', GetSportTeams.as_view()),
)

