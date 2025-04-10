from django.urls import path 
from . import views

app_name = 'inventory'

urlpatterns = [
    path('store/', views.inventory, name='store'),
]
