
from django.urls import path
from . import views  

urlpatterns = [ 
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('contacts/', views.contacts, name='contacts'),
    path('feedback/', views.feedback, name='feedback'),
    path('info', views.info, name='info'),
]