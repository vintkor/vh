from django.contrib import admin
from django.urls import path
from .views import PageList, PageDetail

urlpatterns = [
    path('', PageList.as_view(), name='page-list'),
    path('<int:pk>/', PageDetail.as_view(), name='page-detail'),
]
