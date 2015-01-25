from django.conf.urls import patterns
from django.views.generic import TemplateView
from views import UpdateNCAAMensBasketball
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('api/',
    (r'^ncaabball/$', UpdateNCAAMensBasketball.as_view())
)

