from django.shortcuts import render
from .models import Post, Tag
from user_app.models import Profile
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
def render_all_posts(request):
    
    all_posts = Post.objects.all()
    
    return render(
        request, 
        template_name = "post_app/all_posts.html",
        context = {"all_posts": all_posts}
        )

def render_create_post(request):
    # Якщо відправляється метотд POST, тобто якщо користувач надіслав форму
    if request.method == "POST":
        # Отримуємо заголовок публікації з форми
        title = request.POST.get("title")
        # Отримуємо контент публікації з форми
        content = request.POST.get("content")
        # Отримуємо файл зображення з форми
        image = request.FILES.get('image')
        # Формуємо шлях для зображення
        image_path = os.path.join('images', 'posts', image.name)
        # Створюємо об'єкт файлової системи
        fst = FileSystemStorage()
        # Зберігаємо зображення, вказуючи шлях та об'єкт зображення
        fst.save(image_path, image)
        # Отримуємо користувача, який зараз залогінений
        user = request.user
        # Отримуємо профіль залогіненого користувача
        author_profile = Profile.objects.get(user = user)
        # Отримуємо список тегів з форми
        tags = request.POST.getlist("tags")


    all_tags = Tag.objects.all()

    return render(request, template_name = "post_app/create_post.html", context = {'all_tags': all_tags})
