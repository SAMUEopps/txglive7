from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from txg.views import main_view, signup_view
from cashbag.views import my_recommendations_view

urlpatterns = [
    
    path('', main_view, name='main_view'),

    path('register/', signup_view, name='signup_view'),

    path('<str:ref_code>', main_view, name='main_view'),
    
    path('index/', views.index, name="index"),

    path('register/', views.register, name='register'),

    path('login/', views.loginpage, name='login'),

    path('dashboard/', my_recommendations_view, name='my-recs-view'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('reg_fee/', views.reg_fee, name='reg_fee'),

    #path('investment/', views.investment, name='investment'),

     path('navbar/', views.navbar, name='navbar'),
]    