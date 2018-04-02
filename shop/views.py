from django.shortcuts import render, redirect
from django.views import generic
from .models import Category, Product, Parameter, ParameterValue
from django.http.response import JsonResponse
import decimal


class ProductListView(generic.ListView):
    template_name = 'shop/product_list.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    model = Product

