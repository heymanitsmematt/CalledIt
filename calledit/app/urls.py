from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from app.views import Main 
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
    (r'^$', Main.as_view()),
)

