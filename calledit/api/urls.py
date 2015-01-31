from django.conf.urls import patterns
from django.views.generic import TemplateView
from views import UpdateNCAAMensBasketball, GetSportTeams
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('api/',
    (r'^ncaabball/$', csrf_exempt(UpdateNCAAMensBasketball.as_view())),
    (r'^getSportTeams/(?P<sport>.*)$', GetSportTeams.as_view()),
)

