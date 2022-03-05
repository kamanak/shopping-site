from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_product_item"]= Product.objects.all()
        return context

class ContactView(TemplateView):
    template_name = "contact.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ProductDetailView(TemplateView):
    template_name = "productdetail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        product =Product.objects.get(slug=url_slug)
        context['product']=product
        return context

class AllProducts(TemplateView):
    template_name="allproducts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allproducts"] =Category.objects.all() 
        return context

class AddToCart(TemplateView):
    template_name = "addtocart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs["pro_id"]
        product_obj = Product.objects.get(id=product_id)
        context["product"] =product_obj 
        return context
    
    


        