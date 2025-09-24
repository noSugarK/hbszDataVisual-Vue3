from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Region
from .serializers import RegionSerializer, RegionTreeSerializer


class RegionListCreateView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get_queryset(self):
        queryset = Region.objects.all()
        level = self.request.query_params.get('level', None)
        parent_id = self.request.query_params.get('parent_id', None)

        if level:
            queryset = queryset.filter(level=level)

        if parent_id:
            if parent_id.lower() == 'null':
                queryset = queryset.filter(parent__isnull=True)
            else:
                queryset = queryset.filter(parent_id=parent_id)

        return queryset


class RegionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


@api_view(['GET'])
def region_tree(request):
    # 获取所有顶级区域（城市）
    root_regions = Region.objects.filter(parent__isnull=True)
    serializer = RegionTreeSerializer(root_regions, many=True)
    return Response(serializer.data)
