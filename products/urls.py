from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('view/<str:pk>', views.view, name='view'),
    path('edit/<str:pk>', views.edit, name='edit'),
    path('delete/<str:pk>', views.delete, name='delete'),
]