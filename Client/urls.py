from django.contrib import admin
from django.urls import path

from Client.views import signup_view

urlpatterns = [
	path('signup/',signup_view, name='signup'), 
	]