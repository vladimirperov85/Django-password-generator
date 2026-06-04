from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime 
from .forms import RegistrationForm,AccountForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_http_methods
from .models import Account
import string
import secrets
# -----------генератор пароля
def generate_password(length = 16,use_digits = True,use_special = True):
    # базовый алфавит - буквы в обоих регистрах
    alphabet = string.ascii_letters
    if use_digits:
        alphabet += string.digits
    if use_special:
        alphabet += "!@#$%^&*()-_+="
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def _password_option(request):
    # считываем опции из запроса и при необходимости возвращает пароль.
    # Возвращаемый словарь полей
    # gen_length:текущая длина пароля
    # gen_digits:включены цифры
    # gen_special:включены спецсимволы
    # generated_password:cгенерированный пароль
    # Пароль создается по нажатию кнопки "Сгенерировать пароль"

    is_generate = request.POST.get('generate') == '1'
    # длина пароля
    try:
        length = int(request.POST.get('gen_length',16))
    except (TypeError,ValueError):
        length = 16

    # ограничиваем длину пароля что бы не сломать форму
    length = max(4,min(length,128))
    if is_generate:
        use_digits = request.GET.get('digits') == 'on'
        use_special = request.GET.get('special') == 'on'
        password = generate_password(length = length,
                                    use_digits = use_digits,
                                    use_special = use_special)
    else:
        use_digits = True
        use_special = True
        password = None
    return {"gen_length":length,
            "gen_digits":use_digits,
            "gen_special":use_special,
            "generated_password":password}

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

def account_create_view(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            # привязываем учетную запись к пользователю
            account.owner = request.user
            account.save()
            return redirect('account_list')
        opts = _password_option(request)
    else:
        opts = _password_option(request)
        initial = {}
        if opts['generated_password']:
            initial['password'] = opts['generated_password']
        form = AccountForm(initial=initial)
    context = {'form':form,**opts}
    return render(request, template_name="vault/account_form.html", context=context)


@require_http_methods({'POST'})
def logout_view(request):
    logout(request)
    return redirect('login')


def account_create_view(request):
    # добавление новой учетной записи

    form = AccountForm()
    context = {'form':form}
    return render(request, template_name="vault/account_form.html", context=context)
















def about(request):
    return render(request, "vault/about.html")

