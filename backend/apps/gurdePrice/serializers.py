from rest_framework import serializers
from .models import GuidePrice
from apps.category.models import Category
from apps.specification.models import Specification
from apps.region.models import Region


class GuidePriceSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category_name', read_only=True)
    specification_name = serializers.CharField(source='specification.specification_name', read_only=True)
    region_name = serializers.CharField(source='region.name', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = GuidePrice
        fields = '__all__'


class GuidePriceListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category_name', read_only=True)
    specification_name = serializers.CharField(source='specification.specification_name', read_only=True)
    region_name = serializers.CharField(source='region.name', read_only=True)

    class Meta:
        model = GuidePrice
        fields = ['id', 'date', 'category_name', 'specification_name', 'region_name', 'unit_price']


class GuidePriceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuidePrice
        fields = ['date', 'region', 'specification', 'category', 'unit_price']


class GuidePriceStatsSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()
    latest_month_count = serializers.IntegerField()
    categories_count = serializers.IntegerField()
    regions_count = serializers.IntegerField()
    avg_price = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)