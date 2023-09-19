from django.db import models
from Shared.models import Mechanic, User


# Create your models here.

class MachineParts(models.Model):
    class Meta:
        db_table = 'machine_parts'
        verbose_name = 'Pjese Makine'
        verbose_name_plural = 'Pjeset e Makines'
        unique_together = ['name', 'year', 'brand', 'owner']

    name = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    icon = models.ImageField(upload_to='images', null=True)
    tags = models.CharField(max_length=150, null=True)
    post_published = models.DateTimeField(null=True, auto_now_add=True)
    post_last_updated = models.DateTimeField(null=True, auto_now=True)
    stock_capacity = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(Mechanic, on_delete=models.CASCADE)

    # images


class RatingMachineParts(models.Model):
    class Meta:
        db_table = 'machine_parts_rating'

    starts = models.PositiveIntegerField()
    rating_text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    machine_part = models.ForeignKey(MachineParts, on_delete=models.CASCADE, null=True)


class ConcreteCategoryMachineParts(models.Model):
    class Meta:
        db_table = 'machine_parts_category_concrete'

    machine_part = models.OneToOneField(MachineParts, on_delete=models.CASCADE)
    category = models.ForeignKey('CategoryMachineParts', on_delete=models.CASCADE)


class CategoryMachineParts(models.Model):
    class Meta:
        db_table = 'machine_parts_category'

    name = models.CharField(max_length=20)
