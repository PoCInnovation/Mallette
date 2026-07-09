# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from www.models import Team


def index(request):
	context = {}
	return render(request, 'www/welcome.html', context)

def challenges(request):
	context = {}
	return render(request, 'www/challenges.html', context)

def contact(request):
	context = {}
	return render(request, 'www/contact.html', context)

def partners(request):
	context = {}
	return render(request, 'www/partners.html', context)

def searchTeams(request):
	"""
	Get List of Teams using a searchfield
	Raw queries are evil e^e
	Solution for now: {" [injection here] --}
	Get names of tables: " UNION SELECT 1, name, 2 FROM sqlite_master WHERE type='table'--
	Get flag: " UNION SELECT 1, flag, 3 FROM www_challenge--
	"""
	query = request.GET['q']
	banned = ["DELETE", "UPDATE", "EXECUTE"]
	tests = [ x in query for x in banned ]
	if True in tests:
		raise Http404
	if query == "":
		list = Team.objects.all().order_by('-score')
	else:
		list = Team.objects.raw('SELECT * FROM www_team WHERE name LIKE "{}"'.format(query))
	context = {
		'list': list
	}
	return render(request, 'www/teams.html', context)
	

def teams(request):
	list = Team.objects.all().order_by('-score')
	context = {
		'list': list
	}
	return render(request, 'www/teams.html', context)