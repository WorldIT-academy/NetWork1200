from django.urls import path
from .views import render_all_posts

urlpatterns = [
    path("all/", view= render_all_posts)
]