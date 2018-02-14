from django.urls import path
from .views import ProductListView, ProductDetailView, ProductEdit


urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/edit', ProductEdit.as_view(), name='product-edit'),
]
