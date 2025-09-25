from django.db import models

from apps.category.models import Category


class Specification(models.Model):
    specification_name = models.CharField(max_length=255, verbose_name="规格名称")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="物资类别")

    def __str__(self):
        return self.specification_name

    class Meta:
        verbose_name = "规格"
        verbose_name_plural = "规格"