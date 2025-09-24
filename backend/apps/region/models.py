from django.db import models

class Region(models.Model):
    LEVEL_CHOICES = [
        ('city', 'City'),
        ('district', 'District'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'region'
