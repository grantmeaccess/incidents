from django.conf.urls import patterns, url

from incidents import views

urlpatterns = patterns('',
    # ex: /incidents/
    url(r'^$', views.index, name='index'),
    # ex: /incidents/5/
    url(r'^(?P<id>\d+)/$', views.details, name='details'),
    # ex: /incidents/offense/
    url(r'^offense/$', views.offenselist, name='offenselist'),
    # ex: /incidents/offense/Aggravated Assault/
    url(r'^offense/(?P<offense>[a-zA-Z0-9\s_.-]+)/$', views.offense, name='offense'),
    # ex: /incidents/5/date/
    #url(r'^(?P<id>\d+)/vote/$', views.date, name='date'),
    # ex: /incidents/map/
    url(r'^map/$', views.map, name='map'),

)
