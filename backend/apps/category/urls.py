from django.urls import path
from .views import (
    CategoryListCreateView, 
    CategoryDetailView,
    CategorySpecificationListCreateView,
    CategorySpecificationDetailView
)

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list-create'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('specifications/', CategorySpecificationListCreateView.as_view(), name='specification-list-create'),
    path('specifications/<int:pk>/', CategorySpecificationDetailView.as_view(), name='specification-detail'),
]