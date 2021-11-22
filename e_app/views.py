from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import request
# decorator login
from django.contrib.auth.decorators import login_required
from .models import*
#from .forms import*

# user login logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, logout,login,update_session_auth_hash

# Create your views here.


def index(request):
    type=request.GET.get('type')
    print(type)
    
    if type=='man':  
        data =Product.objects.filter(category=type)
        return render(request,'index.html',{'products':data})
    elif type=='woman':              
        data =Product.objects.filter(category=type)
        return render(request,'index.html',{'products':data}) 
    elif type=='child':                                      
        data =Product.objects.filter(category=type)
        return render(request,'index.html',{'products':data})
    elif type=='vagetable':
        type='vagetable&fruits'                                      
        data =Product.objects.filter(category=type)
        return render(request,'index.html',{'products':data})    
    else:           #all shayeri
        products=Product.objects.all()
        return render(request,'index.html',{'products':products})


def loginuser(request):
    if request.method=='POST':
        name=request.POST['name']
        psw=request.POST['password']
        print(name,psw)
        user = authenticate(request, username=name, password=psw)
        print("------------",user)
        if user is not None:
            login(request, user)
            
            if request.user.is_superuser:
                return HttpResponse('login super user')
            return HttpResponse('login mini user')
        else:
            return HttpResponse('incorect password or name')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return HttpResponse("logout user")




def signupuser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            return HttpResponse("user created")
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# change password 
@login_required
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                # session update 
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('userdashboard')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})
    return redirect('login')


def get_products(requests):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})