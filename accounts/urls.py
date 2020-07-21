from django.urls import path

from . import views

urlpatterns = [
	path('register',views.register, name = 'register'),
	path('login',views.login, name = 'login'),
	path('edit_profile',views.edit_profile, name = 'edit_profile'),
	path('view_profile', views.view_profile, name = 'view_profile'),
	path('logout', views.logout, name = 'logout')
]


