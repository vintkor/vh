from django.urls import path, include
from admin_vh.views.product.views import (
    ProductEdit,
    ProductListView,
    ProductCreateView,
    CategoryListView,
    CategoryCreateView,
    CategoryEdit,
)
from django.views.generic import TemplateView


app_name = 'manager'
urlpatterns = [
    path('', TemplateView.as_view(template_name='admin_base.html'), name='dashboard'),
    path('product/', include([
        path('', ProductListView.as_view(), name='product-list'),
        path('create/', ProductCreateView.as_view(), name='product-create'),
        path('<int:pk>/edit/', ProductEdit.as_view(), name='product-edit'),
    ])),
    path('category/', include([
        path('', CategoryListView.as_view(), name='category-list'),
        path('create/', CategoryCreateView.as_view(), name='category-create'),
        path('<int:pk>/edit/', CategoryEdit.as_view(), name='category-edit'),
    ])),
]
