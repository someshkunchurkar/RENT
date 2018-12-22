# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'boot/dashboard.html')

def property(request):
    return render(request, 'boot/property.html')

def user(request):
    return render(request, 'user.html')


def table(request):
    return render(request, 'boot/table.html')