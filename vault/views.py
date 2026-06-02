from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime 
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_http_methods
from .models import Account


# Create your views here.
def home(request):
    return render(request, "vault/home.html")


def register_view(request) -> HttpResponse:
    
    # if request.user.is_authenticated:
    #     return redirect('/')
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else: # GET
        form = RegistrationForm()
    context = {"form": form}
    return render(request, template_name="vault/register.html", context=context)


def login_view(request):
    """
    кастомная форма аутентификации
    Get - показываем форму с полями логин/пароль
    Post - проверяем форму при успехе - авторизуем пользователя,показыем 
    главную страницу

    """
    if request.user.is_authenticated:
        return redirect('/') # tODO: redirect to main page
    if request.method == "POST":
        # считываем данные из формы
        username = request.POST.get("username",'').strip()
        password = request.POST.get("password",'')
        # проверяем данные - логин/пароль и возвращаем пользователя или None
        user = authenticate(request,username=username, password=password)
        if user is not None:
            # авторизуем пользователя
            login(request,user)
            return redirect('/') # tODO: redirect to main page

        error = "Invalid username or password"
    error = None
    return render(request, template_name="vault/login.html",context={"errors":error})
    

def account_list_view(request):
    """ Страница со списком учетных записей"""

    accounts = Account.objects.filter(owner=request.user)
    context = {"accounts":accounts}
    return render(request,template_name= 'vault/account_list.html', context=context)

@require_http_methods({'POST'})
def logout_view(request):
    logout(request)
    return redirect('login')



















def about(request):
    return render(request, "vault/about.html")

