from rest_framework import serializers
from .models import Region


class RegionSerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(
        queryset=Region.objects.all(),
        source='parent',
        allow_null=True,
        required=False
    )

    class Meta:
        model = Region
        fields = ['id', 'name', 'level', 'parent_id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['parent_id'] = instance.parent.id if instance.parent else None
        return representation


class RegionTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    parent_id = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ['id', 'name', 'level', 'parent_id', 'children']

    def get_children(self, obj):
        children = obj.children.all()
        return RegionTreeSerializer(children, many=True).data

    def get_parent_id(self, obj):
        return obj.parent.id if obj.parent else None
