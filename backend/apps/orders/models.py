from django.db import models
from apps.projects.models import Project
from apps.supplier.models import Supplier
from apps.category.models import Category,CategorySpecification
from apps.brand.models import Brand
from apps.users.models import USER

class Order(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="项目")
    arrival_date = models.DateField(verbose_name="到货时间")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="供应商")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="物资类别")
    CategorySpecification = models.ForeignKey(CategorySpecification, on_delete=models.CASCADE, verbose_name="规格")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="数量")
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="采购价")
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="折扣率")
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="总金额")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="品牌")
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='created_orders', verbose_name="创建用户")

    def __str__(self):
        return f"Order {self.id}"

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"
        db_table = 'orders'
