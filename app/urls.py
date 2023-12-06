from django.urls import path,include
from .views import *
urlpatterns = [
    path('', landing , name='landing'),
    path('login/', login , name='login'),
    path('home/', home, name='home'),
    path('register/', register , name='register'),
]


