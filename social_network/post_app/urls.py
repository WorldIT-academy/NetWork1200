from django.urls import path
from .views import render_all_posts, render_create_post, render_create_tag, render_all_tags

urlpatterns = [
    path("all/", view= render_all_posts, name = "all_posts"),
    path("create/", view = render_create_post),
    path('create_tag/', view = render_create_tag, name="create_tag"),
    path('all_tags/', view = render_all_tags, name = 'all_tags')
]