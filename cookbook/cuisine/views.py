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



def dish_details(request,id):
    select_items=get_object_or_404(cookbook_dishes,pk=id)
    cook_book=get_object_or_404(cookbook_dishes,pk=id)
    count_like=cook_book.dish_like.count()
    is_favourite=False
    if cook_book.favourite.filter(id=request.user.id).exists():
        is_favourite=True
    
    data={

        'select_items' : select_items,
        'is_favourite' : is_favourite,
        'count_like'   :  count_like,
    }
    return render(request,'cuisine/dish_details.html',data)
    
@login_required
def add_dishes(request):
    select_cuisine=cookbook_dishes.objects.values_list('type_of_cuisine',flat=True).distinct()
    if request.method =='POST' and request.FILES['myfile']:
        dish_name=request.POST['dish_name']
        type_of_cuisine=request.POST['type_of_cuisine']
        myfile = request.FILES.get('myfile')
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        url=fs.url(filename)
        description=request.POST['description']
        cook_time=request.POST['cook_time']
        dishes=cookbook_dishes.objects.create( dish_name=dish_name,type_of_cuisine=type_of_cuisine,photo=url,description=description,cook_time=cook_time)
        dishes.save()
        return render(request,'cuisine/add_dishes.html')
    
    data={
        'select_cuisine':select_cuisine
    }
    return render(request,'cuisine/add_dishes.html',data)




@login_required
def add_favourite(request,id):
    #cook_book=get_object_or_404(cookbook_dishes,id=id)
    cook_book_obj= cookbook_dishes.objects.get(pk=id)
    
    if cook_book.favourite.filter(id=request.user.id).exists():
        cook_book.favourite.remove(request.user)
        cook_book,save()
    else:
        cook_book_obj.favourite.add_field(request.user)
        cook_book_obj.save()

    return HttpResponseRedirect(reverse('dish_details',args=[str(id)] ))





def about(request):
    return render(request,'cuisine/about.html')




@login_required
def dish_like(request,id):

    cook_book_obj= cookbook_dishes.objects.get(pk=id)
    cook_book_obj.dish_like.add(request.user)
    cook_book_obj.save()

    return HttpResponseRedirect(reverse('dish_details',args=[str(id)] ))
