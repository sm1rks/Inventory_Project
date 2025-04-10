from django.shortcuts import render, redirect, get_object_or_404
from .models import Store, Inventory
from .forms import InventoryForm
from inventory_project.decorators import google_login_required
from django.urls import reverse

@google_login_required(login_url='/login/')
def inventory(request):
    stores = Store.objects.all()
    store_id = request.GET.get('stores')
    selected_store = Store.objects.filter(storeID=store_id).first() if store_id else None
    inventory_items = Inventory.objects.filter(store=selected_store) if selected_store else []

    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory_item = form.save(commit=False)
            inventory_item.store = selected_store
            inventory_item.save()
            # Redirect to the same store's inventory
            return redirect(f"{reverse('inventory:store')}?stores={selected_store.storeID}")

    form = InventoryForm()

    return render(request, 'inventory/store.html', {
        'stores': stores,
        'selected_store': selected_store,
        'inventory_items': inventory_items,
        'form': form,
    })

@google_login_required(login_url='/login/')
def edit_inventory_item(request, item_id):
    inventory_item = get_object_or_404(Inventory, pk=item_id)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory_item)
        if form.is_valid():
            form.save()
            # Redirect to the same store's inventory
            return redirect(f"{reverse('inventory:store')}?stores={inventory_item.store.storeID}")
    else:
        form = InventoryForm(instance=inventory_item)
    return render(request, 'inventory/edit_item.html', {'form': form, 'inventory_item': inventory_item})

@google_login_required(login_url='/login/')
def delete_inventory_item(request, item_id):
    inventory_item = get_object_or_404(Inventory, pk=item_id)
    if request.method == 'POST':
        store_id = inventory_item.store.storeID
        inventory_item.delete()
        # Redirect to the same store's inventory
        return redirect(f"{reverse('inventory:store')}?stores={store_id}")
    return render(request, 'inventory/delete_item.html', {'inventory_item': inventory_item})

from .forms import StoreForm

@google_login_required(login_url='/login/')
def edit_store(request, store_id=None):
    store = get_object_or_404(Store, pk=store_id) if store_id else None
    stores = Store.objects.all()  # Fetch all stores for display

    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('inventory:create_store')  # Redirect to the same page after saving
    else:
        form = StoreForm(instance=store)

    return render(request, 'inventory/edit_store.html', {'form': form, 'store': store, 'stores': stores})

@google_login_required(login_url='/login/')
def delete_store(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    if request.method == 'POST':
        store.delete()
        return redirect('inventory:create_store')  # Redirect to the store management page after deletion
    return render(request, 'inventory/delete_store.html', {'store': store})