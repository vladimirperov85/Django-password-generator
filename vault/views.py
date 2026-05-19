from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'vault/home.html')

def about(request):
    return render(request,'vault/about.html')

def help(request):
    return render(request,'vault/help.html')

def contacts(request):
    return render(request,'vault/contacts.html')

def datail(request):
    return render(request,'vault/datail.html')

def feedback(request):
    return render(request,'vault/feedback.html')

def info(request):
    return render(request,'vault/info.html')

def main_page_1(request):
    return render(request,'vault/main-page-1.html')

def main_page_2(request):
    return render(request,'vault/main-page-2.html')


def main_page_3(request):
    return render(request,'vault/main-page-3.html')


def gen_page_1(request):
    return render(request,'vault/gen-page-1.html')


def gen_page_2(request):
    return render(request,'vault/gen-page-2.html')

def gen_page_3(request):
    return render(request,'vault/gen-page-3.html')

def news_page_1(request):
    return render(request,'vault/news-page-1.html')

def news_page_2(request):
    return render(request,'vault/news-page-2.html')

def news_page_3(request):
    return render(request,'vault/news-page-3.html')