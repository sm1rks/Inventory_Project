from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('store/', views.inventory, name='store'),
    path('edit/<int:item_id>/', views.edit_inventory_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_inventory_item, name='delete_item'),
]