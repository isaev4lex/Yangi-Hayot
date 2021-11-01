from django.urls import path
from .views import *

urlpatterns = [
    path('', services, name='services'),
    path('<slug:lang>', services, name='services'),
    path('<slug:slug>/', services, name='card'),
    path('<slug:slug>/<slug:lang>/', services, name='card'),
]
