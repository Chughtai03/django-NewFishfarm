#from typing import Pattern
from django.urls import path
from fishfarm import views
urlpatterns = [
    path('', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    path('register', views.register,name='register'),
    path('login', views.signin,name='login'),
    path('myaccount', views.myaccount,name='myaccount'),
    path('about', views.about,name='about'),
    path('ourteam', views.ourteam,name='ourteam'),
    path('logout', views.Logouts , name='logout'),
    path('store', views.store, name='store'),
#add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
]