from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, CategorySpecification
from .serializers import CategorySerializer, CategorySpecificationSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all().prefetch_related('specifications')
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().prefetch_related('specifications')
    serializer_class = CategorySerializer


class CategorySpecificationListCreateView(generics.ListCreateAPIView):
    queryset = CategorySpecification.objects.all()
    serializer_class = CategorySpecificationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class CategorySpecificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategorySpecification.objects.all()
    serializer_class = CategorySpecificationSerializer
