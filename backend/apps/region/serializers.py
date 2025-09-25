from rest_framework import serializers
from .models import Region
from apps.projects.models import Project


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
    project_count = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ['id', 'name', 'children', 'project_count']

    def get_children(self, obj):
        children = obj.children.all()
        return RegionTreeSerializer(children, many=True).data

    def get_project_count(self, obj):
        # 计算当前地区及其所有子地区的项目数量总和
        def get_all_descendant_ids(region):
            ids = [region.id]
            for child in region.children.all():
                ids.extend(get_all_descendant_ids(child))
            return ids

        descendant_ids = get_all_descendant_ids(obj)
        return Project.objects.filter(region_id__in=descendant_ids).count()


class RegionDetailSerializer(serializers.ModelSerializer):
    """
    地区详情序列化器
    """
    parent_name = serializers.SerializerMethodField()
    project_count = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ['id', 'name', 'level', 'parent_id', 'parent_name', 'project_count']

    def get_parent_name(self, obj):
        return obj.parent.name if obj.parent else None

    def get_project_count(self, obj):
        # 计算当前地区及其所有子地区的项目数量总和
        def get_all_descendant_ids(region):
            ids = [region.id]
            for child in region.children.all():
                ids.extend(get_all_descendant_ids(child))
            return ids

        descendant_ids = get_all_descendant_ids(obj)
        return Project.objects.filter(region_id__in=descendant_ids).count()
