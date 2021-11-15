from django.urls import path
from django.contrib.auth import views as auth_views # the "contrib.auth" provide login and logout views so we named it auth_views to clarify
from . import views

app_name = 'accounts'

urlpatterns =[
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('signup/', views.SignUp.as_view(), name='signup'),
]