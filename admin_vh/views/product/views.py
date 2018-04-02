import decimal
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from shop.models import (
    ParameterValue,
    Product,
    Parameter,
    ProductParameter,
    Category,
)
from .forms import (
    ProductAddForm,
    CategoryAddForm,
)


class ProductCreateView(generic.CreateView):
    form_class = ProductAddForm
    template_name = 'admin_vh/product/product-create.html'
    model = Product

    def get_success_url(self):
        return reverse('manager:product-edit', kwargs={'pk': self.object.pk})


class ProductEdit(generic.DetailView):
    template_name = 'admin_vh/product/product_edit.html'
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
        return render(self.request, 'admin_vh/product/partials/_add-parameters.html', context)

    def get_parameter_value(self):
        data = []
        for i in ParameterValue.objects.filter(parameter_id__exact=self.request.POST.get('parameter_id')):
            data.append({'id': i.id, 'value': i.value})
        return JsonResponse(data, safe=False)

    def save(self, product):
        parameters = [i for i in Parameter.objects.filter(id__in=self.request.POST.getlist('parameter'))]
        parameter_choice_values = [i for i in ParameterValue.objects.filter(id__in=self.request.POST.getlist('parameter-choice-value'))]
        parameter_custom_values = self.request.POST.getlist('parameter-custom-value')

        all_parameters = [i.value.lower() for i in ParameterValue.objects.all()]

        ProductParameter.objects.filter(product=product).delete()

        for index, parameter in enumerate(parameters):
            if parameter_custom_values[index]:
                if parameter_custom_values[index].lower() in all_parameters:
                    pp = ProductParameter(
                        product=product,
                        parameter=parameter,
                        value=ParameterValue.objects.get(value__iexact=parameter_custom_values[index]),
                    )
                    pp.save()
                else:
                    new_param_value = ParameterValue(
                        parameter=parameter,
                        value=parameter_custom_values[index]
                    )
                    new_param_value.save()
                    pp = ProductParameter(
                        product=product,
                        parameter=parameter,
                        value=ParameterValue.objects.get(id=new_param_value.pk),
                    )
                    pp.save()
            else:
                pp = ProductParameter(
                    product=product,
                    parameter=parameter,
                    value=parameter_choice_values[index],
                )
                pp.save()

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


class ProductListView(generic.ListView):
    template_name = 'admin_vh/product/product-list.html'
    context_object_name = 'products'
    model = Product


class CategoryListView(generic.ListView):
    template_name = 'admin_vh/product/category-list.html'
    context_object_name = 'categories'
    model = Category


class CategoryCreateView(generic.CreateView):
    form_class = CategoryAddForm
    template_name = 'admin_vh/product/category-create.html'
    model = Category

    def get_success_url(self):
        return reverse('manager:category-edit', kwargs={'pk': self.object.pk})


class CategoryEdit(generic.UpdateView):
    form_class = CategoryAddForm
    template_name = 'admin_vh/product/category-create.html'
    model = Category

    def get_success_url(self):
        return reverse('manager:category-list')
