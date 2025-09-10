# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class USER(AbstractUser):
    full_name = models.CharField(max_length=150, verbose_name="姓名")
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True, verbose_name="手机号")
    created_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_users',
        verbose_name="创建者"
    )

    class Meta:
        db_table = 'USER'
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username