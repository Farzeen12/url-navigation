from django.urls import path
from benz.views import *

app_name='benz'

urlpatterns=[

path('car/',car,name='car'),

]