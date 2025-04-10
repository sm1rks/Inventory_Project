from inventory_project.decorators import google_login_required
from django.shortcuts import render
from .models import Shipment
from inventory.models import Store


@google_login_required(login_url='/login/')
def storeShipments(request):
    selected_store_id = request.GET.get('store')
    stores = Store.objects.all()
    shipments = Shipment.objects.filter(store_id=selected_store_id) if selected_store_id else []

    context = {
        'store': stores,
        'shipments': shipments,
        'selected_store_id': int(selected_store_id) if selected_store_id else None,
    }

    return render(request, 'shipments/storeShipments.html', context)