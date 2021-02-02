from django.urls import path
from django.conf.urls.static import static
from .import views

urlpatterns = [ 
   
   path('',views.home,name="home"), 
   path('search',views.search,name="search"),
   path('add_dishes',views.add_dishes,name="add_dishes"),
   path('<int:id>',views.dish_details,name="dish_details"),
   path('<int:id>',views.dish_like,name="dish_like"),
   path('about',views.about,name="about"), 
   path('<int:id>',views.add_favourite,name="add_favourite"), 
]