from django.shortcuts import render
from .models import  cookbook_dishes,dish_Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm 
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def home(request):
    all_dishes =  cookbook_dishes.objects.order_by('-created_date')
    select_cuisine=cookbook_dishes.objects.values_list('type_of_cuisine',flat=True).distinct()
    data={

        'all_dishes': all_dishes,
        'select_cuisine':select_cuisine,
    }

   
def search(request):
    search_data = cookbook_dishes.objects.order_by('-created_date')
    #cuisine_select = cookbook_dishes.objects.values_list('type_of_cuisine',flat=True).distinct()

    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            search_data=search_data.filter(dish_name__icontains=keyword)

    if 'type_of_cuisine' in request.GET:
        type_of_cuisine =request.GET['type_of_cuisine']
        if  type_of_cuisine:
            search_data=search_data.filter(type_of_cuisine__iexact=type_of_cuisine)

    data={
      'search_data':search_data,
      #'cuisine_select':cuisine_select,
    }
    return render(request,'cuisine/search.html',data)
