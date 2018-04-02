from django import forms
from shop.models import Product, Category


class ProductAddForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'category',)
        model = Product


class CategoryAddForm(forms.ModelForm):
    class Meta:
        fields = ('title',)
        model = Category
