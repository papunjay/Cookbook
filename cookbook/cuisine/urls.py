from django.urls import path
from django.conf.urls.static import static
from .import views


urlpatterns = [ 
   
   path('',views.home,name="home"), 
   path('search',views.search,name="search"),
   path('add_dishes',views.add_dishes,name="add_dishes"),
   path('<int:id>',views.dish_details,name="dish_details"),
   #path('<int:id>',views.favorite_add,name="favorite_add"),
   #path('favorite_list',views.favorite_list,name="favorite_list"),
   #path('<int:id>',views.post_detailview,name="post_detailview") ,
   #path('<int:id>',views.youtubers_details,name="youtubers_details"),
   #path('comment/<str:course>/<str:chapter>/<str:video>/<str:uname>', views.comment, name='comment'),
   #path('favorite_dish',views.favorite_dish,name="favorite_dish")
]