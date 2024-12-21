from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.utils import IntegrityError
from django.contrib.auth import login, authenticate, logout


def render_registration(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            try:
                User.objects.create_user(username = username, password = password)
                return redirect('login')
            except IntegrityError:
                messages.error(request=request, message="Такий користувач вже існує")
                return redirect('reg')
        else:
            messages.error(request=request, message = 'Паролі не співпадають')
            return redirect('reg')
    return render(request = request, template_name = "user_app/registration.html")


def render_login(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request= request, message = "Логін або пароль не вірні")
            return redirect('login')
    return render(request, "user_app/login.html")


def render_welcome(request):
    return render(request, 'user_app/welcome.html')

    