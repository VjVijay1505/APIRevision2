from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items.as_view(), name='items'),
    path('items/<str:pk>/', views.item.as_view(), name='item'),
    path('itemsearch/', views.itemsearch.as_view(), name='itemsearch'),
]