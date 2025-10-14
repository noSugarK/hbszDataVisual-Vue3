from django.db import models
from apps.category.models import Category,CategorySpecification
from apps.users.models import USER
from apps.region.models import Region

class GuidePrice(models.Model):
    date = models.DateField(verbose_name="日期（月）")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="地区")
    CategorySpecification = models.ForeignKey(CategorySpecification, on_delete=models.CASCADE, verbose_name="规格")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="物资类别")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="信息价")
    user = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name="指向录入用户id")

    def __str__(self):
        return f"GuidePrice {self.id} - {self.date}"

    class Meta:
        verbose_name = "指导价"
        verbose_name_plural = "指导价"
        db_table = 'guide_price'
