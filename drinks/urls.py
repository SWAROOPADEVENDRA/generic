from django.urls import path
from drinks.views import *

app_name='drinks'

urlpatterns=[
    path('apple/',apple,name='apple'),
    path('pine_apple/',pine_apple,name='pine_apple')
]