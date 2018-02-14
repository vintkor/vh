from django.shortcuts import render
from .models import Page, Image, Text
from django.views.generic import ListView, DetailView


class PageList(ListView):
    template_name = 'base_field/list_nav.html'
    context_object_name = 'pages'
    model = Page


class PageDetail(DetailView):
    template_name = 'base_field/page.html'
    context_object_name = 'page'

    def get_object(self):
        return Page.objects.get(id=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super(PageDetail, self).get_context_data(**kwargs)
        context['field'] = self.get_object().get_fields()
        return context
