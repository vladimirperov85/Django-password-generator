from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime 
from .forms import RegistrationForm,AccountForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_http_methods
from .models import Account
from django.contrib.auth.decorators import login_required
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

def _password_options(request):
    # считываем опции из запроса и при необходимости возвращает пароль.
    # Возвращаемый словарь полей
    # gen_length:текущая длина пароля
    # gen_digits:включены цифры(для чекбокса)
    # gen_special:включены спецсимволы(для чекбока)
    # generated_password:cгенерированный пароль
    # Пароль создается(только если в  GET явно есть generate=1) по нажатию кнопки "Сгенерировать пароль" или None
    
    is_generate = request.GET.get('generate') == '1'
    # длина пароля
    try:
        length = int(request.GET.get('length',16))
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
    
@login_required
def account_list_view(request):
    """ Страница со списком учетных записей"""

    accounts = Account.objects.filter(owner=request.user)
    context = {"accounts":accounts}
    return render(request,template_name= 'vault/account_list.html', context=context)

@require_http_methods(['POST'])
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def account_create_view(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        print(f"[DEBUG] POST-данные: {request.POST}")
        if form.is_valid():
            account = form.save(commit=False)
            account.owner = request.user
            try:
                account.save()
                print(f"[✅ SUCCESS] Account saved: id={account.id}, site={account.site}, owner_id={account.owner_id}")
                return redirect('account_list')
            except Exception as e:
                print(f"[❌ SAVE ERROR] {e}")
        else:
            print(f"[❌ FORM ERRORS] {form.errors}")
    else:
        opts = _password_options(request)
        initial = {}
        if opts.get('generated_password'):
            initial['password'] = opts['generated_password']
        form = AccountForm(initial=initial)
        return render(request, "vault/account_form.html", {'form': form, **opts})

    opts = _password_options(request)
    return render(request, "vault/account_form.html", {'form': form, **opts})


def about(request):
    return render(request, "vault/about.html")

def account_detail_view(request, pk):
    account = Account.objects.filter(pk=pk).first()
    context = {"account":account}
    return render(request,template_name= "vault/account_detail.html",context=context)

def account_edit_view(request,pk):
    # Получаем запись по pk или возвращаем 404
    account = get_object_or_404(Account, pk=pk,owner = request.user)
    if request.method == "POST":
        form = AccountForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_detail',pk = account.pk)
        
        opts = _password_options(request)
    else:
        opts = _password_options(request)
        if opts['generated_password']:
            form = AccountForm(instance=account, 
                            initial={'password': opts['generated_password']})
        else:
            form = AccountForm(instance=account)
    return render(request, "vault/account_form.html", {'form': form, **opts})
    

