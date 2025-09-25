from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name="物资类别名称")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "物资类别"
        verbose_name_plural = "物资类别"
