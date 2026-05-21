
from django.urls import path
from . import views, register_view

urlpatterns = [ 
    path('register/',register_view, name='register_view'),




    path('about/', views.about, name='about'),
    path('detail/', views.datail, name='datail'),
    path('help/', views.help, name='help'),
    path('contacts/', views.contacts, name='contacts'),
    path('feedback/', views.feedback, name='feedback'),
    path('info', views.info, name='info'),
    path('main_page_1/', views.main_page_1, name='main_page_1'),
    path('main_page_2/', views.main_page_2, name='main_page_2'),
    path('main_page_3/', views.main_page_3, name='main_page_3'),
    path('gen-page-1/', views.gen_page_1, name='gen-page-1'),
    path('gen-page-2/', views.gen_page_2, name='gen-page-2'),
    path('gen-page-3/', views.gen_page_3, name='gen-page-3'),
    path('news/news-page-1/', views.news_page_1, name='news-page-1'),
    path('news/news-page-2/', views.news_page_2, name='news-page-2'),
    path('news/news-page-3/', views.news_page_3, name='news-page-3'),
    path('info/detail/', views.datail, name='detail')
]