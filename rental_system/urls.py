from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.home,name='Home'),
    path(r'about/',views.about,name='About')
]