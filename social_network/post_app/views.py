from django.shortcuts import render
from .models import Post

# Create your views here.
def render_all_posts(request):
    
    all_posts = Post.objects.all()
    
    return render(
        request, 
        template_name = "post_app/all_posts.html",
        context = {"all_posts": all_posts}
        )
