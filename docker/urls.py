
from django.contrib import admin
from django.urls import path, include
from docker.views import test

urlpatterns = [
    path('', view=test, name="Home")
]
