from django.db import models

# Create your models here.from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse

cuisine_choices=(
    ('GermanAndhra Pradesh','Andhra Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Manipur','Manipur'),
)


# Create your models here.

class cookbook_dishes(models.Model):

    dish_name=models.CharField(max_length=255)
    type_of_cuisine=models.CharField(choices=cuisine_choices, max_length=255)
    photo=models.ImageField(upload_to='media/%Y/%m')
    description=RichTextField()
    cook_time=models.IntegerField()
    favourite=models.ManyToManyField(User,related_name="favourite",blank=True)
    dish_like=models.ManyToManyField(User,related_name="dish_like",blank=True)
    created=models.DateTimeField(auto_now_add=True)
    created_date=models.DateTimeField(default=datetime.now,blank=True)
    #slug=models.SlugField(max_length=225)
    #person=models.ForeignKey(User, on_delete = models.CASCADE) 
    
    def __str__(self):
        return self.dish_name

    #def get_absolute_url(self):
    #    return reverse('dish_details',args[self.id,self.slug])
        