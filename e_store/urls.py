"""e_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from e_app import views
import django
from django.conf.urls import *
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('login',views.loginuser,name="loginuser"),
    path('logoutuser',views.logoutuser,name="logoutuser"),
    path('signupuser',views.signupuser,name="signupuser"),
    path('change_password',views.change_password,name="change_password"),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('show_cart_item',views.show_cart_item,name='show_cart_item'),
    path('delete_cart_item',views.delete_cart_item,name='delete_cart_item'),
    path('shwo_data_by_price',views.shwo_data_by_price,name='p'),
     #forget password
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)