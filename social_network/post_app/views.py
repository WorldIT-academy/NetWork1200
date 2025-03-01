from django.shortcuts import render, redirect
from .models import Post, Tag
from user_app.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import PostForm, TagForm
from django.contrib.admin.views.decorators import staff_member_required


def render_all_posts(request):
    
    all_posts = Post.objects.all()
    
    return render(
        request, 
        template_name = "post_app/all_posts.html",
        context = {"all_posts": all_posts}
        )

# Декоратор відображає сторінку тільки якщо користувач авторизувався, 
# інашке - перенаправлення на сторінку логіну за вказаним LOGIN_URL у settings.py
@login_required
def render_create_post(request):
    # Якщо відправляється метод POST, тобто якщо користувач надіслав форму
    if request.method == "POST":
        # Створюємо об'єкт форми та наповнюємо даними, які надіслав користувач
        form = PostForm(request.POST, request.FILES)
        # Якщо дані, надіслані користувачем відповідають усім вимогам, описаним у класі PostForm
        if form.is_valid():
            # Отримуємо профіль автора
            author = Profile.objects.get(user = request.user)
            # Зберігаємо усю форму
            form.save(author)
            return redirect("all_posts") 
    else:
        # Створюємо об'єкт порожньої форми
        form = PostForm()
        
    return render(request, template_name = "post_app/create_post.html", context = {'form': form})

@staff_member_required
def render_create_tag(request):
    # Якщо відправляється метод POST, тобто якщо користувач надіслав форму
    if request.method == "POST":
        # Створюємо об'єкт форми та наповнюємо даними, які надіслав користувач
        form = TagForm(request.POST, request.FILES)
        # Якщо дані, надіслані користувачем відповідають усім вимогам, описаним у класі PostForm
        if form.is_valid():
            # Зберігаємо усю форму
            form.save()
            return redirect("all_tags") 
    else:
        # Створюємо об'єкт порожньої форми
        form = TagForm()
        
    return render(request, template_name = "post_app/create_tag.html", context = {'form': form})


def render_all_tags(request):
    tags = Tag.objects.filter(active = True)
    return render(request=request, template_name='post_app/all_tags.html', context = {'tags': tags})