from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup_page/',views.signuppage,name='signup_page'),
    path('login_page/',views.loginpage,name='login_page'),
    path('login/',views.handleLogin,name='login'),
    path('logout/',views.handleLogout,name='logout'),
    path('signup/',views.handleSignup,name='signup'),
    path('delete/<str:pk>', views.delete, name='delete')
]
