from unicodedata import category
from django.db import models
from category . models import Category
from django.utils.safestring import mark_safe
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    product_slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to = 'photos/products')
    images1 = models.ImageField(upload_to = 'photos/products', null=True, blank=True)
    images2 = models.ImageField(upload_to = 'photos/products', null=True, blank=True)
    images3 = models.ImageField(upload_to = 'photos/products',null=True, blank=True)
    images4 = models.ImageField(upload_to = 'photos/products', null=True, blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    # def thumbnail(self):
    #     return mark_safe('<img src="{}" width="70" height="50"?>' .format(self.images.url))
    # images.allow_tags = 'True'
    
    