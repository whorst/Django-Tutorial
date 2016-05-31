from django.conf.urls import include
from django.conf.urls import url
from . import views

# When we get to polls, there's a number of things that we can do and a number of things that can happen.
#Usually, an HTML template is rendered from views.

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name ='index'), # ex: /polls/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), #/polls/5
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'), # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'), # ex: /polls/5/vote/
#I don't understand why .as_view is used. Thread safety? Denotes a class is being used? Who knows?

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
