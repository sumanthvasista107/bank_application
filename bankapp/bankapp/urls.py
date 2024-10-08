"""
URL configuration for bankapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from create_account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-user/', views.register_user, name='register_user'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('login/', views.user_login, name='login'),
    path('user_home/', views.user_home, name='user_home'),
    path('transfer/', views.transfer_funds, name='transfer'),
    path('accounts/', include('django.contrib.auth.urls')),   
]
