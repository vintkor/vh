from django.contrib import admin
from .models import (
    Category, Product, Parameter, ParameterValue,
)


class ParameterValueInline(admin.TabularInline):
    extra = 0
    model = ParameterValue


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_simple', 'price', 'old_price',)
    filter_horizontal = ('parameter',)


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    inlines = (ParameterValueInline,)


@admin.register(ParameterValue)
class ParameterValueAdmin(admin.ModelAdmin):
    pass
