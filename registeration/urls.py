from django.contrib import admin
from django.urls import path, include
from .views import onboard_user, get_newsletter, subscribe_newsletter

urlpatterns = [
    path('onboard_user/', onboard_user),
    path('get_newsletter/', get_newsletter),
    path('subscribe_newsletter/', subscribe_newsletter),
]