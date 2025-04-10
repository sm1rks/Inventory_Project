from django.shortcuts import render
from inventory.models import Store, Inventory
from shipments.models import Shipment
from .decorators import google_login_required

@google_login_required(login_url='/login/')
def dashboard(request):
    stores = Store.objects.all()
    store_data = []

    for store in stores:
        inventory_items = Inventory.objects.filter(store=store)
        shipments = Shipment.objects.filter(store=store)
        store_data.append({
            'store': store,
            'inventory': inventory_items,
            'shipments': shipments,
        })

    return render(request, 'dashboard.html', {
        'store_data': store_data,
    })
