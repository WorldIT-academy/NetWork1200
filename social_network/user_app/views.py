from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.utils import IntegrityError
from django.contrib.auth import login, authenticate, logout
from .models import Profile


def render_registration(request):
    # Якщо метод запиту post (Якщо користувач відправив форму) 
    if request.method == 'POST':
        # Зберігаємо дані з форми у змінні
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        # Якщо користувач підтвердив пароль
        if password == confirm_password:
            # відловлюємо помилку при спробі зареєструватися під вже існуючим ім'ям
            try:
                # Заносимо користувача до бази даних (створюємо користувача)
                User.objects.create_user(username = username, password = password)
                # переадресовуємо користувача на сторінку логіна
                return redirect('login')
            except IntegrityError:
                # Відображаємо помилку на сторінці
                messages.error(request=request, message="Такий користувач вже існує")
                return redirect('reg')
        else:
            # Відображаємо помилку на сторінці
            messages.error(request=request, message = 'Паролі не співпадають')
            return redirect('reg')
    return render(request = request, template_name = "user_app/registration.html")


def render_login(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Перевіряємо існування користувача по заданним данним | Дані коректні - повертає об'єкт User | Дані не коректні - повертає None
        user = authenticate(request=request, username=username, password=password)
        # Якщо є такий користувач (Якщо користувач ввів вірні дані)
        if user != None:
            # Авторизація користувача
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request= request, message = "Логін або пароль не вірні")
            return redirect('login')
    return render(request, "user_app/login.html")


def render_welcome(request):
    # Якщо користувач авторизований
    if request.user.is_authenticated:
        return render(request, 'user_app/welcome.html')
    else:
       return redirect('login')
    
def logout_user(request):
    # Вихід користувача з акаунту
    logout(request=request)
    return redirect('login')

def render_all_profiles(request):
    all_profiles = Profile.objects.all()
    return render(request, 'user_app/all_profiles.html', context = {'all_profiles': all_profiles})