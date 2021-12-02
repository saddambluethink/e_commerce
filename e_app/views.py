from django.contrib.auth.models import AnonymousUser
from django.http.response import HttpResponseRedirect
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
    else:           
        #items=cartitem.objects.filter(user=request.user)
        products=Product.get_all_products()
        return render(request,'index.html',{'products':products})


def single_item(requests,id):
    product=Product.objects.get(id=id)
    p=product.price*product.discount/100

    return render(requests,'s_item.html',{'product':product,'total_p':p})










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
                #return HttpResponse('login super user')
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
            form.save()
                           #return HttpResponse("user created")
                # for login
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
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
        print(id,'==1=====================')
        product=Product.objects.get(id=id)
       # print(product)
        
        if request.user=='AnonymousUser':
            return redirect('index')
        try:
            check=cartitem.objects.get(product=product,user=request.user)
            i=check.quantity+1
            #print(i,"====i==========")
            check.quantity=i
            check.save()
            return redirect('show_cart_item')
        except:
                obj=cartitem(user=request.user,product=product)
                print('obj',request.user)
                obj.save()
                print("===========================save")
                return redirect('show_cart_item')



@login_required_d
def show_cart_item(request):
    user=request.user
    
    items=cartitem.objects.filter(user=request.user)
   # total price
    total=0
    for item in items:
        a=item.product.price
        total +=a
    return render(request, 'cart_item.html',{'items':items,'total':total,'user':user})




@login_required_d
def delete_cart_item(request):
    if request.method=='POST':
        id=request.POST['id']
        d=cartitem.objects.get(id=id,user=request.user)
        d.delete()
        print(id,'===')
        return redirect('show_cart_item')




def itemquantityplus(request,id):
    print(id,"=======plus=======")
    data=cartitem.objects.get(id=id,user=request.user)
    print(data.quantity)
    qu=data.quantity+1
    data.quantity=qu
    data.save()
    return redirect('show_cart_item')
    


def itemquantityremove(request,id):
   # print(id,"=====remove=========")
    data=cartitem.objects.get(id=id)
    #print(data.quantity)
    qu=data.quantity-1
    if qu==0:
        data.delete()
        return redirect('show_cart_item')
    data.quantity=qu
    data.save()
    return redirect('show_cart_item')




def show_data_by_price(request):
    if request.method=='POST':
        minimumprice=request.POST['price_min']
        maximumprice=request.POST['price_max']
        print("===========================mini", minimumprice,'max',maximumprice)
        price=Product.objects.filter(price__gte =minimumprice, price__lte =maximumprice)
        print(price)
        return render(request, 'price.html',{'data':price})
    price=Product.objects.all()     
    return render(request, 'price.html',{'data':price})




def check_out(request,id):
    print(id,"==================")
    item=cartitem.objects.get(id=id)
    pric=item.product.price
    d=item.product.discount
    qu=item.quantity
    print("========",pric,qu)
    dpp=pric-(pric*d/100)
    dp=dpp*qu
    total=pric*qu
    print('total price:',total,dp)
    return render(request,'checkout.html',{'data':item,'total_price':total,'dp':dp})




def payment(requests):
    print("======45=====")
    # price=requests.POST['price']
    # id=requests.POST['id']
    # print("=============",price,id)
    return render(requests,'payment.html')



def ratingp(requests):
    id=requests.POST['id']
    st=requests.POST['fav_language']
    print(id,st,"=============")
    product=Product.objects.get(id=id)
    #if rating.objects.get(product=product,user=requests.user).exist:
    try:   
        pr=rating.objects.get(product=product,user=requests.user)
        pr.prating=st
        pr.save()
        print("inner if")
        return HttpResponseRedirect(f's_item/{id}')
    except:   
        s=rating(user=requests.user,product=product,prating=st)
        s.save()
        print("inner else")
        return HttpResponseRedirect(f's_item/{id}')