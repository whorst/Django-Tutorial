from django.conf.urls import include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name ='index'), # ex: /polls/

    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

#include() allows us to reference other URLconfs
#Whenever Django ecounters include(), it chops off whatever part of the url matched up
#to that point and sends the remaining string to the included URLconf for further
#processing


#VVVVVVVV
'''
The idea behind include() is to make it easy to plug and play URLs.

Use include when you include other URL patterns. '
'''
