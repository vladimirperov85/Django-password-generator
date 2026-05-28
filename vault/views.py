from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime 
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate


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
    return render(request, template_name="vault/index.html",context={"errors":error})
    









def index(request):
    return render(request, "vault/index.html")

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    langs = request.POST.getlist("languages", ["python"])
    return HttpResponse(f"""
                <div>Name: {name}  Age: {age}<div>
                <div>Languages: {langs}</div>
            """)

















def about(request):
    return render(request, "vault/about.html")


def help(request):
    return render(request, "vault/help.html")


def contacts(request):
    return render(request, "vault/contacts.html")


def datail(request):
    return render(request, "vault/datail.html")


def feedback(request):
    return render(request, "vault/feedback.html")


def info(request):
    return render(request, "vault/info.html")


def main_page_1(request):
    return render(request, "vault/main-page-1.html")


def main_page_2(request):
    return render(request, "vault/main-page-2.html")


def main_page_3(request):
    return render(request, "vault/main-page-3.html")


def gen_page_1(request):
    return render(request, "vault/gen-page-1.html")


def gen_page_2(request):
    return render(request, "vault/gen-page-2.html")


def gen_page_3(request):
    return render(request, "vault/gen-page-3.html")


def news_page_1(request):
    return render(request, "vault/news-page-1.html")


def news_page_2(request):
    return render(request, "vault/news-page-2.html")


def news_page_3(request):
    return render(request, "vault/news-page-3.html")
