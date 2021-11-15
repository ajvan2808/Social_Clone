from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from . import forms

# Create SignUp view. Display signup form
# Once s.o has singed up for our actual website, then on a successful sign up we will reverse them back to the login page.
# Otherwise it's just normal reverse  
class SignUp(CreateView):
	form_class = forms.UserSignUpForm 
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'