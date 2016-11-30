from django.shortcuts import render, redirect
from linkedin import linkedin
import requests
from django.contrib.auth import logout as auth_logout
import urllib2
import json
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def login(request):
	return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

def home(request):
	return render(request, 'home.html')

def linkedin_response(request):
	API_KEY = "75i4121vcmndhp"
	API_SECRET = "Zi6dEWMS9GijIyuS"
	RETURN_URL = "http://9efbc57c.ngrok.io/complete/linkedin-oauth2/"
	code = request.GET.get('code')
	authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL)
	authentication.authorization_code = code
	token = authentication.get_access_token()
	application = linkedin.LinkedInApplication(token=token)
	print 'profile--------------', application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'headline','distance', 'num-connections', 'skills', 'educations','public-profile-url'])
	return render(request, 'login.html')


