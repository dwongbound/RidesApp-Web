from django.urls import path

from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatters = [
    path('sms-response', views.test_parse, name='rando')
]