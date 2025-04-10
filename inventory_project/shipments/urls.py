from django.urls import path
from . import views

app_name = 'shipments'

urlpatterns = [
    path('store-shipments/', views.storeShipments, name='storeShipments'),
]