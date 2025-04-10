from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('store/', views.inventory, name='store'),
    path('create/', views.edit_store, name='create_store'),
    path('edit-store/<int:store_id>/', views.edit_store, name='edit_store'),
    path('delete-store/<int:store_id>/', views.delete_store, name='delete_store'),  # New URL for deleting a store
    path('edit/<int:item_id>/', views.edit_inventory_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_inventory_item, name='delete_item'),
]