from django.shortcuts import render

# Create your views here.

    path('login',views.login,name="login"),
    path('logout',views.logout_user,name="logout"),
    path('register',views.register,name="register"),

def register(request):
    pass

def login(request):
    pass

def logout(request):
    pass

