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