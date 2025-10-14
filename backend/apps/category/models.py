from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name="物资类别名称")
    
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "物资类别"
        verbose_name_plural = "物资类别"
        db_table = 'category'


class CategorySpecification(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="物资类别", related_name="specifications")
    specification_name = models.CharField(max_length=255, verbose_name="规格名称")
    
    def __str__(self):
        return f"{self.category.category_name} - {self.specification_name}"

    class Meta:
        verbose_name = "物资类别规格"
        verbose_name_plural = "物资类别规格"
        db_table = 'category_specification'
        unique_together = ('category', 'specification_name')  # 确保同一类别下规格名称唯一
