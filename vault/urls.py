from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("about/", views.about, name="about"),
    path("login/", views.login_view, name="login"),
    path("accounts/", views.account_list_view, name="account_list"),
    path("logout/", views.logout_view, name="logout"),
    path("accounts/new/", views.account_create_view, name="account_create"),
]
