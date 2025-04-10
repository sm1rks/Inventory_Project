from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['item', 'quantityShipped', 'expectedArrival', 'status']
        labels = {
            'item': 'Select Item',
            'quantityShipped': 'Quantity Shipped',
            'expectedArrival': 'Expected Arrival Date',
            'status': 'Shipment Status',
        }
        widgets = {
            'item': forms.Select(attrs={
                'placeholder': 'Select Item',
                'class': 'form-control',
                'style': 'max-width: 230px;',
            }),
            'quantityShipped': forms.NumberInput(attrs={
                'placeholder': 'Enter Quantity',
                'class': 'form-control',
            }),
            'expectedArrival': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'status': forms.TextInput(attrs={
                'placeholder': '(e.g., In Transit, Delivered)',
                'class': 'form-control',
            }),
        }