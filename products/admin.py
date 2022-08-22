from django.contrib import admin
from .models import ProductModel, Review

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(Review)