from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path(r'dashboard/',views.dashboard),
    path(r'property/',views.property),
    path(r'user/', views.user, name='user'),
    path(r'table/',views.table),
]
