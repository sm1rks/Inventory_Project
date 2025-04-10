from inventory_project.decorators import google_login_required
from django.shortcuts import render
from .models import Store, Inventory


@google_login_required(login_url='/users/')
def inventory(request):
    stores = Store.objects.all()
    store_id = request.GET.get('stores')
    selected_store = Store.objects.filter(storeID=store_id).first() if store_id else None
    inventory_items = Inventory.objects.filter(store=selected_store) if selected_store else []

    return render(request, 'inventory/store.html', {
        'stores': stores,
        'selected_store': selected_store,
        'inventory_items': inventory_items,
    })