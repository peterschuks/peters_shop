from . import views
from django.urls import path
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('register/', views.register, name= 'register'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    
    # because of the email activation , i have to create a url for the activation link
    path('activate/<uidb64>/<token>/', views.activate, name= 'activate'),
]