from django.contrib import admin
from .models import Product

class productAdmin(admin.ModelAdmin):
    list_display    = ('name','price','stock','category', 'date_modified','is_available',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, productAdmin)

# Register your models here.
