
from django.urls import reverse
from tabnanny import verbose
from django.db import models

#this is the categories class for the product categories in my shop.
class category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length= 100, unique=True)
    discribtion = models.TextField(max_length=500, blank= True)
    image = models.ImageField(upload_to ='photos/categories', blank=True)

    # the model catagory has its plural as categorys in the database, so i want to correct 
    # it below.

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args = [self.slug])

    def __str__(self):
        return self.name


