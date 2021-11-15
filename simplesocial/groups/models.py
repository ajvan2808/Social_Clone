from enum import unique
from django.db import models
from django.utils.text import slugify 
from django.urls import reverse
''' 
slugify just allows us to remove any characters that are alphanumeric or underscores
or hyphens. And basically the idea behind that is if you have a string that has spaces in it and you want to use
that as part of the URL, it's going to be able to lowercase and add dashes instead of spaces.
''' 

import misaka as m  # allow us to likned and embeded markdown text
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

class Group(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(allow_unicode=True, unique=True)
	description = models.TextField(blank=True, default='')
	description_html = models.TextField(editable=False, default='', blank=True)
	members = models.ManyToManyField(User, through='GroupMember')

	'''
	A "slug" is a way of generating a valid URL, generally using data already obtained. 
	For instance, a slug uses the title of an article to generate a URL. I advise to generate the slug 
	by means of a function, given the title (or another piece of data), rather than setting it manually.
	'''

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		self.description_html = m.html(self.description)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('group:single', kwargs={'slug': self.slug})

	class Meta():
		ordering = ['name']

class GroupMember(models.Model):
	group = models.ForeignKey(Group, related_name='memeberships')
	user = models.ForeignKey(User, related_name='user_groups')

	def __str__(self):
		return self.user.username

	class Meta():
		unique_together = ('group', 'user')
