from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    img = models.ImageField(default='images/default.png', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    RATING_TYPE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rating = models.CharField(max_length=10, choices=RATING_TYPE)
    comments = models.TextField(blank=True, null=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.rating + " | " + self.product.name