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