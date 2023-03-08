from django.db import models
from category.models import category
from django.urls import reverse
# below is my product model 
class Product(models.Model):
    name    = models.CharField(max_length=200, unique=True)
    slug    = models.SlugField(max_length= 200, unique=True)
    description     = models.TextField(max_length=600, blank= True)
    price   = models.IntegerField()
    images  = models.ImageField(upload_to = 'photos/products')
    stock   = models.IntegerField()
    is_available    = models.BooleanField(default= True)
    category    = models.ForeignKey(category, on_delete= models.CASCADE)
    date_added  = models.DateTimeField(auto_now_add=True)
    date_modified   = models.DateTimeField(auto_now= True)

    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name
