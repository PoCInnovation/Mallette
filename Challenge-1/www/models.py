# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Team(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(max_length=50)
	score = models.IntegerField(default=0)

class Challenge(models.Model):
	"""
	The flag is in there o/
	"""
	def __str__(self):
		return self.name
	name = models.CharField(max_length=70)
	max_score = models.IntegerField(default=0)
	flag = models.CharField(max_length=100)
	discovered_by = models.IntegerField(default=0)