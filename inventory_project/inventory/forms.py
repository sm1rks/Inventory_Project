from django import forms
from .models import Inventory, Store

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['itemName', 'quantity']
        labels = {
            'itemName': 'Item Name',
            'quantity': 'Quantity',
        }
        widgets = {
            'itemName': forms.TextInput(attrs={'placeholder': 'Item Name'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantity'}),
        }

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']
        labels = {
            'name': 'Store Name',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Store Name', 'class': 'form-control'}),
        }