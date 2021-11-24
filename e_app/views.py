from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import request
# decorator login
from .decorators import login_required_d
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
        data =Product.get_products_by_category(type)
        return render(request,'index.html',{'products':data})
    elif type=='woman':              
        data =Product.get_products_by_category(type)
        return render(request,'index.html',{'products':data}) 
    elif type=='child':                                      
        data =Product.get_products_by_category(type)
        return render(request,'index.html',{'products':data})
    elif type=='vagetable':
        type='vagetable&fruits'                                      
        data =Product.get_products_by_category(type)
        return render(request,'index.html',{'products':data}) 
    else:           #all shayeri
        
        #items=cartitem.objects.filter(user=request.user)
        products=Product.get_all_products()
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
            
            # if request.user.is_superuser:
            #     return HttpResponse('login super user')
            return  redirect('index') #HttpResponse('login mini user')
        else:
            return HttpResponse('incorect password or name')
    return render(request,'login.html')

@login_required
def logoutuser(request):
    logout(request)
    return redirect('index')




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

#@login_required
@login_required_d
def add_to_cart(request):
    if request.method=='POST':
        id=request.POST['id']
        print(id,'=======================')
        product=Product.objects.get(id=id)
        print(product)
        if request.user=='AnonymousUser':
            return redirect('index')
        obj=cartitem(user=request.user,product=product)
        print('obj',request.user)
        obj.save()
        return redirect('index')

@login_required_d
def show_cart_item(request):
    #user=request.user
    
    items=cartitem.objects.filter(user=request.user)
    total=0
    for item in items:
        a=item.product.price
        total +=a
    return render(request, 'cart_item.html',{'items':items,'total':total})

@login_required_d
def delete_cart_item(request):
    if request.method=='POST':
        id=request.POST['id']
        d=cartitem.objects.get(id=id)
        d.delete()
        print(id,'===')
        return redirect('show_cart_item')


def shwo_data_by_price(request):
    price=Product.objects.all()
    # for pr in price:
    #     if pr.price<=300 and pr.price>=900:
    #         print('===========',pr.price)
        
    return render(request, 'price.html',{'price':price})