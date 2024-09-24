from django.urls import path
from . import views

urlpatterns = [
    path('register-user/', views.register_user, name='register_user'),
    path('.admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_home/', views.user_home, name='user_home'),
    path('login/', views.login_view, name='login'),
    path('transfer/', views.transfer_funds, name='transfer'),

]