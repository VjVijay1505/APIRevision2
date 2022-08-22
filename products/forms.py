from itertools import product
from django.forms import ModelForm
from .models import ProductModel, Review

import math

class ProductForm(ModelForm):    
    class Meta:
        model = ProductModel
        fields = '__all__'
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'