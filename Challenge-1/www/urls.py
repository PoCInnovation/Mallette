from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('challenges', views.challenges, name='challenges'),
	path('partners', views.partners, name='partners'),
	path('teams', views.teams, name='teams'),
	path('teams/result', views.searchTeams, name='teams-result'),
	path('contact-us', views.contact, name='contact-us')
]