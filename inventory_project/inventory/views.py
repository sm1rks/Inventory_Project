from inventory_project.decorators import google_login_required
from django.shortcuts import render
from .models import Store, Inventory


@google_login_required(login_url='/login/')
def inventory(request):
    store = None
    inventory_items = []

    # Get the store ID from the GET request
    store_id = request.GET.get('stores', None)

    # Get all stores to populate the drop-down
    stores = Store.objects.all()

    if store_id:
        try:
            # Get the selected store using the provided store ID
            store = Store.objects.get(id=store_id)
            
            # Get inventory items related to the selected store
            inventory_items = Inventory.objects.filter(store=store)
        except Store.DoesNotExist:
            store = None

    return render(request, 'inventory/store.html', {
        'stores': stores,
        'selected_store': store,
        'inventory_items': inventory_items
    })