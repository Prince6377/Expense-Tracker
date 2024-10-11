from django.urls import path,include
from .views import *
urlpatterns = [
    
    path("" , index , name='index'),
    path('delete-history/<uuid>/',deleteHistory, name = 'deleteHistory')
]
