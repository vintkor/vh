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


class ProductEdit(generic.DetailView):
    template_name = 'shop/edit/product_detail.html'
    context_object_name = 'product'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parameters'] = Parameter.objects.prefetch_related('parametervalue_set').all()
        return context

    def add_parameter(self, product):
        context = {
            'product': product,
            'parameters': Parameter.objects.all(),
        }
        return render(self.request, 'shop/edit/partials/add-parameters.html', context)

    def get_parameter_value(self):
        data = []
        for i in ParameterValue.objects.filter(parameter_id__exact=self.request.POST.get('parameter_id')):
            data.append({'id': i.id, 'value': i.value})
        return JsonResponse(data, safe=False)

    def save(self, product):
        print('-' * 90)
        print(self.request.POST)

        product.title = self.request.POST.get('product-title')
        product.is_simple = True if self.request.POST.get('product-is_simple') == 'on' else False
        product.price = decimal.Decimal(self.request.POST.get('product-price'))
        product.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def post(self, *args, **kwargs):
        action = self.request.POST.get('action')
        save = self.request.POST.get('save-form', False)
        product = self.get_object()

        if action == 'add-parameter':
            return self.add_parameter(product)

        if action == 'get-parameter-value':
            return self.get_parameter_value()

        if save:
            return self.save(product)
