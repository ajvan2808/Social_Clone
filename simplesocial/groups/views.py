from django.db import models
from django.shortcuts import get_object_or_404, render
from django.contrib import messages

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin, 
										PermissionRequiredMixin)

from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from groups.models import Group, GroupMember


class CreateGroup(LoginRequiredMixin, generic.CreateView):
	fields = ('name', 'description')
	model = Group

class SingleGroup(generic.DetailView):
	model = Group

class ListGroups(generic.ListView):
	model = Group

class JoinGroup(LoginRequiredMixin, generic.RedirectView):
	
	# Once you join the group, go back to that group single page 
	def get_redirect_url(self, *args, **kwargs):
		return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

	def get(self, request, *args, **kwargs):
		group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

		try:
			GroupMember.objects.create(user=self.request.user, group=group)
		except IntegrityError: # or only except
			messages.warning(self.request, 'You already have an account!')
		else:
			messages.success(self.request, 'You are now a member!')

		return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
	
	def get_redirect_url(self, *args, **kwargs):
		return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

	def get(self, request, *args, **kwargs):

		try:
			membership = GroupMember.objects.filter(
				user=self.request.user,
				group__slug = self.kwargs.get('slug')
			).get()
		except GroupMember.DoesNotExist:
			messages.warning(self.request, 'You are not in the group!')
		else:
			membership.delete()
			messages.success(self.request, 'You have left the group.')
		
		return super().get(request, *args, **kwargs)