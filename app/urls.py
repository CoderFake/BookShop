from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path("register/", views.register, name="register"),
    path("login/", views.loginPage, name = "login"),
    path('detail/', views.detail, name='detail'),    
    path('information/', views.information, name='information'),    
    path("logout/", views.logoutPage, name = "logout"),
    path("search/", views.search, name = "search"),
    path("category/", views.category, name = "category"),
    path('cart/',views.cart, name="cart"),
    path('checkout/', views.checkout, name = 'checkout'),
    path("gioithieu/", views.gioithieu, name= 'gioithieu'),
    path("lienhe/", views.lienhe, name="Lienhe"),
    path("update_item/", views.updateItem, name = "updateItem"),
    path('place_order', views.place_order, name = "place_order"),
]