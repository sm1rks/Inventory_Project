from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['itemName', 'quantity']
        widgets = {
            'itemName': forms.TextInput(attrs={'placeholder': 'Item Name'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantity'}),
        }