# URLconf, maps view from 'views.py' to 'index view'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]

