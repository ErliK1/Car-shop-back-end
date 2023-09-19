from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
GENDER_CHOICES = [
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('OTHER', 'OTHER'),
]


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='Numri I Telefonit')
    location_address = models.CharField(max_length=100, blank=True, verbose_name='Addresa(Lokacioni)')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True, null=True, verbose_name='Gjinia')

    class Meta(AbstractUser.Meta):
        db_table = 'shared_user'


class Mechanic(models.Model):
    class Meta:
        db_table = 'shared_mechanic'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='images')


class BigUser(models.Model):
    class Meta:
        db_table = 'shared_big_user'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
