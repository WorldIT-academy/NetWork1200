from django.urls import path
from .views import *


urlpatterns = [
    path('registration/', render_registration, name = "reg" ),
    path('login/', render_login, name = "login"),
    path('welcome/', render_welcome, name = 'welcome')
]
