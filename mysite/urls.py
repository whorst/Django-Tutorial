"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

'''
///////
Urls.py will hold all of the urls that are to be rendered. This will be in the view.
These can either be function or class based views.
///////
'''



from django.conf.urls import url, patterns
#from django.conf.urls.defaults import *
from django.conf.urls import include
from django.contrib import admin



urlpatterns = [
    url(r'^polls/', include('polls.urls')), # When you load up the site, one can either go to poll.urls or admin.site.urls
    url(r'^admin/', admin.site.urls),
]
