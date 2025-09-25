# apps/brand/views.py
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Brand
from .serializers import BrandSerializer

class BrandListView(generics.ListCreateAPIView):
    """
    品牌列表展示和创建品牌
    GET: 获取品牌列表
    POST: 创建新品牌
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['brand_name']
    filterset_fields = ['brand_name']

class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    品牌详情、更新和删除
    GET: 获取品牌详情
    PUT: 更新品牌信息
    PATCH: 部分更新品牌信息
    DELETE: 删除品牌
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

@api_view(['GET'])
def brand_search_by_name(request):
    """
    根据名称查找品牌
    """
    name = request.query_params.get('name', None)
    if name:
        brands = Brand.objects.filter(brand_name__icontains=name)
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
    return Response({"error": "请输入品牌名称参数"}, status=400)
