from rest_framework import serializers
from .models import Category, CategorySpecification


class CategorySpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySpecification
        fields = ['id', 'category', 'specification_name']
        read_only_fields = ['id']


class CategorySerializer(serializers.ModelSerializer):
    specifications = CategorySpecificationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'specifications']
        read_only_fields = ['id']