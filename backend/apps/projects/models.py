from django.db import models


class Project(models.Model):
    """
    项目表模型
    """
    STATUS_CHOICES = [
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('closed', 'Closed'),
    ]

    project_name = models.CharField(max_length=255, verbose_name="项目名称")  # 项目名称
    region_id = models.IntegerField(verbose_name="指向地区id")  # 地区ID（外键关联）
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="状态：inactive|active|closed")  # 状态
    created_by = models.IntegerField(verbose_name="创建者ID，关联USER表id")  # 创建者ID（外键关联）

    class Meta:
        db_table = 'project'  # 数据库表名
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.project_name
