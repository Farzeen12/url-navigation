from django.urls import path
from bmw.views import *

app_name='bmw'

urlpatterns=[

path('car/',car,name='car'),

]