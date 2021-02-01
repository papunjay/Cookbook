from django.contrib import admin
from .models import cookbook_dishes,dish_Comment
# Register your models here.
admin.site.register(cookbook_dishes)
# admin.site.register(Comment)
admin.site.register(dish_Comment)


