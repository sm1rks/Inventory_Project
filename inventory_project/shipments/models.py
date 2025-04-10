from django.db import models
from inventory.models import Inventory, Store

# Create your models here.
class Shipment(models.Model):
    shipmentID = models.AutoField(primary_key=True)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE, db_column='itemID')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='storeID')
    quantityShipped = models.IntegerField()
    expectedArrival = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=200)

class Meta:
    db_table = 'shipments'

def __str__(self):
        return f"ShipmentID: {self.ShipmentID} - item: {self.item} - store: {self.store} - quantityShipped: {self.quantityShipped} - expectedArrival: {self.expectedArrival} - status: {self.status}"