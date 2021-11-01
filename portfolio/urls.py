from django.urls import path
from .views import *

urlpatterns = [
    path('', portfolio, name='portfolio'),
    path('<slug:lang>', portfolio, name='portfolio'),
]
