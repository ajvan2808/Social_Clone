import django


from django.urls import path 
from . import views

app_name = 'groups'

urlpatterns = [
	path('', views.ListGroups.as_view(), name='all'),
	path('new/', views.CreateGroup.as_view(template_name='groups/group_create_form.html'), name='create'),
	# because this html template named differently. Auto app_name will be groups_ + url name 
	path('posts/in/<slug>/', views.SingleGroup.as_view(), name='single'),
	path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
	path('leave/<slug>/', views.LeaveGroup.as_view(), name='leave'),
	
]