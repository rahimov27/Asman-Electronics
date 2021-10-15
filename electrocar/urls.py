from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', addclient, name='addclient')
]