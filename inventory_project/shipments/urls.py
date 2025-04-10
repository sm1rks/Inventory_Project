from django.urls import path
from . import views

app_name = 'shipments'

urlpatterns = [
    path('store-shipments/', views.store_shipments, name='store_shipments'),
    path('edit/<int:shipment_id>/', views.edit_shipment, name='edit_shipment'),
    path('delete/<int:shipment_id>/', views.delete_shipment, name='delete_shipment'),
]