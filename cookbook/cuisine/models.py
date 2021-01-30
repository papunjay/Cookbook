from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.shortcuts import redirect


cuisine_choices=(
    ('German','German'),
    ('Indian','Indian'),
)


FAVORITE_CHOICES=(
    ('favorite','favorite'),
    ('unfavorite','unfavorite'),
    
)

# Create your models here.

class cookbook_dishes(models.Model):

    dish_name=models.CharField(max_length=255)
    type_of_cuisine=models.CharField(choices=cuisine_choices, max_length=255)
    photo=models.ImageField(upload_to='media/dishes/%Y/%m')
    description=RichTextField()
    cook_time=models.IntegerField()
    favorited=models.ManyToManyField(User,default=None,blank=True,related_name="favorited")
    # created=models.DateTimeField(auto_now_add=True)
    created=models.DateTimeField(auto_now_add=True)
    created_date=models.DateTimeField(default=datetime.now,blank=True)
  

    #person=models.ForeignKey(User, on_delete = models.CASCADE) 
    
    def __str__(self):
        return self.dish_name

class dish_Comment(models.Model):
    cook_dishes=models.ForeignKey(cookbook_dishes,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    userName=models.CharField(max_length=255)
    content=models.TextField()
    #created=models.DateTimeField(default=False)
    created_date=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.content


class favorite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    favorite_dishes=models.ForeignKey(cookbook_dishes,on_delete=models.CASCADE)
    value=models.CharField(choices=FAVORITE_CHOICES,default='unfavorite',max_length=255)
    
    def __str__(self):
        return str(self.favorite_dishes)
