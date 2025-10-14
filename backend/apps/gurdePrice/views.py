from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import Count, Max, Min, Avg, Q
from django.http import HttpResponse
import datetime
from datetime import timedelta
import pandas as pd
from .models import GuidePrice
from .serializers import GuidePriceSerializer, GuidePriceListSerializer, GuidePriceCreateSerializer, GuidePriceStatsSerializer


class GuidePriceListCreateView(generics.ListCreateAPIView):
    queryset = GuidePrice.objects.all().order_by('-date')
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return GuidePriceCreateSerializer
        return GuidePriceListSerializer
    
    def get_queryset(self):
        queryset = GuidePrice.objects.all().order_by('-date')
        
        # 筛选参数
        region_id = self.request.query_params.get('region_id', None)
        category_id = self.request.query_params.get('category_id', None)
        specification_id = self.request.query_params.get('specification_id', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        
        if region_id:
            queryset = queryset.filter(region_id=region_id)
        
        if category_id:
            queryset = queryset.filter(category_id=category_id)
            
        if specification_id:
            queryset = queryset.filter(specification_id=specification_id)
            
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
            
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
            
        return queryset


class GuidePriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GuidePrice.objects.all()
    serializer_class = GuidePriceSerializer


@api_view(['GET'])
def guide_price_stats(request):
    """
    获取指导价统计信息
    """
    # 获取总记录数
    total_count = GuidePrice.objects.count()
    
    # 获取最近一个月的记录数
    one_month_ago = datetime.now().date() - timedelta(days=30)
    latest_month_count = GuidePrice.objects.filter(date__gte=one_month_ago).count()
    
    # 获取物资类别数量
    categories_count = GuidePrice.objects.values('category').distinct().count()
    
    # 获取地区数量
    regions_count = GuidePrice.objects.values('region').distinct().count()
    
    # 获取平均价格
    avg_price = GuidePrice.objects.aggregate(avg_price=Avg('unit_price'))['avg_price']
    
    data = {
        'total_count': total_count,
        'latest_month_count': latest_month_count,
        'categories_count': categories_count,
        'regions_count': regions_count,
        'avg_price': avg_price
    }
    
    serializer = GuidePriceStatsSerializer(data)
    return Response(serializer.data)


@api_view(['GET'])
def guide_price_chart_data(request):
    """
    获取指导价图表数据
    """
    region_id = request.query_params.get('region_id', None)
    category_id = request.query_params.get('category_id', None)
    specification_id = request.query_params.get('specification_id', None)
    start_date = request.query_params.get('start_date', None)
    end_date = request.query_params.get('end_date', None)
    
    queryset = GuidePrice.objects.all()
    
    if region_id:
        queryset = queryset.filter(region_id=region_id)
    
    if category_id:
        queryset = queryset.filter(category_id=category_id)
        
    if specification_id:
        queryset = queryset.filter(specification_id=specification_id)
        
    if start_date:
        queryset = queryset.filter(date__gte=start_date)
        
    if end_date:
        queryset = queryset.filter(date__lte=end_date)
    
    # 按日期分组获取平均价格
    chart_data = queryset.values('date').annotate(
        unit_price=Avg('unit_price')
    ).order_by('date')
    
    # 获取物资类别和规格信息
    category_name = ""
    specification_name = ""
    region_name = ""
    
    if category_id:
        try:
            from apps.category.models import Category
            category = Category.objects.get(id=category_id)
            category_name = category.category_name
        except Category.DoesNotExist:
            pass
    
    if specification_id:
        try:
            from apps.specification.models import Specification
            specification = Specification.objects.get(id=specification_id)
            specification_name = specification.specification_name
        except Specification.DoesNotExist:
            pass
    
    if region_id:
        try:
            from apps.region.models import Region
            region = Region.objects.get(id=region_id)
            region_name = region.name
        except Region.DoesNotExist:
            pass
    
    # 格式化数据
    result = {
        'category_name': category_name,
        'specification_name': specification_name,
        'region_name': region_name,
        'data': []
    }
    
    for item in chart_data:
        result['data'].append({
            'date': item['date'].strftime('%Y-%m-%d'),
            'unit_price': float(item['unit_price']) if item['unit_price'] else 0
        })
    
    return Response(result)


def export_guide_price(request):
    """
    导出指导价数据为Excel文件
    """
    # 获取筛选条件
    region_id = request.GET.get('region_id', None)
    category_id = request.GET.get('category_id', None)
    specification_id = request.GET.get('specification_id', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    
    # 构建查询条件
    filters = Q()
    if region_id:
        filters &= Q(region_id=region_id)
    if category_id:
        filters &= Q(category_id=category_id)
    if specification_id:
        filters &= Q(specification_id=specification_id)
    if start_date:
        filters &= Q(date__gte=start_date)
    if end_date:
        filters &= Q(date__lte=end_date)
    
    # 查询数据
    queryset = GuidePrice.objects.filter(filters).select_related(
        'region', 'category', 'specification', 'user'
    ).order_by('-date')
    
    # 转换为DataFrame
    data = []
    for item in queryset:
        data.append({
            '日期': item.date,
            '地区': item.region.name if item.region else '',
            '物资类别': item.category.category_name if item.category else '',
            '规格': item.specification.specification_name if item.specification else '',
            '信息价(元)': item.unit_price,
            '录入人': item.user.username if item.user else ''
        })
    
    df = pd.DataFrame(data)
    
    # 创建HTTP响应
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename=指导价数据_{datetime.datetime.now().strftime("%Y%m%d")}.xlsx'
    
    # 写入Excel文件
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='指导价数据', index=False)
    
    return response
