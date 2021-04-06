from django.db import models
from accounts.models import *
from django.conf import settings


class Products(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=120)
    Price = models.IntegerField()
    Brand = models.CharField(max_length=120)
    Product_Image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return f'{self.Product_Name} of {self.user.get_full_name()}'
