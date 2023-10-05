from django.db import models

# Create your models here.
from shared.models import Mechanic


class MachinePart(models.Model):
    class Meta:
        db_table = 'machine_part'

    name = models.CharField(max_length=50)
    serial_no = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='pics', blank=True)
    price = models.FloatField(blank=True)
    tags = models.CharField(max_length=100, blank=True)
    material = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50)
    made_in = models.CharField(max_length=50)
    owner = models.ForeignKey(Mechanic, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.serial_no}'


class Category(models.Model):
    class Meta:
        db_table = 'machine_part_category'

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics', blank=True)

    def __str__(self):
        return f'{self.name}'
