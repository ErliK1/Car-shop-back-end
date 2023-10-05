from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER = [
    [1, 'Male'],
    [2, 'Female'],
]


class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.PositiveIntegerField(null=True)
    gender = models.CharField(choices=GENDER, max_length=10)
    icon = models.ImageField(upload_to='pics', null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'