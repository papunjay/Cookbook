from django.urls import path
from django.conf.urls.static import static
from .import views

urlpatterns = [ 
    path('login',views.login,name="login"),
    path('logout',views.logout_user,name="logout"),
    path('register',views.register,name="register"),

 
]