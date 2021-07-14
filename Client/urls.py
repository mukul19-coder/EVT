from django.contrib import admin
from django.urls import path

from Client.views import verification, signup_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup',signup_view, name='signup'), 
    path('verification', verification, name='verification'),
	]
