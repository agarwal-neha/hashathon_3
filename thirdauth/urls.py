"""thirdauth URL Configuration

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

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'fbauth.views.home', name='home'),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^login/$', 'fbauth.views.login', name='login'),
   url(r'^logout/$', 'fbauth.views.logout', name='logout'),
   url(r'^complete/linkedin-oauth2/$', 'fbauth.views.linkedin_response', name='linkedin'),
   url('', include('django.contrib.auth.urls', namespace='auth')),
   url('', include('social.apps.django_app.urls', namespace='social')),
   # url(r'^linkedin-data/', 'fbauth.views.linkedin_setup')
)
