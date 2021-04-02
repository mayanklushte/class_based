from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Mobile_Number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    Address = models.CharField(max_length=80)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Pin_Code = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{6}$')])
    Profile_Picture = models.ImageField(upload_to='profile_pic')
    is_customer = models.BooleanField(default=False)
    is_Shop = models.BooleanField(default=False)
    Shop_Name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name + self.last_name
