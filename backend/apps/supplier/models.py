from django.db import models

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255, verbose_name="供应商名称")

    def __str__(self):
        return self.supplier_name

    class Meta:
        verbose_name = "供应商"
        verbose_name_plural = "供应商"
        db_table = 'supplier'