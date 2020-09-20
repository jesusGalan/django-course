from django.contrib import admin
from django.urls import path, re_path

from . import views

app_name = "home_app"

urlpatterns = [
    path('nueva-url', views.IndexView.as_view(), name="index"),
]