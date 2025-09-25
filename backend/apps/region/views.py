#file:E:\HBSZ\hbszDataVisual-Vue3\backend\apps\region\views.py
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Region
from .serializers import RegionSerializer, RegionTreeSerializer, RegionDetailSerializer
from apps.projects.models import Project

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
    serializer_class = RegionDetailSerializer

@api_view(['GET'])
def region_tree(request):
    # 获取所有顶级区域（省级或市级）
    root_regions = Region.objects.filter(parent__isnull=True)
    serializer = RegionTreeSerializer(root_regions, many=True)
    # 转换字段名以匹配前端需求
    result = []
    for item in serializer.data:
        result.append(transform_region_data(item))
    return Response(result)

@api_view(['GET'])
def region_stats(request):
    """
    获取区域卡片数据统计信息
    返回 projectedCount, nonProjectedCount, totalCount, partnersCount
    """
    # 获取所有项目
    all_projects = Project.objects.all()

    # 统计各类项目数量
    projected_count = all_projects.filter(status='active').count()  # 立项项目数
    non_projected_count = all_projects.filter(status='inactive').count()  # 非立项项目数
    total_count = all_projects.count()  # 总项目数
    partners_count = all_projects.values('created_by').distinct().count()  # 合作伙伴数（根据创建者去重统计）

    data = {
        'projectedCount': projected_count,
        'nonProjectedCount': non_projected_count,
        'totalCount': total_count,
        'partnersCount': partners_count
    }

    return Response(data)

def transform_region_data(region_data):
    transformed = {
        'id': str(region_data['id']),
        'name': region_data['name'],
        'projectCount': region_data['project_count'],
        'children': []
    }

    if 'children' in region_data and region_data['children']:
        for child in region_data['children']:
            transformed['children'].append({
                'id': str(child['id']),
                'name': child['name'],
                'projectCount': child['project_count']
            })

    return transformed