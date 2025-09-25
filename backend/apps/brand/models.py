from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=255, verbose_name="品牌名称")
    description = models.TextField(verbose_name="描述")

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = "品牌"
