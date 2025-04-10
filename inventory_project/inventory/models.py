from django.db import models

# Create your models here.

class Store(models.Model):
    storeID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"name: {self.name} - storeID: {self.storeID}"
    
class Inventory(models.Model):
    itemID = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.itemName} (Qty: {self.quantity})"