from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import Main


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'calledit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Main.as_view()),
    #url(r'^api$', include(api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
