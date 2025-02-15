from django.urls import path
from .views import render_all_posts, render_create_post

urlpatterns = [
    path("all/", view= render_all_posts, name = "all_posts"),
    path("create/", view = render_create_post),
]