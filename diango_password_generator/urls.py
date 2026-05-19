"""
URL configuration for diango_password_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from vault import views

# 2 варианта обработки маршрута
urlpatterns = [
    path("admin/", admin.site.urls),
    path("generator/", include("vault.urls")),
    path('', views.home, name='home'),
    path('main-page-1/', views.main_page_1, name='main_page_1'),
    path('main-page-2/', views.main_page_2, name='main_page_2'),
    path('main-page-3/', views.main_page_3, name='main_page_3'),
    path("users/",include("vault.urls"))

]
