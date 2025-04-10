from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Store,Inventory

@login_required(login_url='/users/login/')
def inventory(request):
    store = None
    inventory_items = []

    stores = request.GET.get('stores', None)
    
    if stores:
        try:
            Store.objects.get(id=stores)
            inventory_items = Inventory.objects.filter(store=store)
            
        except Store.DoesNotExist:
            store = None

    return render(request, 'inventory/store.html', {'stores': stores, 'selected_store': store, 'inventory_items': inventory_items})