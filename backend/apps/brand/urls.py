# apps/brand/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BrandListView.as_view(), name='brand-list'),
    path('<int:pk>/', views.BrandDetailView.as_view(), name='brand-detail'),
    path('search/', views.brand_search_by_name, name='brand-search'),
]
