from django.conf.urls import patterns, include, url
from django.contrib import admin
import app
import api
from app.views import Main

urlpatterns = patterns('',
    url(r'^$', Main.as_view()),
    url(r'^app/', include('app.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^social', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
)
