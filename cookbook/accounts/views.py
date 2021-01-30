from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"you are successfully login")
            return redirect('home')
        else:
            messages.error(request,"wrong password")
            return redirect('login')
    return render(request,'accounts/login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

@csrf_protect
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name =request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirm_password']

        if password == confirmPassword:

            if User.objects.filter(username=username).exists():
                messages.error(request,'Username exists')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exists')
                    return redirect('register')

                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                    user.save()
                    messages.success(request,"Resister successfull")
                    print("done")
                    return redirect('login')

        else:
            messages.error(request,'password should be same')
            return redirect('register')
    
    return render(request,'accounts/register.html')
