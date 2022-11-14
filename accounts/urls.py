from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import auth_views


urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
]
