from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(),name="home"),
    path('contact/', ContactView.as_view(),name="contact"),
    path('about/', AboutView.as_view(),name="about"),
    path('product/<slug:slug>', ProductDetailView.as_view(),name="productdetail"),
    path('all-products',AllProducts.as_view(),name="allproducts"),
    path('add-to-cart/<int:pro_id>',AddToCart.as_view(),name="addtocart"),
    
]