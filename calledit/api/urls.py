from django.conf.urls import patterns
from django.views.generic import TemplateView
from app.views import NCAABBall
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
    (r'^ncaabball/$', NCAABBall.as_view())
)

