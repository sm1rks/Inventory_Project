from django.shortcuts import render, redirect, get_object_or_404
from inventory_project.decorators import google_login_required
from .models import Shipment
from inventory.models import Store, Inventory
from .forms import ShipmentForm
from django.urls import reverse

@google_login_required(login_url='/login/')
def store_shipments(request):
    stores = Store.objects.all()
    store_id = request.GET.get('store')
    selected_store = Store.objects.filter(storeID=store_id).first() if store_id else None
    shipments = Shipment.objects.filter(store=selected_store) if selected_store else []

    # Filter items for the selected store
    if selected_store:
        items = Inventory.objects.filter(store=selected_store)
    else:
        items = Inventory.objects.none()  # No items if no store is selected

    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        form.fields['item'].queryset = items  # Limit items to the selected store
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.store = selected_store
            shipment.save()
            # Redirect to the same store's shipments
            return redirect(f"{reverse('shipments:store_shipments')}?store={selected_store.storeID}")
    else:
        form = ShipmentForm()
        form.fields['item'].queryset = items  # Limit items to the selected store

    return render(request, 'shipments/store_shipments.html', {
        'stores': stores,
        'selected_store': selected_store,
        'shipments': shipments,
        'form': form,
    })

@google_login_required(login_url='/login/')
def edit_shipment(request, shipment_id):
    shipment = get_object_or_404(Shipment, pk=shipment_id)
    if request.method == 'POST':
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            # Redirect to the same store's shipments
            return redirect(f"{reverse('shipments:store_shipments')}?store={shipment.store.storeID}")
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, 'shipments/edit_shipment.html', {'form': form, 'shipment': shipment})

@google_login_required(login_url='/login/')
def delete_shipment(request, shipment_id):
    shipment = get_object_or_404(Shipment, pk=shipment_id)
    if request.method == 'POST':
        store_id = shipment.store.storeID
        shipment.delete()
        # Redirect to the same store's shipments
        return redirect(f"{reverse('shipments:store_shipments')}?store={store_id}")
    return render(request, 'shipments/delete_shipment.html', {'shipment': shipment})