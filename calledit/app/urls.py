from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from app.views import Main, register 
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
    url(r'^$', Main.as_view()),
    url(r'register', register),
    url(r'login', 'django.contrib.auth.views.login'),
    url(r'logout', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)

